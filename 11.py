#練習1-1
# def add_two_numbers(a,b):
#     return a + b

#練習1-2
# def garden_area(radius):
#     area = 3.14 * radius * radius
#     return area
# print(garden_area(5))

#練習1-3
# def add_two_numbers(a,b):
#     if isinstance(a, int) and isinstance(b, int):
#         return a + b
#     else:
#         return "請輸入整數"
# print(add_two_numbers(3,5))

#1-4
# def convert_celsius_to_fahrenheit(celsius):
#     fahrenheit = (celsius * 9/5) + 32
#     return fahrenheit
# print(convert_celsius_to_fahrenheit(25))

# #1-5
# def check_season(month):
#     if month in [3, 4, 5]:
#         return "春天"
#     elif month in [6, 7, 8]:
#         return "夏天"
#     elif month in [9, 10, 11]:
#         return "秋天"
#     elif month in [12, 1, 2]:
#         return "冬天"
#     else:
#         return "月份輸入錯誤"
# a=input("請輸入月份:")
# a=int(a)
# month = a
# print(check_season(a))

#1-6
# def calculate_slope(x1, y1, x2, y2):
#     if x2 - x1 == 0:
#         return "斜率不存在"
#     else:
#         slope = (y2 - y1) / (x2 - x1)
#         return slope

#1-7
# def solve_quadratic_eqn(a,b,c,x):
#     result = a * x**2 + b * x + c
#     return result

#1-8

# def print_list(lst):
#     for item in lst:
#         print(item)

#1-9
# def reverse_list(list1,list2):
#     return(list1[::-1],list2[::-1])
# reverse_list3=[1,2,3,4,5]
# reverse_list4=["A","B","C"]
# reverse3,severse4=reverse_list(reverse_list3,reverse_list4)
# print(reverse3)
# print(severse4)

#1-10
# def capitalize_list_items(items):
#     return [item.capitalize() for item in items]
# fruit=["apple","banana","mango"]
# output=capitalize_list_items(fruit)
# print(output)

#1-11
def add_item_to_list(lst,item):
    lst.append(item)
    return lst
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item_to_list(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
numbers = [2, 3, 7, 9]
print(add_item_to_list(numbers, 5))