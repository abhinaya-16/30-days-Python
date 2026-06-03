# Any data under single, double or triple quote are strings
letter = 'P'                # A string could be a single character or a bunch of texts
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # String could be made using a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "I hope you are enjoying 30 days of Python Challenge"
print(sentence)

print()
#------------------------------------------------
# Multiline string in python
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)

print()

# Another way of doing the same thing
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)
print()
#------------------------------------------------

#Concatenating strings
first_name = 'Abhinaya'
last_name = 'Kondi'
space = ' '
full_name = first_name  + space + last_name
print(full_name) # Abhinaya Kondi
# Checking the length of a string using len() built-in function
print(len(first_name))  # 8
print(len(last_name))   # 5
print(len(first_name) > len(last_name)) # True
print(len(full_name)) # 14

print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
print('Days\tTopics\tExercises') # adding tab space or 4 spaces
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote

# output
# I hope every one is enjoying the Python Challenge.
# Are you ?
# Days  Topics  Exercises
# Day 1	5	    5
# Day 2	6	    20
# Day 3	5	    23
# Day 4	1	    35
# This is a backslash  symbol (\)
# In every programming language it starts with "Hello, World!"

print()
#------------------------------------------------

# String formatting
# % Operator (Old formatting)
# "argument specifiers", special symbols like "%s", "%d", "%f", "%.number of digitsf".
# Strings only
first_name = 'Abhinaya'
last_name = 'Kondi'
language = 'Python'
formated_string = 'I am %s %s. I learn %s' %(first_name, last_name, language)
print(formated_string)

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area) # 2 refers the 2 significant digits after the point
print(formated_string) # The area of circle with a radius 10 is 314.00.

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
formated_string = 'The following are python libraries:%s' % (python_libraries)
print(formated_string) # "The following are python libraries:['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']"

print()
#------------------------------------------------

# str.format
first_name = 'Abhinaya'
last_name = 'Kondi'
language = 'Python'
print('I am {} {}. I learn {}'.format(first_name, last_name, language))
print('I am {first} {last}. I learn {lang}'.format(first=first_name, last=last_name, lang=language))
print('I am {1} {0}. I learn {2}'.format(first_name, last_name, language))

a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal
print(formated_string)

print()
#------------------------------------------------

# String interpolation (f-string) (New formatting)
# f-string
first_name = 'Abhinaya'
last_name = 'Kondi' 
language = 'Python'
print(f'I am {first_name} {last_name}. I learn {language}')

a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

print()
#------------------------------------------------

# General formatting
first_name = 'Abhinaya'
last_name = 'Kondi'
language = 'Python'
print('I am', first_name, last_name, '. I learn', language)
# This is a simple way to format strings in Python

print()
#------------------------------------------------
