family_members = ()
family_members =list(family_members)
sister = ('Ethan')
brother = ('Jim')
family_members.append(sister)
family_members.append(brother)
family_members.append('Marcus')
family_members.append('Ava')
print(family_members)
sister , brother , father , mother= family_members
print('Sister is:',sister)
print('Brother is:',brother)
print('Father is:',father)
print('Mother is:',mother)

fruits = ('banana', 'orange' , 'mango')
vegetables = ('Tomato' , 'Potato' , 'Cabbage')
animals_products = ('milk' , 'meat' , 'butter')
food_stuff_tp = fruits + vegetables + animals_products
food_stuff_tp = list(food_stuff_tp)
print(food_stuff_tp)
print(food_stuff_tp[4])
print(food_stuff_tp[0:3])
print(food_stuff_tp[-3:])
del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)

print(food_stuff_tp)