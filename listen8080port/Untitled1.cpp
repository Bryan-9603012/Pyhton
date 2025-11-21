// g++ -std=c++17 proxy.cc -lboost_system -lcurl -lpthread
#include <boost/beast/core.hpp>
#include <boost/beast/http.hpp>
#include <boost/asio.hpp>
#include <boost/algorithm/string.hpp>
#include <nlohmann/json.hpp>
#include <curl/curl.h>
#include <cstdlib>
#include <iostream>
#include <string>
#include <unordered_map>

using tcp = boost::asio::ip::tcp;
namespace http = boost::beast::http;
using json = nlohmann::json;

static size_t curl_write_cb(void* contents, size_t size, size_t nmemb, void* userp) {
    size_t total = size * nmemb;
    std::string* s = static_cast<std::string*>(userp);
    s->append(static_cast<char*>(contents), total);
    return total;
}

std::string url_decode(const std::string& s) {
    std::string out;
    out.reserve(s.size());
    for (size_t i = 0; i < s.size(); ++i) {
        if (s[i] == '%' && i + 2 < s.size()) {
            std::string hex = s.substr(i + 1, 2);
            char ch = static_cast<char>(std::strtol(hex.c_str(), nullptr, 16));
            out.push_back(ch);
            i += 2;
        } else if (s[i] == '+') {
            out.push_back(' ');
        } else {
            out.push_back(s[i]);
        }
    }
    return out;
}

std::unordered_map<std::string, std::string> parse_query(const std::string& target) {
    std::unordered_map<std::string, std::string> kv;
    auto pos = target.find('?');
    if (pos == std::string::npos) return kv;
    std::string qs = target.substr(pos + 1);
    size_t start = 0;
    while (start < qs.size()) {
        size_t amp = qs.find('&', start);
        if (amp == std::string::npos) amp = qs.size();
        std::string pair = qs.substr(start, amp - start);
        size_t eq = pair.find('=');
        if (eq != std::string::npos) {
            std::string k = url_decode(pair.substr(0, eq));
            std::string v = url_decode(pair.substr(eq + 1));
            kv[k] = v;
        } else {
            kv[url_decode(pair)] = "";
        }
        start = amp + 1;
    }
    return kv;
}

json call_openai(const std::string& api_key, const std::string& q) {
    const char* url = "https://api.openai.com/v1/chat/completions";

    json payload = {
        {"model", "gpt-4o-mini"},
        {"messages", json::array({
            json{{"role","system"},{"content","You are an API proxy demo."}},
            json{{"role","user"},{"content", q}}
        })},
        {"temperature", 0.2}
    };

    std::string response_body;
    CURL* curl = curl_easy_init();
    if (!curl) throw std::runtime_error("curl init failed");
    struct curl_slist* headers = nullptr;
    std::string auth = "Authorization: Bearer " + api_key;
    headers = curl_slist_append(headers, auth.c_str());
    headers = curl_slist_append(headers, "Content-Type: application/json");

    std::string payload_str = payload.dump();

    curl_easy_setopt(curl, CURLOPT_URL, url);
    curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
    curl_easy_setopt(curl, CURLOPT_POSTFIELDS, payload_str.c_str());
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, curl_write_cb);
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, &response_body);
    curl_easy_setopt(curl, CURLOPT_TIMEOUT, 30L);

    CURLcode res = curl_easy_perform(curl);
    long status = 0;
    curl_easy_getinfo(curl, CURLINFO_RESPONSE_CODE, &status);
    curl_slist_free_all(headers);
    curl_easy_cleanup(curl);

    if (res != CURLE_OK) throw std::runtime_error(std::string("curl error: ") + curl_easy_strerror(res));
    if (status < 200 || status >= 300) throw std::runtime_error("upstream status " + std::to_string(status) + ": " + response_body);

    return json::parse(response_body);
}

int main() {
    const char* key = std::getenv("OPENAI_API_KEY");
    if (!key) {
        std::cerr << "OPENAI_API_KEY not set\n";
        return 1;
    }
    std::string api_key = key;

    try {
        boost::asio::io_context ioc;
        tcp::acceptor acceptor{ioc, tcp::endpoint(tcp::v4(), 8080)}; // 監聽 8080
        for (;;) {
            tcp::socket socket{ioc};
            acceptor.accept(socket);

            boost::beast::flat_buffer buffer;
            http::request<http::string_body> req;
            http::read(socket, buffer, req); // 讀取一次請求

            http::response<http::string_body> res{http::status::ok, req.version()};
            res.set(http::field::server, "cpp-proxy");
            res.set(http::field::content_type, "application/json");
            res.keep_alive(false);

            try {
                if (req.method() != http::verb::get) {
                    res.result(http::status::method_not_allowed);
                    res.body() = R"({"error":"only GET is allowed"})";
                } else {
                    auto params = parse_query(std::string(req.target()));
                    auto it = params.find("q");
                    if (it == params.end() || it->second.empty()) {
                        res.result(http::status::bad_request);
                        res.body() = R"({"error":"missing query parameter 'q'"})";
                    } else {
                        // 呼叫 OpenAI
                        json data = call_openai(api_key, it->second);
                        std::string content = data["choices"][0]["message"]["content"].get<std::string>();
                        json out = {{"reply", content}};
                        res.body() = out.dump();
                    }
                }
            } catch (const std::exception& e) {
                res.result(http::status::bad_gateway);
                json err = {{"error","upstream_error"},{"detail", e.what()}};
                res.body() = err.dump();
            }

            res.content_length(res.body().size());
            http::write(socket, res);
            boost::system::error_code ec;
            socket.shutdown(tcp::socket::shutdown_send, ec);
        }
    } catch (const std::exception& e) {
        std::cerr << "server exception: " << e.what() << "\n";
        return 1;
    }
}

