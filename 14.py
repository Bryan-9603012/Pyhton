#1-4
# countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
# for country in countries:
#     print(country)
#1-5
# name =['Asabemeh','Lidiya','Ermias','Abraham']
# for person in name:
#     print(person)
#1-6
# numbers = [1,2,3,4,5,6,7,8,9,10]
# for number in numbers:
#     print(number)
#2-1
# countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
# output = map(lambda country: country.upper(), countries)
# print(list(output))
#2-2
# numbers = [1,2,3,4,5,6,7,8,9,10]
# squared_numbers = map(lambda x: x ** 2, numbers)
# print(list(squared_numbers))
#2-3
# countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
# output = filter(lambda country: len(country) == 6, countries)
# print(list(output))
#2-4
# countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
# output = filter(lambda country: len(country) >= 6, countries)
# print(list(output))
#2-5
# countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
# output = filter(lambda country: 'land' not in country, countries)
# print(list(output))
#2-6
# countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
# output = filter(lambda country: not country.startswith('E'), countries)
# print(list(output))
#2-7
# from functools import reduce
# arr= [1,2,3,4,5,6,7,8,9,10]
# output = reduce(lambda x,y: x+y, filter(lambda x: x%2==0, map(lambda x: x**2, arr)))
# print(output)
#2-8
# def get_string_lists():
#     countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
#     output = list(map(lambda country: country.upper(), filter(lambda country: len(country) == 6, countries)))
#     return output
# print(get_string_lists())
#2-9
# from functools import reduce
# numbers = [1,2,3,4,5,6,7,8,9,10]
# def add_all_numbers(x,y):
#     return int(x)+int(y)
# total = reduce(add_all_numbers, numbers)
# print(total)
#2-10
# from functools import reduce
# countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
# def concatenate_countries(x,y):
#     return x + ', ' + y
# total_countries = reduce(concatenate_countries, countries)
# print(total_countries)
#2-11
# def categorize_countries():
#     countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
#     europe_countries_1 = list(filter(lambda country: 'land' in country, countries))
#     europe_countries_2 = list(filter(lambda country: 'ia' in country, countries))
#     europe_countries_3 = list(filter(lambda country: 'island' in country, countries))
#     europe_countries_4 = list(filter(lambda country: 'stan' in country, countries))
#     non_europe_countries = list(filter(lambda country: 'land' not in country, countries))
#     return europe_countries_1, non_europe_countries, europe_countries_2, europe_countries_3, europe_countries_4
# europe, non_europe , europe_countries_2, europe_countries_3, europe_countries_4 = categorize_countries()
# print("包含 'land' 的國家:", europe)
# print("不包含 'land' 的國家:", non_europe)
# print("包含 'ia' 的國家:", europe_countries_2)
# print("包含 'island' 的國家:", europe_countries_3)
# print("包含 'stan' 的國家:", europe_countries_4)
#2-12
# def categorize_countries(countries):
#     output ={}
#     for country in countries:
#         first_letter = country[0].upper()

#         if first_letter in output:
#             output[first_letter] += 1
#         else:
#             output[first_letter] = 1
#     return output
# countries = ['Estonia', 'Einland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
# result = categorize_countries(countries)
# print(result)
#2-13
# import json, re
# from pathlib import Path

# def get_first_ten_countries():
#     p = Path(__file__).parent / "countries.json"
#     text = p.read_text(encoding="utf-8")

#     # 去除行註解（若有）
#     text = re.sub(r"^\s*//.*$", "", text, flags=re.MULTILINE)
#     # 將單引號改為雙引號（適用於簡單字串清單）
#     text = text.replace("'", '"')

#     data = json.loads(text)  # 這時已是合法 JSON 了
#     return data[:10]

# print(get_first_ten_countries())
#2-14
# import json, re
# from pathlib import Path

# def get_first_ten_countries():
#     p = Path(__file__).parent / "countries.json"
#     text = p.read_text(encoding="utf-8")

#     # 去除行註解（若有）
#     text = re.sub(r"^\s*//.*$", "", text, flags=re.MULTILINE)
#     # 將單引號改為雙引號（適用於簡單字串清單）
#     text = text.replace("'", '"')

#     data = json.loads(text)  # 這時已是合法 JSON 了
#     return data[16:4:-1]

# print(get_first_ten_countries())

#3-1
# from countries_data import countries
# from operator import itemgetter
# from collections import defaultdict

# def sort_by_name(countries):
#     return sorted(countries, key=lambda c: c.get("name", "").lower())

# def sort_by_capital(countries):
#     return sorted(countries, key=lambda c: (c.get("capital") is None, str(c.get("capital", "")).lower()))

# def sort_by_population(countries):
#     return sorted(countries, key=itemgetter("population"), reverse=True)

# def top_languages_by_population(countries, top_n=10):
#     lang_pop = defaultdict(int)
#     for c in countries:
#         pop = int(c.get("population", 0))
#         for lang in c.get("languages", []):
#             lang_pop[str(lang).strip()] += pop
#     return sorted(lang_pop.items(), key=lambda x: x[1], reverse=True)[:top_n]

# def top_countries_by_population(countries, top_n=10):
#     ranked = sort_by_population(countries)
#     return [(c.get("name", ""), int(c.get("population", 0))) for c in ranked[:top_n]]

# if __name__ == "__main__":
#     print([c["name"] for c in sort_by_name(countries)[:5]])
#     print([c["name"] for c in sort_by_capital(countries)[:5]])
#     print([(c["name"], c["population"]) for c in sort_by_population(countries)[:5]])
#     print(top_languages_by_population(countries, 10))
#     print(top_countries_by_population(countries, 10))

