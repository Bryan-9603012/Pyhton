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
# def add_item_to_list(lst,item):
#     lst.append(item)
#     return lst
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
# print(add_item_to_list(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
# numbers = [2, 3, 7, 9]
# print(add_item_to_list(numbers, 5))
# 1-14
# def sum_of_odds(a):
#     total =0
#     for i in range(a+1):
#         if i%2==0:
#             total+=i
#             i+=1
#     return total
# print(sum_of_odds(100))
#
# 1-15
# def sum_of_odds(a):
#     total =0
#     for i in range(a):
#         if i%2!=0:
#             total+=i
#             i+=1
#     return total
# print(sum_of_odds(100))
#
#2-1
# a= 100
# def evens_and_odds(a):
#     total_odd = 0
#     total_even = 0
#     for i in range(a+1):
#         if i%2==0:
#             total_even+=1
#         else:
#             total_odd+=1
#     return total_even,total_odd
# total_evens,total_odds = evens_and_odds(a)
# print("The number of odds are",total_evens,".")
# print("The number of evens are",total_odds,".")
#
#2-2
# def factorial(a):
#     b =1
#     while a>1:
#         b = b*a
#         a-=1
#     return b
# print(factorial(5))
#
#2-3
# def is_empty(a):
#     return not a
# print(is_empty([]))

#2-4
# import statistics
# def number(a,b,c,d):
#     score=[a,b,c,d]
#     average = statistics.mean(score)
#     median = statistics.median(score)
#     Mode = statistics.mode(score)
#     variance = statistics.variance(score)
#     std = statistics.stdev(score)
#     rng = max(score)-min(score)
#     return average, median, Mode, variance, std, rng

# a=int(input("請輸入數字a:"))
# b=int(input("請輸入數字b:"))
# c=int(input("請輸入數字c:"))
# d=int(input("請輸入數字d:"))

# average, median, Mode, variance, std, rng = number(a,b,c,d)

# print("平均數為:",average)
# print("中位數為:",median)
# print("眾數為:",Mode)
# print("範圍為:",variance)
# print("變異數為:",std)
# print("標準差為:",rng)

#3-1
#def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# a = int(input("請輸入一個數:"))

# a=is_prime(a)
# print(a)

#3-2
# def all_unique(lst):
#     return len(lst) == len(set(lst))
# print(all_unique([1,2,3,4,5]))
# print(all_unique([1,2,3,5,5]))

#3-3
# def all_same_type(lst):
#     return all(type(x) == type(lst[0]) for x in lst)
# print(all_same_type([1,2,3]))
# print(all_same_type([1,2,"dock"]))

#3-4
# import keyword
# def is_valid_variable(name):
#     return (name.isidentifier() and not keyword.iskeyword(name))
# print(is_valid_variable('a'))
# print(is_valid_variable('1nhhuhrk'))
# print(is_valid_variable('for'))
