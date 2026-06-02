age=21
height=1.75
complex_number=1+2j
print('Age:', age)
print('Height:', height)
print('Complex number:', complex_number)

print()

base=float(input('Enter base: '))
height=float(input('Enter height: '))
print('The area of the triangle is: ', 0.5 * base * height)

print()

a=input('Enter a: ')
b=input('Enter b: ')
c=input('Enter c: ')
print('The perimeter of the triangle is: ', a + b + c)

print()

length=float(input('Enter length: '))
width=float(input('Enter width: '))
print('The area of the rectangle is: ', length * width)
print('The perimeter of the rectangle is: ', 2 * (length + width))

print()

radius=float(input('Enter radius: '))
print('The area of the circle is: ', 3.14 * radius ** 2)
print('The circumference of the circle is: ', 2 * 3.14 * radius)

print()

# Equation: y = 2x - 2
slope_a = 2
# x-intercept: set y = 0
x_intercept = (0 + 2) / 2
# y-intercept: set x = 0
y_intercept = 2 * 0 - 2

print("Slope:", slope_a)
print("x-intercept:", x_intercept)
print("y-intercept:", y_intercept)

print()

# Slope between point (2, 2) and point (6,10)
# Slope formula: m = (y2 - y1) / (x2 - x1)
x1, y1 = 2, 2
x2, y2 = 6, 10
slope_b = (y2 - y1) / (x2 - x1)
print("Slope between points (2, 2) and (6, 10):", slope_b)
# Euclidean distance between point (2, 2) and point (6,10)
# Distance formula: d = sqrt((x2 - x1)^2 + (y2 - y1)^2)
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("Distance between points (2, 2) and (6, 10):", distance)

if(slope_a > slope_b):
    print("Slope of the line y = 2x - 2 is greater")
elif(slope_a < slope_b):
    print("Slope of the line between points (2, 2) and (6, 10) is greater.")

print()

# y (y = x^2 + 6x + 9)
# y=0
# x^2 + 6x + 9 = 0
a = 1.0
b = 6.0
c = 9.0
x1 = (-b + (b**2 - 4*a*c) ** 0.5) / (2*a)
x2 = (-b - (b**2 - 4*a*c) ** 0.5) / (2*a)

print(x1)
print(x2)

for x in range(-10, 11):
    y = x**2 + 6*x + 9
    if y == 0:
        print("x =", x)

print()

print(len('python') > len('dragon'))
print()

print('on' in 'python' and 'on' in 'dragon')
print()

print('jargon' in 'I hope this course is not full of jargon')
print()

print('on' not in 'python' and 'on' not in 'dragon')
print()

print(str(float(len('python'))))
print()

num=int(input('Enter a number: '))
if (num % 2 == 0):
    print(num, 'is an even number.')
else:
    print(num, 'is an odd number.')
print()

res=7//3 #result is 2
if (res == int(2.7)):
    print(res)
print()

print(type('10') == type(10)) # False, because '10' is a string and 10 is an integer
print()

# print(int('9.8')) -> This will raise a ValueError since '9.8' is not a valid integer string.
# print (int('9.8') == 10) 
# False, because int('9.8') 
# It will raise a ValueError since '9.8' is not a valid integer string

hours = float(input('Enter hours: '))
rph = float(input('Enter rate per hour: '))
print('Your weekly charge is:', hours * rph)
print()

years=int(input('Enter number of years you have lived:'))
seconds= years * 365 * 24 * 60 * 60
print('You have lived for', seconds, 'seconds.')
print()

for i in range(1,6):
    print(i, end=' ')
    for j in range(0,4):
        print(i**j, end=' ')
    print()
print()
