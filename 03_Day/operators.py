#Boolean
print(True)
print(False)

#Assignment Operators
x = 5
print(x) # 5

x += 3 # x = x + 3
print(x) # 8

x -= 2 # x = x - 2
print(x) # 6

x *= 4 # x = x * 4  
print(x) # 24

x /= 6 # x = x / 6
print(x) # 4.0

x %= 3 # x = x % 3
print(x) # 1.0

x //= 1 # x = x // 1
print(x) # 1.0

x **= 2 # x = x ** 2
print(x) # 1.0

x=5
x&= 2 # x = x & 2
print(x) # 0

x|= 2 # x = x | 2
print(x) # 2

x^= 2 # x = x ^ 2
print(x) # 0

x>>= 2 # x = x >> 2
print(x) # 0

x<<= 2 # x = x << 2
print(x) # 0

print()
#------------------------------------------------

#Arithmetic Operators
# Integers
#
print('Addition: ', 1 + 2)        # 3
print('Subtraction: ', 2 - 1)     # 1
print('Multiplication: ', 2 * 3)  # 6
print ('Division: ', 4 / 2)       # 2.0  Division in Python gives floating number
print('Division: ', 6 / 2)        # 3.0         
print('Division: ', 7 / 2)        # 3.5
print('Division without the remainder: ', 7 // 2)   # 3,  gives without the floating number or without the remaining
print ('Division without the remainder: ',7 // 3)   # 2
print('Modulus: ', 3 % 2)         # 1, Gives the remainder
print('Exponentiation: ', 2 ** 3) # 8 it means 2 * 2 * 2

print()

#Arithetic Operators using variables
a = 3 
b = 2 

total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

print(total) 
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

print()

# Floating numbers
print('Floating Point Number-> PI:', 3.14)
print('Floating Point Number-> gravity:', 9.81)

# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j))

print()

# Calculating formula using operators
# Calculating area of a circle
radius = 10                                 
area_of_circle = 3.14 * radius ** 2         
print('Area of a circle:', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')                         
# Adding unit to the weight

# Calculate the density of a liquid
mass = 75 
volume = 0.075 
density = mass / volume 
print(density, 'Kg/m^3') 
# Adding unit to the density

print()
#------------------------------------------------

#Comparison Operators
print(3 > 2)     # True 
print(3 >= 2)    # True
print(3 < 2)     # False
print(2 < 3)     # True
print(2 <= 3)    # True 
print(3 == 2)    # False
print(3 != 2)    # True
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)

print()

# is, is not, in, not in

print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B not in Asabeneh', 'B' in 'Asabeneh') # False - there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

# difference between == and is 
# is checks the exact same object in memory, while == checks if the values are the same.
# == → "Do these boxes contain the same stuff?"
# is → "Are these literally the same box?"
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True
print(a is b)  # False

x = 5
y = 5

print(x is y)  # True
# In Python, small integers (from -5 to 256) are cached and reused, 
# so x and y point to the same memory location. 
# However, for larger integers or other objects, this may not be the case.

print()
#------------------------------------------------

#Logical Operators
# and, or, not
print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False
