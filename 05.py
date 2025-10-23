empty_list = list()
print(len(empty_list))

fruits = ['banana', 'orange' , 'mango' , 'lemon']
vegetables = ['Tomato' , 'Potato' , 'Cabbage' , 'Onion' , 'Carrot']
animals_products = ['milk' , 'meat' , 'butter' , 'yoghurt']
web_techs = ['HTML','CSS','JS','Reat','Redux','Node','MongDB']
contries = ['Finland','Estonia','Denmark','Sweden','Norway']

print('Fruits:',fruits)
print('Number of fruits:',len(fruits))
print('Vegetables:',vegetables)
print('Number of Vegetables:',len(vegetables))
print('Animals products:',animals_products)
print('Number of Animals products:',len(animals_products))
print('Web Technologies:',web_techs)
print('Number of Web Technologies:',len(web_techs))
print('Number of countries:',len(contries))

fruits = ['banana', 'orange' , 'mango' , 'lemon']
last_fruit = fruits[-1]
second_fruit = fruits[-2]
print(last_fruit)
print(second_fruit)

fruits = ['banana', 'orange' , 'mango' , 'lemon']
all_fruits = fruits[0:4]
all_fruits = fruits[0:]
orange_and_mango = fruits[1:3]
orange_mango_lemon = fruits[1:]

fruits = ['banana', 'orange' , 'mango' , 'lemon']
all_fruits = fruits[-4]
orange_and_mango = fruits[-3:-1]
orange_mango_lemon = fruits[-3:]

fruits = ['banana', 'orange' , 'mango' , 'lemon']
fruits[0] = 'Avocado'
print(fruits)
fruits[1] = 'apple'
print(fruits)
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)

fruits = ['banana', 'orange' , 'mango' , 'lemon']
fruits.append('apple')
print(fruits)
fruits.append('lime')
print(fruits)

fruits = ['banana', 'orange' , 'mango' , 'lemon']
fruits.insert(2,'apple')
print(fruits)
fruits.insert(3,'lime')
print(fruits)

fruits = ['banana', 'orange' , 'mango' , 'lemon']
fruits.pop()
print(fruits)
fruits.pop(0)
print(fruits)

fruits = ['banana', 'orange' , 'mango' , 'lemon']
del fruits[0]
print(fruits)
del fruits[1]
print(fruits)
del fruits
print(fruits)

fruits = ['banana', 'orange' , 'mango' , 'lemon']
fruits.clear()
print(fruits)

fruits = ['banana', 'orange' , 'mango' , 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)

positive_numbers =[1,2,3,4,5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers +zero + positive_numbers
print(integers)
fruits = ['banana', 'orange' , 'mango' , 'lemon']
vegetables = ['Tomato' , 'Potato' , 'Cabbage' ,'Onion' , 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

num1 =[0,1,2,3]
num2 = [4,5,6]
num1.extend(num2)
print('Numbers',num1)
negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1,2,3,4,5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers',negative_numbers)
fruits = ['banana', 'orange' , 'mango' , 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print('Fruits and Vegetables:',fruits)

fruits = ['banana', 'orange' , 'mango' , 'lemon']
print(fruits.count('orange'))
ages = [22,19,24,25,26,24,25,26]
print(ages.count(24))

fruits = ['banana', 'orange' , 'mango' , 'lemon']
print(fruits.index('orange'))
ages = [22,19,24,25,26,24,25,26]
print(ages.index(24))

fruits = ['banana', 'orange' , 'mango' , 'lemon']
fruits.reverse()
print(fruits)
ages = [22,19,24,25,26,24,25,26]
ages.reverse()
print(ages)

fruits = ['banana', 'orange' , 'mango' , 'lemon']
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
ages = [22,19,24,25,26,24,25,26]
ages.sort()
print(ages)
ages.sort(reverse=True)
print(ages)