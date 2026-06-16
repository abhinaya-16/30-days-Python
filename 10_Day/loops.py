#while loop

count = 0
while count < 5:
    print(count)
    count = count + 1
#prints from 0 to 4
print()
#--------------------------------------------

# syntax
# while condition:
#     code goes here

# run block of code once the condition is no longer true,
# while condition:
#     code goes here
# else:
#     code goes here
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)
# else block executes once and exits
print()
#--------------------------------------------

#for loop on list
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5
print(numbers)
print()
#--------------------------------------------

#for loop in tuple
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
print(numbers)
print()
#--------------------------------------------

#for loop on string 
language = 'Python'
for letter in language:
    print(letter)
# works the same
print()
#--------------------------------------------

for i in range(len(language)):
    print(language[i])
print()
#--------------------------------------------

#for loop in a dictionary
person={
    'first_name': 'Satoru',
    'last_name': 'Gojo',
    'age': 28,
    'country': 'Tokyo',
    'is_married': False,
    'skills': ['Reversal-Red', 'Amplification-Blue', 'Domain Expansion: Infinte Void', 'Hollow Purple', 'Black Flash', 'Teleportation', 'Limitless Technique', 'Infinity', '', 'Reversed Cursed Technique', 'Six eyes', 'Barrier Techniques'],
    'address': {
        'street': 'Roppongi',
        'zipcode': '02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out

print()
#--------------------------------------------

#for loop in sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)
print(it_companies)

# range(start, end, step) takes three parameters: starting, ending and increment.
# By default it starts from 0 and the increment is 1
lst = list(range(11))
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}

# for backward from start to end 
lst = list(range(11,0,-2))
print(lst) # [11,9,7,5,3,1]

for number in range(11):
    print(number)   # prints 0 to 10, not including 11
print()
#--------------------------------------------

#Nested for loop
person={
    'first_name': 'Satoru',
    'last_name': 'Gojo',
    'age': 28,
    'country': 'Tokyo',
    'is_married': False,
    'skills': ['Reversal-Red', 'Amplification-Blue', 'Domain Expansion: Infinte Void', 'Hollow Purple', 'Black Flash', 'Teleportation', 'Limitless Technique', 'Infinity', '', 'Reversed Cursed Technique', 'Six eyes', 'Barrier Techniques'],
    'address': {
        'street': 'Roppongi',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)
print()
#--------------------------------------------

# for else
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)

# The else block executes only if the loop finishes normally (without hitting break).
# Here else does not run
for number in range(11):
    if number == 5:
        break
    print(number)
else:
    print("Loop completed normally")

print("Done")
print()
#--------------------------------------------

#Pass: Placeholder for future statements
for number in range(6):
    pass
print('Code passed')
