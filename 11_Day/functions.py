#Function without Parameters
def generate_full_name ():
    first_name = 'Abi'
    last_name = 'Kennedy'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name () # calling a function

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()
print()
#---------------------------------------------------------

#return statement
def generate_full_name ():
    first_name = 'Abi'
    last_name = 'Kennedy'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())

#returning with parameters
def print_full_name(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    return full_name
print_full_name(firstname='Abi', lastname='Kennedy')

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age
print('Age: ', calculate_age(2019, 1819))

def is_even (n):
    if n % 2 == 0:
        return True    # return stops further execution of the function, similar to break 
    return False
print(is_even(10)) # True
print(is_even(7)) # False

def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))
print()
#---------------------------------------------------------

#Function with single parameter
def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings('Abi'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    return total
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
print()
#---------------------------------------------------------

#Function with two parameter:
def generate_full_name (first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print('Full Name: ', generate_full_name('Abi','Kennedy'))

def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(1, 9))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age 
print('Age: ', calculate_age(2021, 1819))

def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to a string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))
print()
#---------------------------------------------------------

#Passing arguements with Key and Value
def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    print(full_name)
print_fullname(firstname = 'Abi', lastname = 'Kennedy')

def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(num2 = 3, num1 = 2)) # Order does not matter 
print()
#---------------------------------------------------------

#Function with default parameters
def greetings (name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Abi'))

def generate_full_name (first_name = 'Abi', last_name = 'Kennedy'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())
print(generate_full_name('David','Smith'))

def calculate_age (birth_year,current_year = 2021):
    age = current_year - birth_year
    return age 
print('Age: ', calculate_age(1821))

def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100)) # 9.81 - average gravity on Earth's surface
print('Weight of an object in Newtons: ', weight_of_object(100, 1.62)) # gravity on the surface of the Moon
print()
#---------------------------------------------------------

# Arbitrary number of arguments-
# When we do not know the number of arguments we pass to our function
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # same as total = total + num 
    return total
print(sum_all_nums(2, 3, 5)) # 10

def generate_groups (team,*args):
    print('Team',team)
    for i in args:
        print(i) 
generate_groups('Team-1','Abi','Brook','David','Eyob')
print()
#---------------------------------------------------------

#Dictionary unpacking:
def greet(name, location):
    print("Hi there", name, "how is the weather in", location)
greet(name="Alice", location="New York")  

# Create a dictionary with keys matching the function's parameter names
my_dict = {"name": "Alice", "location": "New York"}
greet(**my_dict)  
# Call the function using dictionary unpacking
# The ** operator unpacks the dictionary, passing its key-value pairs
# Normally greet(my_dict) would pass as a complete dictionary to parameter name 
# as keyword arguments to the function.
# Output: Hi there Alice how is the weather in New York

# *param for arbitrary number of arguments
# **arg for dictionary unpacking of argument
print()
#---------------------------------------------------------

# Arbitrary number of named arguments:
# Generally avoid this unless required
def arbitrary_named_args(**args):
    print("I received an arbitrary number of arguments, totaling", len(args))
    print("They are provided as a dictionary in my function:", type(args))
    print("Let's print them:")
    for k, v in args.items():
        print(" * key:", k, "value:", v)
arbitrary_named_args(
    first_name="Satoru",
    last_name="Gojo",
    age=28,
    country="Japan",
    technique="Limitless",
    eyes="Six Eyes"
)

#Function as a parameter of another function
#You can pass functions around as parameters
def square_number (n):
    return n ** n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 27
