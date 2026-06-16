def add_two_numbers(a,b):
    return a+b
print(add_two_numbers(5,10))
print()
#---------------------------------------------------------------

def area_circle(r):
    return 3.14*r*r
print(area_circle(7))

print()
#---------------------------------------------------------------

def add_all_nums(*para):
    sum=0
    for i in para:
        if(type(i)!=int):
            return 'Invalid argument'
        sum=sum+i
    return sum
print(add_all_nums(2,7,9,5,6,4))
print(add_all_nums(2,7,9,5,6,'a'))

print()
#---------------------------------------------------------------

def  convert_celsius_to_fahrenheit(celsius):
    return (celsius*(9/5))+32
print(convert_celsius_to_fahrenheit(40))

print()
#---------------------------------------------------------------

def check_season(month):
    Autumn=['september', 'october', 'november']
    Winter=['december', 'january', 'february']
    Spring=['march', 'april', 'may']
    Summer=['june', 'july', 'august']
    if(month.lower() in Autumn):
        return('Season is Autumn')
    elif(month.lower() in Winter):
        return('Season is Winter')
    elif(month.lower() in Spring):
        return('Season is Spring')
    elif(month.lower() in Summer):
        return('Season is Summer')
print(check_season('July'))

print()
#---------------------------------------------------------------

def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)
slope = calculate_slope(2, 3, 6, 11)
print(slope)
print()
#---------------------------------------------------------------

def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        # Two distinct real solutions
        x1 = (-b + (discriminant)**(1/2)) / (2 * a)
        x2 = (-b - (discriminant)**(1/2)) / (2 * a)
        return (x1, x2)
    elif discriminant == 0:
        # One repeated real solution
        x = -b / (2 * a)
        return (x,)
    else:
        # No real solutions
        return "No real solutions"
print(solve_quadratic_eqn(1, -5, 6))
print(solve_quadratic_eqn(1, -2, 1))
print()
#---------------------------------------------------------------

def print_list(lst):
    for i in lst:
        print(i)
print_list([1,2,3,4,5,6,7,8,9])
print()
#---------------------------------------------------------------

def reverse_list(lst):
    return lst[::-1]
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"])) 
# ["C", "B", "A"]
print()
#---------------------------------------------------------------

def capitalize_list_items(lst):
    for i in lst:
        print(i.upper())
capitalize_list_items(['Gojo','Megumi','Tsumiki','Yuji','Nobara'])
print()
#---------------------------------------------------------------

def add_item(lst,item):
    lst.append(item)
    return lst
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_stuff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      # [2, 3, 7, 9, 5]
print()
#---------------------------------------------------------------

def remove_item(lst,item):
    lst.remove(item)
    return lst
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]
print()
#---------------------------------------------------------------

def sum_of_numbers(n):
    sum=0
    for i in range(0,n+1):
        sum=sum+i
    return sum
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
print()
#---------------------------------------------------------------

def sum_of_odds(n):
    sum=0
    for i in range(1,n+1,2):
        sum=sum+i
    return sum
print(sum_of_odds(5))  # 15
print(sum_of_odds(10)) # 55
print(sum_of_odds(100)) # 5050
print()
#---------------------------------------------------------------

def sum_of_evens(n):
    sum=0
    for i in range(0,n+1,2):
        sum=sum+i
    return sum
print(sum_of_evens(5))  # 15
print(sum_of_evens(10)) # 55
print(sum_of_evens(100)) # 5050
print()


