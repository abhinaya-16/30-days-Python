from functools import reduce
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Abhinaya', 'Lidiya', 'Ermias', 'Satoru']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Built-in higher order functions take function and an iterable
def upper_case(country):
    return country.upper()
result=map(upper_case,countries)
print(list(result))

def upper_case(name):
    return name.upper()
result=map(upper_case,names)
print(list(result))

def square(num):
    return num*num
result=map(square,numbers)
print(list(result))

def filter_land(country):
    if 'land' in country:
        return True
    else:
        return False
result=filter(filter_land,countries)
print(list(result))

def six(country):
    if len(country)>=6:
        return True
    else:
        return False
result=filter(six,countries)
print(list(result))

def starting_e(country):
    if country[0]=='E':
        return True
    else:
        return False
result=filter(starting_e,countries)
print(list(result))

result = reduce(
    lambda acc, x: acc + x,
    filter(
        lambda x: x > 5,
        map(lambda x: x * 2, numbers)
    )
)
print(result)

def get_string_lists(lst):
    new_lst=[]
    for item in lst:
        if(type(item)==str):
            new_lst.append(item)
    return new_lst
print(get_string_lists([1,2,'Megumi','3',4,5,'Gojo']))

def sum(num1,num2):
    return num1+num2
total = reduce(sum, numbers)
print(total) 

def concatenate(country1,country2):
    return country1+','+country2
sentence = reduce(concatenate, countries)
print(sentence)             

 

