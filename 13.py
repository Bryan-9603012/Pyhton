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