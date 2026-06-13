# Quick recall: {} curly braces are unordered (meaning no index however dictionaries have key)
# A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.

# Creating
# syntax
empty_dict = {}
empty_dict = dict()
# Dictionary with data values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

# Example:
person = {
    'first_name':'Abi',
    'last_name':'Kenndey',
    'age':250,
    'country':'Canada',
    'is_married':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
print(person)
# value could be any data types:string, boolean, list, tuple, set or a dictionary.

#Dictionary Length:
person = {
    'first_name':'Abi',
    'last_name':'Kenndey',
    'age':250,
    'country':'Canada',
    'is_married':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(len(person)) # 7

#Accessing dictionery items:
# Key does not exist -> return error
person = {
    'first_name':'Abi',
    'last_name':'Kenndey',
    'age':250,
    'country':'Canada',
    'is_married':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(person['first_name']) # Abi
print(person['country'])    # Canada
print(person['skills'])     # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0])  # JavaScript
print(person['address']['street']) # Space street
print(person['city'])       # Error

# get() method for accessing dictionery items:
# Key does not exist -> return None
person = {
    'first_name':'Abi',
    'last_name':'Kenndey',
    'age':250,
    'country':'Canada',
    'is_married':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(person.get('first_name')) # Abi
print(person.get('country'))    # Canada
print(person.get('skills')) #['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('city'))   # None

#Adding items to a dictionery
person = {
    'first_name':'Abi',
    'last_name':'Kenndey',
    'age':250,
    'country':'Canada',
    'is_married':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
        }
}
person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)

#Modifying
person = {
    'first_name':'Abi',
    'last_name':'Kenndey',
    'age':250,
    'country':'Canada',
    'is_married':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
person['first_name'] = 'Satoru'
person['age'] = 252
print(person)

#Is X key in the dictionary?
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct) # True
print('key5' in dct) # False

# Removing key and value pairs:
# pop(key)
# popitem()
# del dct[key]
person = {
    'first_name':'Abi',
    'last_name':'Kenndey',
    'age':250,
    'country':'Canada',
    'is_married':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
person.pop('first_name')        # Removes the firstname item
# Imp: pop() for dictionary requires atleast one argument
# however pop() for list without an argument removes the last item

person.popitem()                # Removes # removes the last item address
del person['is_married']        # Removes the is_married item
print(person)

#clear()
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear()) # None

# del
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct
print(dct) # error

#copy()
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() 

#items() method changes dictionary to a list of tuples.
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) 
# dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])

#keys()
# gives us all the keys of a a dictionary as a list.
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)     
# dict_keys(['key1', 'key2', 'key3', 'key4'])

#values()
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)     
# dict_values(['value1', 'value2', 'value3', 'value4'])
