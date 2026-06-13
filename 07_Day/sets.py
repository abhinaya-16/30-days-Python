# Sets{} unordered unchangable(existing items, but we can add new items to the set) 
# no duplicate 

# Creating a set
# syntax
st=set()
st = {'item1', 'item2', 'item3', 'item4'}
print(st)
fruits = {'banana', 'orange', 'mango', 'lemon'}
print(fruits)
print()
#-----------------------------------------------------------

#Get length
fruits = {'banana', 'orange', 'mango', 'lemon'}
len(fruits)
print(len(fruits))
print()
#-----------------------------------------------------------

#Checking an item
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits ) # True
print('Does mango belong to the set fruits', 'mango' in fruits)
print()
#-----------------------------------------------------------

# Adding one item to a set
# Adds at any index
# The result is unordered
# add() function is specific to sets
# Lists do not have add() or update().
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')
print(st)
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')
print(fruits)
print()
#-----------------------------------------------------------

# Adding multiple items to a set
# update()
# update() takes a list or tuple argument
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])
print(st)
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
print(fruits)
print()
#-----------------------------------------------------------

# Removing items
#remove() and del
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')
print(st)
#remove() method will raise errors
st.discard('item1')
print(st)
#discard() method doesn't raise any errors
#pop() method removes a random item from a list and it returns the removed item.
fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop() 
print(removed_item)
print(fruits)
print()
#-----------------------------------------------------------

#Clear Items in a set
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits) # set()
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits
print(fruits) # Gives NameError
print()
#-----------------------------------------------------------

#Converting List to Set
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits) 
print(fruits)
# {'mango', 'lemon', 'banana', 'orange'} 
# the order is random, because sets in general are unordered
print()
#-----------------------------------------------------------

#Converting Set to List
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = set(fruits) # {'mango', 'lemon', 'banana', 'orange'}
print(fruits)
print()
#-----------------------------------------------------------

#Joining Sets
# union()
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2) #st3 = st1 | st2
print(st3)

# or using this : print(fruits | vegetables)
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits | vegetables)

#or using update()
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}
print()
#-----------------------------------------------------------

#Finding Intersection or common items
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
res=whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}
print(res)

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python & dragon)     # {'o', 'n'}
# python & dragon
print()
#-----------------------------------------------------------

#Subset and superset
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.issubset(even_numbers)) # False, because it is a super set
print(whole_numbers.issuperset(even_numbers)) # True

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.issubset(dragon)     # False
print()
#-----------------------------------------------------------

#Difference between two sets
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
odd_numbers=whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9}
print(odd_numbers)

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.difference(dragon))   # {'p', 'y', 't'}  - the result is unordered (characteristic of sets)
# python - dragon
print(dragon.difference(python))    # {'d', 'r', 'a', 'g'}
# dragon - python
print()
#-----------------------------------------------------------

# Symmetric Difference Between Two Sets
# Remove common items from both the sets and join
# it means (A-B)∪(B-A)

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
new_set=whole_numbers.symmetric_difference(some_numbers) # {0, 6, 7, 8, 9, 10}
print(new_set)

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
new_set=python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}
print(new_set)
# python ^ dragon
print()
#-----------------------------------------------------------

#Check if disjoint
# Two sets do not have a common item
even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
print(even_numbers.isdisjoint(odd_numbers)) # True, because no common item

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.isdisjoint(dragon)) # False, there are common items {'o', 'n'}
print()
#-----------------------------------------------------------