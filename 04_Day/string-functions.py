# Built in String functions or methods

# len(): Returns the length of the string
challenge = 'thirty days of python'
print(len(challenge))

#upper(): Uppercase all letters
challenge = 'thirty days of python'
print(challenge.upper())

#lower(): Lowercase all letters
challenge = 'thirty days of python'
print(challenge.lower())

# capitalize(): Converts the first character the string to Capital Letter
challenge = 'thirty days of python'
print(challenge.capitalize())  # 'Thirty days of python'

# title(): Returns a Title Cased String. Capitalizing first letter of each word
challenge = 'thirty days of python'
print(challenge.title())  # Thirty Days Of Python

# count(): returns occurrences of substring in string, count(substring, start, end)
challenge = 'thirty days of python'
print(challenge.count('y'))  # 3
print(challenge.count('y', 7, 14))  # 1
print(challenge.count('th'))  # 2

# endswith(): Checks if a string ends with a specified ending
challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion'))  # False

# expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10))  # 'thirty    days      of        python'

# find(): Returns the index of first occurrence of substring
# find(substring, start-index, stop-index)
# index(substring, start-index, stop-index)
# The main difference is what happens when the substring isn't found.
# find() if not found returns -1
# index() if not found returns ValueError 
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th'))  # 0

# rfind(): Returns the index of the last occurrence of a substring, if not found returns -1
challenge = 'thirty days of python'
print(challenge.rfind('y'))  # 16
print(challenge.rfind('th')) # 17
print(challenge.rfind('y',0,11)) #9
print(challenge.rfind('n'))
print(len(challenge))

# index():  Returns the first occurance of a substring 
# If the substring is not found it raises a ValueError.
challenge = 'thirty days of python'
sub_string = 'da'
ch='y'
print(challenge.index(sub_string))  # 7
print(challenge.index(ch)) #5
print(challenge.index(sub_string, 9)) # error

# rindex(): Returns the index of the last occurrence of a substring
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string))  # 7
print(challenge.rindex(sub_string, 9)) # error
print(challenge.rindex('on', 8)) # 19

# format()	formats string into nicer output
first_name = 'Abhinaya'
last_name = 'Kondi'
job = 'Software Developer'
country = 'Canada'
sentence = 'I am {} {}. I am a {}. I live in {}.'.format(first_name, last_name, job, country)
print(sentence)

radius = 10
pi = 3.14
area = pi  # radius ## 2
result = 'The area of circle with {} is {}'.format(radius, area)
print(result)  # The area of circle with 10 is 314.0

# isalnum(): Checks alphanumeric character
challenge = 'ThirtyDaysPython'
print(challenge.isalnum())  # True

challenge = '30DaysPython'
print(challenge.isalnum())  # True

challenge = 'thirty days of python'
print(challenge.isalnum())  # False, whitespace is not an alphanumeric character

challenge = 'thirty days of python 2019'
print(challenge.isalnum())  # False

# isalpha(): Checks if all characters are alphabets
challenge = 'thirty days of python'
print(challenge.isalpha()) # False, space is once again excluded
challenge = 'ThirtyDaysPython'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False

# isdecimal() ⊆ isdigit() ⊆ isnumeric()
# Anything that is isdecimal() is also isdigit() and isnumeric(), but not vice versa.
# isdecimal() -> Only 0-9
# isdigit()   -> 0-9 + superscripts (², ³, ...)
# isnumeric() -> 0-9 + superscripts (², ³, ...) + fractions (½, ⅓, ...)

# Normal digits
num = '123'
print(num.isdecimal())  # True
print(num.isdigit())    # True
print(num.isnumeric())  # True

# Superscript 2
num = '²'
print(num.isdecimal())  # False # Not a decimal digit
print(num.isdigit())    # True  # Is a digit
print(num.isnumeric())  # True  # Is numeric

# Fraction one-half
num = '½'
print(num.isdecimal())  # False # Not a decimal digit
print(num.isdigit())    # False # Not a digit
print(num.isnumeric())  # True  # Is numeric

# Decimal number as a string
num = '10.5'
print(num.isdecimal())  # False # '.' is not a decimal digit
print(num.isdigit())    # False # '.' is not a digit
print(num.isnumeric())  # False # '.' is not numeric

# isidentifier():Checks for valid identifier means it check if a string is a valid variable name
challenge = '30DaysOfPython'
print(challenge.isidentifier())  # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier())  # True

# islower():Checks if all alphabets in a string are lowercase
challenge = 'thirty days of python'
print(challenge.islower())  # True
challenge = 'Thirty days of python'
print(challenge.islower())  # False

# isupper(): returns if all characters are uppercase characters
challenge = 'thirty days of python'
print(challenge.isupper())  # False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper())  # True

# join(): Returns a concatenated string
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '* '.join(web_tech)
print(result) # 'HTML* CSS* JavaScript* React'

# strip(): Removes both leading and trailing characters
challenge = 'yHello y Worldy'
print(challenge.strip('y')) # Hello y World

# replace(): Replaces substring inside
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding'))  # 'thirty days of coding'

# split():Splits String from Left
challenge = 'thirty days of python'
print(challenge.split()) # takes whitespace as default 
# ['thirty', 'days', 'of', 'python']
challenge = 'thirty* days* of* python'
print(challenge.split('* '))

# swapcase(): Checks if String Starts with the Specified String
challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON

# startswith(): Checks if String Starts with the Specified Strin
challenge = 'thirty days of python'
print(challenge.startswith('thirty'))  # True
challenge = '30 days of python'
print(challenge.startswith('thirty'))  # False