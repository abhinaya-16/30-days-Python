# Higher-order functions-
# Where functions are used as parameters
# Return a function
# Modify a function
# Function assigned to a variable

# Function as a parameter
def sum_numbers(nums):  # normal function
    return sum(nums)    # a sad function abusing the built-in sum function :<

def higher_order_function(func, lst):  # function as a parameter
    summation = func(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15
print()
#------------------------------------------------------------------------------------------------

# Function as a return value
def square(x):          # a square function
    return x ** 2

def cube(x):            # a cube function
    return x ** 3

def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3
print()
#------------------------------------------------------------------------------------------------

# Closures
# Allows a nested function to access the outer scope of the enclosing function
# Even after the enclosing function has terminated after the execution of the return statement
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20
print()
#------------------------------------------------------------------------------------------------

# Decorator
# Allows a user to add new functionality to an existing object without modifying its structure.
# A wrapper function is needed because the decorator must return a function not the actual result.
# so technically the decorator function receives and returns the same function.

# Normal function
def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g())          # WELCOME TO PYTHON

## Let us implement the example above with a decorator

'''This decorator function is a higher order function
that takes a function as a parameter'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON

# @uppercase_decorator
# def greeting():
#     return 'Welcome to Python'

# This is actually shorthand for:

# def greeting():
#     return 'Welcome to Python'
# greeting = uppercase_decorator(greeting)

# the function immediately below the decorator is the one being passed as the argument.
# So inside
# def uppercase_decorator(function):
# the parameter function receives function = greeting

# If a string is written by itself and not assigned to a variable, Python simply ignores it:
# Triple-quoted strings as multiline comments, even though they're technically strings.
'''These decorator functions are higher order functions
that take functions as parameters'''

# First Decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

#Decorators will be executed from bottom to top
@split_string_decorator
@uppercase_decorator     # order with decorators is important in this case - .upper() function does not work with lists
def greeting():
    return 'Welcome to Python'
print(greeting())   # ['WELCOME', 'TO', 'PYTHON']

# Accepting Parameters in Decorator Functions
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name))

print_full_name("Asabeneh", "Yetayeh",'Finland')

# Real life-use cases for Closures-
# Page visits
# API requests
# Button clicks
# Event tracking

# Decorators-
# Decorators are useful when you want to add behavior to many functions without rewriting code.
# Logging
# Authentication
# Caching
# Timing
# Rate limiting
# Validation
print()
#------------------------------------------------------------------------------------------------
