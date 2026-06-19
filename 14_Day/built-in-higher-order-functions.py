from functools import reduce
# map(), filter(), reduce()
# These bult-in functions are the best use-case of Lambda functions
# An iterable is any object that can be looped over one item at a time.
# So the function should define what it does to one item in the iterable.

# map()
# So this function applies a calculation to each item of the iterable
# syntax
# map(function, iterable)

numbers = [1, 2, 3, 4, 5] # iterable
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
# Lets apply it with a lambda function
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]

numbers_str = ['1', '2', '3', '4', '5']  # iterable
numbers_int = map(int, numbers_str)
print(list(numbers_int))    # [1, 2, 3, 4, 5]

names = ['Abhinaya', 'Lidiya', 'Ermias', 'Satoru']  # iterable
def change_to_upper(name):
    return name.upper()
names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))    # ['ABHINAYA', 'LIDIYA', 'ERMIAS', 'SATORU']
# Let us apply it with a lambda function
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))    # ['ABHINAYA', 'LIDIYA', 'ERMIAS', 'SATORU']
print()
#------------------------------------------------------------------------------------------------

# filter()
# syntax
# filter(function, iterable)
# Lets filter only even nubers
numbers = [1, 2, 3, 4, 5]  # iterable
def is_even(num):
    if num % 2 == 0:
        return True
    return False
even_numbers = filter(is_even, numbers)
print(list(even_numbers))       # [2, 4]

numbers = [1, 2, 3, 4, 5]  # iterable
def is_odd(num):
    if num % 2 != 0:
        return True
    return False
odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))       # [1, 3, 5]

# Filter long name
names = ['Abhinaya', 'Lidiya', 'Ermias', 'Satoru']  # iterable
def is_name_long(name):
    if len(name) > 7:
        return True
    return False
long_names = filter(is_name_long, names)
print(list(long_names))         # ['Abhinaya']

print()
#------------------------------------------------------------------------------------------------

# reduce()
numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)
total = reduce(add_two_nums, numbers_str)
print(total)    # 15
