dog ={
    'name': 'Buddy',
    'Color':'Gold Brown',
    'Breed':'Golden Retriever',
    'Legs':4,
    'Age':4
}

Student = {
    'First name':'Emily',
    'Last name':'Johnson',
    'Gender':'Female',
    'Age':22,
    'Marital Status':'Single',
    'Skill':['Python','Data Analysis','Public Speaking'],
    'Country':'Canda',
    'City':'Toronto',
    'Address':'123 Mepe Street,Toronto,ON,Canda'
}
print(len(Student))
print(type(Student['Skill']))
Student['Skill'].append('Machine Learning')
print(Student.items())
A = Student.keys()
print(A)
Student.pop('Age')
print(Student)
del dog
