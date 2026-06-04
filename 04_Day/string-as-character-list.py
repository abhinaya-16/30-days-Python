# Strings as Character Lists (or a list of characters)
# Unpacking Characters
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n

print()
#----------------------------------------------------------------

# Accessing Characters in Strings by Index
language = 'Python'
print('first_letter:', language[0]) # P
print('second_letter:', language[1]) # y
last_index = len(language) - 1
print('last_letter:', language[last_index]) # n

#If we want to start from right end we can use negative indexing. -1 is the last index
print('last_letter:', language[-1]) # n
print('second_last:', language[-2]) # o

print()
#----------------------------------------------------------------

# Slicing Python Strings
language = 'Python'

first_three = language[0:3] # starts at zero index and up to 3 but not include 3
print(first_three) #Pyt

last_three = language[3:6]
print(last_three) # hon

# Another way
last_three = language[-3:]
print(last_three)   # hon

last_three = language[3:]
print(last_three)   # hon

print()
#----------------------------------------------------------------

# Reversing a String
# string[start:stop:step]
# When the step is negative, Python moves backwards through the string.
greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH
print(greeting[-3::-1]) #lroW ,olleH
print(greeting[-2:3:-1]) #dlroW ,o
print(greeting[::2])       # Hlo ol!
print(greeting[::-2])      # !lo ole
print(greeting[-5:])       # orld!
print(greeting[:-1])       # Hello, World
print(greeting[:5])        # Hello
print(greeting[11:6:-1])   # dlroW
print()
#----------------------------------------------------------------

# Skipping Characters While Slicing
language = 'Python'
pto = language[0:6:2] #
print(pto) # Pto
# negative slicing has been mentioned above
print()
#----------------------------------------------------------------