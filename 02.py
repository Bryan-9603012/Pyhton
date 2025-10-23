from genericpath import isdir

first_name = 'Asabeneh'
last_name ='Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML','CSS','JS','React','Python']
person_info ={
                'firstname':'Asabeneh',
                'lastname':'Yetayeh' ,
                'country':'Finland',
                'city':'Helsinki',
            }
print('First name:',first_name)
print('First name length:',len(first_name))
print('Last name',last_name)
print('Last name length:',len(last_name))
print('Country:',country)
print('City:',city)
print('Age:',age)
print('Married:',is_married)
print('Skills:',skills)
print('Person info:',person_info)

first_name,last_name,country,age,is_married='Asabeneh','Yetayeh','Helisink',250,True

print(first_name,last_name,country,city,age,is_married)
print('First name',first_name)
print('Last name',last_name)
print('Country',country)
print('Age:',age)
print('Married:',is_married)
