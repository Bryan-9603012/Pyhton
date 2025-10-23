# 1-1
# age = input('請輸入你的年齡:')
# age = int(age)
# if age < 18:
#     a = 18 - age
#     print('You need %d more years old.' % a)
# else:
#     print('You are old enough learn to drive.')
from tokenize import endpats

#1-2
# You_age = int(input('輸入你的年齡:'))
# my_age = 35
# if You_age > my_age:
#     A = You_age - my_age
#     print('You are %d years older than me' % A)
# else:
#     A = my_age - You_age
#     print('You are %d years younger than me' % A)

#1-3
# a = input('請輸入a:')
# b = input('請輸入b:')
#
# a = int(a)
# b = int(b)
#
# if a>b:
#     print('a大於b')
# elif a<b:
#     print('a小於b')
# else:
#     print('a等於b')

#2-1
# grade = input('請輸入成績:')
# garde = int(grade)
#
# if garde<=100 and garde>=90:
#     print('A')
# elif garde<=89 and garde>=70:
#     print('B')
# elif garde<=69 and garde>=60:
#     print('C')
# elif garde<=59 and garde>=50:
#     print('D')
# else:
#     print('F')

# 2-2
# while True:
#     Month = int(input('請輸入月份:'))
#     season = {
#     'spring':[3,4,5],
#     'summer':[6,7,8],
#     'fall':[9,10,11],
#     'winter':[12,1,2]
#     }
#
#     if Month in season['spring']:
#         print('Spring')
#     elif Month in season['summer']:
#         print('Summer')
#     elif Month in season['fall']:
#         print('Fall')
#     elif Month in season['winter']:
#         print('Winter')
#     elif Month  not in season:
#         print('請輸入1~12月其中一個')

#2-3
# fruits = ['apple','banana','orange']
# fruits_1 = input('Enter fruits:')
# if fruits_1 in fruits:
#     print('That fruit already exists in the list')
# else:
#     fruits.append(fruits_1)
#     print(fruits)

# 3-1
# person = {
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_marred': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
# }
# if 'skills'in person:
#     skills = person['skills']
#     A = len(skills)//2
#     print(skills[A])
# person['skills'].remove('JavaScript')
# person['skills'].remove('React')
#
# skills = set(person['skills'])
# if 'Python' in person['skills']:
#     print('他有Python技能')
# if skills=={'JavaScript', 'React'}:
#     print('他是前端開發人員')
# if skills=={'Node','MongoDB','Python'}:
#     print('他是後端開發人員')
# if skills=={'React','Node','MongoDB'}:
#     print('他是全限開發人員')
#
# if person['is_marred']==True:
#     print('Asabeneh Yetayeh lives in Finland. He is married.')
