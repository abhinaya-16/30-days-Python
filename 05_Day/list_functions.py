# Adding Items to list

# syntax
lst = list()
lst.append('item')
print(lst)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']
print(fruits)

print()
#--------------------------------------------------------------------------------

# Inserting Items into a List
# At a specific position

# syntax
lst = ['item1', 'item2']
lst.insert(1, 'item*')
print(lst)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # insert apple between orange and mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
print(fruits)

print()
#--------------------------------------------------------------------------------

#Removing Items from a List

#remove() function only removes one item
# syntax
lst = ['item1', 'item2']
lst.remove('item1')
print(lst)

fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon', 'banana'] - this method removes the first occurrence of the item in the list
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango', 'banana']

print()
#--------------------------------------------------------------------------------

#Removing Items Using Pop
#The pop() method removes the specified index, (or the last item if index is not specified):
# pop() method removes one item at a time
# syntax
lst = ['item1', 'item2', 'item3']
lst.pop()    # last item
print(lst)   
lst.pop(0)
print(lst)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)       # ['banana', 'orange', 'mango']
fruits.pop(0)
print(fruits)       # ['orange', 'mango']

print()
#--------------------------------------------------------------------------------

#Removing Items using Del
#Delete items at index
#Delete items within index range 
#Deletes complete list

#syntax
lst = ['item1', 'item2']
del lst[1] # only a single item
print(lst)
del lst        # to delete the list completely
# on printing list now gives error

fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)       # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[1]
print(fruits)       # ['orange', 'lemon', 'kiwi', 'lime']
del fruits[1:3]     # this deletes items between given indexes, so it does not delete the item with index 3!
print(fruits)       # ['orange', 'lime']
del fruits
print(fruits)       # This should give: NameError: name 'fruits' is not defined

print()
#--------------------------------------------------------------------------------

#Clearing List Items
# syntax
lst = ['item1', 'item2']
lst.clear()
print(lst)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)       # []

print()
#--------------------------------------------------------------------------------

#Copying a List
#list2=list1 would point to the same memory box
#This creates a new copy without altering the original

# syntax
lst = ['item1', 'item2']
lst_copy = lst.copy()
print(lst_copy)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy.append('apple')) # ['banana', 'orange', 'mango', 'lemon', 'apple']
print(fruits)                      # ['banana', 'orange', 'mango', 'lemon']

print()
#--------------------------------------------------------------------------------

#Counting Items in a List
# syntax
lst = ['item1', 'item2','item2']
print(lst.count('item2'))

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3

print()
#--------------------------------------------------------------------------------

#Finding Index of an Item
# syntax
lst = ['item1', 'item2']
print(lst.index('item1'))

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))           # 2, the first occurrence

print()
#--------------------------------------------------------------------------------

#Reversing a List
# syntax
lst = ['item1', 'item2']
lst.reverse()
print(lst)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits) # ['lemon', 'mango', 'orange', 'banana']
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages) # [24, 25, 24, 26, 25, 24, 19, 22]

#Also without using the function and using slicing
reverse_fruits = fruits[::-1]

print()
#--------------------------------------------------------------------------------

#Sorting List Items
# syntax

#➡️sort(): this method modifies the original list
lst = ['item1', 'item2']
lst.sort()                # ascending
print(lst)
lst.sort(reverse=True)    # descending
print(lst)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)             # sorted in alphabetical order, ['banana', 'lemon', 'mango', 'orange']
fruits.sort(reverse=True)
print(fruits) # ['orange', 'mango', 'lemon', 'banana']

ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages) #  [19, 22, 24, 24, 24, 25, 25, 26]
ages.sort(reverse=True)
print(ages) #  [26, 25, 25, 24, 24, 24, 22, 19]


#➡️ sorted(): returns the ordered list without modifying the original list
fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))   # ['banana', 'lemon', 'mango', 'orange']
# Reverse order
fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits,reverse=True))
print(fruits)     #remins original without being altered

print()
#--------------------------------------------------------------------------------

#Joining List using Plus Operator(+)
# syntax
list1=['item1','item2']
list2=['item3']
list3 = list1 + list2
print(list3)

positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables ) # ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']

print()
#--------------------------------------------------------------------------------

#Extend Lists using the extend() function
# Alters the list being extended

# syntax
list1 = ['item1', 'item2']
list2 = ['item3', 'item4', 'item5']
list1.extend(list2) # ['item1', 'item2', 'item3', 'item4', 'item5']
print(list1)

num1 = [0, 1, 2, 3]
num2= [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1) # Numbers: [0, 1, 2, 3, 4, 5, 6]

negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]
negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers) # Integers: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits ) # Fruits and vegetables: ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']

print()
#--------------------------------------------------------------------------------

# Add all the values in a list
numbers = [10, 20, 30, 40]
total = sum(numbers)

print(total)  # Output: 100

