#1-1
# numbers = [-4,-3,-2,-1,0,2,4,6]
# positive_number = []
# negative_number = []
# for num in numbers:
#     if num > 0:
#         positive_number.append(num)
#     else:
#         negative_number.append(num)
# print("正數有:",len(positive_number),"個",positive_number)
# print("負數有",len(negative_number),"個",negative_number)

#1-2
# def flatten(nested_list):
#     flat_list = []
#     for item in nested_list:
#         if isinstance(item, list):
#             flat_list.extend(flatten(item))
#         else:
#             flat_list.append(item)
#     return flat_list
# nested_list = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
# flat_list = flatten(nested_list)
# print("扁平化後的列表:", flat_list)

#1-3
#1-4
# def calculate_bmi(countries):
#     flat_countries = []
#     for item in countries:

#         if isinstance(item,list):
#             flat_countries.extend(calculate_bmi(item))
#         else:
#             flat_countries.append(item)
#     return flat_countries
# countries =[[('Finland','Helsinki')],[('Sweden','Stockholm')],[('Norway','Oslo')]]
# flat_countries = calculate_bmi(countries)
# print("扁平化後的國家列表:", flat_countries)
#1-5
# countries =[[('Finland','Helsinki')],[('Sweden','Stockholm')],[('Norway','Oslo')]]
# result =[]
# for item in countries:
#     for country,capital in item:
#         result.append(f"Country: {country}, Capital: {capital}")
# print(result)
#1-6
# name =[['Asabeneh','Yetayeh'],['David','Smith'],['Donald','Trump'],['Bill','Gates']]
# outpt_string =[', '.join(full_name) for full_name in name]
# print(outpt_string)
#1-7
# get_line_params =lambda x1, y1, x2, y2: ((y2 - y1) / (x2 - x1), y1 - ((y2 - y1) / (x2 - x1)) * x1)
# slope, intercept = get_line_params(2, 3, 5, 11)
# print("Slope:", round(slope,2))
# print("Intercept:", round(intercept,2))