dog=dict()
dog={
    'name': 'Bolt',
    'color': 'White',
    'breed': 'Siberian Husky',
    'legs': 4,
    'age': 6
}
print(dog)
print()
#-----------------------------------------

student={
    'first_name':'Abi',
    'last_name':'Kenndey',
    'gender': 'female',
    'age':250,
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'country':'Canada',
    'city':'Toronto',
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
print(student)
print()
#-----------------------------------------

length=len(student)
print('The length of the student dictionary is', length)
print()
#-----------------------------------------


print(student['skills'])
print(type(student['skills']))
print()
#-----------------------------------------

student['skills'].append('Azure')
student['skills'].append('Java')
print(student['skills'])
print()
#-----------------------------------------

print(student.keys())
print()
print(student.values())
print()
print(student.items())
print()
#-----------------------------------------

student.popitem()
print(student)
# deleted the last item in the dictionary
print()
#-----------------------------------------

student.pop('is_married')
print(student)
print()
#-----------------------------------------

del student
print(student) # Error
print()
#-----------------------------------------