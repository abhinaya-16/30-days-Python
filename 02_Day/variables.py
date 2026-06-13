#------------------------------------------------
# Functions in python
print('Hello, World!')
length = len('Hello, World!')
print(length)

print()
#------------------------------------------------

type_var = type('Hello, World!')
print(type_var)

print()
#------------------------------------------------

print(int(3.14)) # 3 -> converts float to int
print(float(10)) # 10.0 -> converts int to float
print(str(10)) # '10' -> converts int to string
print(int('10')) # 10 -> converts string to int
print(float('3.14')) # 3.14-> converts string to float
print(str(3.14)) # '3.14' -> converts float to string

print()
#------------------------------------------------
# Input function in python by default takes input as a string, 
# we can convert it to other data types using the type conversion functions.
input_str = input('Enter your name: ')
print('Hello, ' + input_str + '!')

print()
#------------------------------------------------

print(min(20,30,40,50))
print(max(20,30,40,50))
print(min([20,30,40,50]))
print(max([20,30,40,50]))
print(sum([20,30,40,50])) # only takes list as an argument

print()
#------------------------------------------------
# Variables in python
# Snake case example: first_name, last_name, country, age, etc.
# Camel case example: FirstName, LastName, Country, Age, etc.
# Data types don't have to be declared in python,
# we can directly assign a value to a variable and it will automatically determine the data type.

# Variables in Python
first_name = 'Abi'
last_name = 'Kennedy'
country = 'Canada'
city = 'Toronto'
age = 21
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
# This is a dictionary:
person_info = {
   'firstname':'Abi',
   'lastname':'Kennedy',
   'country':'Canada',
   'city':'Toronto'
   }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)
print('Person first name: ', person_info['firstname'])

print()
#------------------------------------------------
# Declaring multiple variables in one line
name, city, yo = 'Gojo', 'Tokyo', 28
print('Name: ', name)
print('City: ', city)
print('Age: ', yo)

print()
#------------------------------------------------
# Types of variables
# Printing out types
print(type('Abi'))               # str
print(type(first_name))          # str
print(type(10))                  # int
print(type(3.14))                # float
print(type(1 + 1j))              # complex
print(type(True))                # bool
print(type([1, 2, 3, 4]))        # list
print(type({'name':'Abi'}))      # dict
print(type((1,2)))               # tuple
print(type(zip([1,2],[3,4])))    # zip

print()
#------------------------------------------------
# str to list
first_name = 'Abhinaya'
print(first_name)               # 'Abhinaya'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 'b', 'h', 'i', 'n', 'a', 'y', 'a']

