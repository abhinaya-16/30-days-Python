# Day 2: 30 Days of python programming
# Exercises Level 1 --------------------------------------------------------
first_name='Abhinaya'
last_name='Kondi'
full_name=first_name + ' ' + last_name
country='Canada'
city='Toronto'
age=21
year=2026
is_married=False
is_true=True
is_light_on=False
height, weight=1.65, 55

print('First name: ', first_name)
print('Last name: ', last_name)
print('Full name: ', full_name)
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Year: ', year)
print('Married: ', is_married)
print('Is true: ', is_true)
print('Is light on: ', is_light_on) 
print('Height: ', height)
print('Weight: ', weight)

# Exercises Level 2---------------------------------------------------------
print(type(first_name))   # str
print(type(last_name))    # str
print(type(full_name))    # str     
print(type(country))      # str
print(type(city))         # str
print(type(age))          # int
print(type(year))         # int
print(type(is_married))   # bool
print(type(is_true))      # bool
print(type(is_light_on)) # bool
print(type(height))      # float
print(type(weight))      # float

print(len(first_name))   # 8
print(len(last_name))    # 5
if len(first_name) > len(last_name):
    print('First name is longer than last name')
else:    
    print('Last name is longer than first name')

num_one=5
num_two=4
total=num_one + num_two
diff=num_one - num_two
product=num_one * num_two
division=num_one / num_two # 1.25
remainder=num_one % num_two # modulus operator = 1
exp=num_one ** num_two
floor_division=num_one // num_two # floor division = 1
# Difference between / and // is that / gives us a float value while // gives us an integer value
print('Total: ', total)
print('Difference: ', diff)     
print('Product: ', product)
print('Division: ', division)
print('Remainder: ', remainder)
print('Exponent: ', exp)
print('Floor division: ', floor_division)

radius=30
area_of_circle=3.14 * radius ** 2 # pi r^2 = 2826
circum_of_circle=2 * 3.14 * radius # 2pi r = 188.4
print('Area of circle: ', area_of_circle)
print('Circumference of circle: ', circum_of_circle)

user_radius=int(input('Enter radius: ')) # 30
area_of_circle=3.14 * user_radius ** 2
print('Area of circle with radius', user_radius, 'is', area_of_circle)

user_first_name=input('Enter your first name: ') 
user_last_name=input('Enter your last name: ')  
user_country=input('Enter your country: ')
user_age=int(input('Enter your age: ')) 
print('First name: ', user_first_name)
print('Last name: ', user_last_name)
print('Country: ', user_country)
print('Age: ', user_age)
