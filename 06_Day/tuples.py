# Tuple: ordered, unchangeable.  Allows duplicate members.
# Tuples are written with round brackets, ()
# Once a tuple is created, we cannot change its values.

#Creating an empty tuple
# syntax
empty_tuple = ()
# or using the tuple constructor
empty_tuple = tuple()

tpl = ('item1', 'item2','item3')
fruits = ('banana', 'orange', 'mango', 'lemon')
print(tpl)
print(fruits)

tpl = ('item1', 'item2', 'item3')
len(tpl)

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index =len(fruits) - 1
last_fruit = fruits[last_index]
print(first_fruit)
print(second_fruit)
print(last_fruit)
fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]
print(first_fruit)
print(second_fruit)
print(last_fruit)

#Slicing Tuples
fruits = ('banana', 'orange', 'mango', 'lemon')
print(fruits[0:4])    # all items
print(fruits[0:])      # all items
print(fruits[1:3])  # doesn't include item at index 3
print(fruits[1:])

fruits = ('banana', 'orange', 'mango', 'lemon')
print(fruits[-4:])    # all items
print(fruits[-3:-1])  # doesn't include item at index 3 and 0
print(fruits[-3:])

#Checking an Item in a Tuple
fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False
# fruits[0] = 'apple' 
# TypeError: 'tuple' object does not support item assignment

#Joining Tuples
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

# Deleting Tuples
# It is not possible to remove a single item in a tuple 
# but it is possible to delete the tuple itself using del.

fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits
# print(fruits)
# Gives NameError

# ✨ Changing Tuples to List and List to Tuples
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')
