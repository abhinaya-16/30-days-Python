a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')

#Short Hand
a = 3
print('A is positive') if a > 0 else print('A is negative') 
# first condition met, 'A is positive' will be printed

#Nested Conditions:
a = 2
if a > 0:
    if a % 2 == 0:
        print('A is a positive even integer')
    else:
        print('A is a positive odd integer')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

#Conditional and Logical Operators
#and
a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')

#or
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')
