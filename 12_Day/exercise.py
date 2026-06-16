# Exercise 1:
from random import choice, randint, shuffle
import string

def random_user_id():
    chars = string.ascii_lowercase + string.digits
    #abcdefghijklmnopqrstuvwxyz0123456789
    result = ''
    for _ in range(6):
        result += choice(chars)
        #picks one random character from chars
    # x=6
    # while x>0:
    #     result += choice(chars)
    #     x=x-1
    return result
print(random_user_id())
print()
#---------------------------------------------------------

def user_id_gen_by_user():
    no_of_char=int(input("Enter the number of characters "))
    no_of_IDs=int(input("Enter the number of IDs "))
    chars = string.ascii_lowercase + string.digits
    #abcdefghijklmnopqrstuvwxyz0123456789
    while no_of_IDs>0:
        result=''
        for _ in range(no_of_char):
            result =  result + choice(chars)
            #picks one random character from chars
        print(result)
        no_of_IDs=no_of_IDs-1
user_id_gen_by_user()
print()
#---------------------------------------------------------

def rgb_color_gen():
    r=randint(0,255)
    b=randint(0,255)
    g=randint(0,255)
    st="rgb("+str(r)+","+str(b)+","+str(g)+")"
    return st
print(rgb_color_gen())
print()
#---------------------------------------------------------

#Exercise 2:
def list_of_hexa_colors(num):
    lst=[]
    alphabet= string.ascii_lowercase
    chars = alphabet[0:6] + string.digits
    #abcdef0123456789
    while num>0:
        result=''
        for _ in range(6):
            result = result+choice(chars)
            #picks one random character from chars
        lst.append("#"+result)
        num=num-1
    return lst
print(list_of_hexa_colors(5))
print()
#---------------------------------------------------------

def list_of_rgb_colors(num):
    lst=[]
    for _ in range(num):
        lst.append(rgb_color_gen())
    return lst
print(list_of_rgb_colors(3))
print()
#---------------------------------------------------------

def generate_colors(t,num):
    if(t=='hexa'):
        return list_of_hexa_colors(num)
    elif(t=='rgb'):
        return list_of_rgb_colors(num)
    else:
        return "Invalid argument"
print(generate_colors('hexa', 3)) # ['#a3e12f','#03ed55','#eb3d2b'] 
print(generate_colors('hexa', 1)) # ['#b334ef']
print(generate_colors('rgb', 3))  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
print(generate_colors('rgb', 1))  # ['rgb(33,79, 176)']
print()
#---------------------------------------------------------

# Exercise 3
# Returns a shuffled list
def shuffle_list(lst):
    shuffle(lst)
    return lst
print(shuffle_list([1,2,3,4,5,6,7,8,9]))

def unique_array():
    lst=[]
    while len(lst)<=6:
        num=randint(0,9)
        if num not in lst:
            lst.append(num)
    return lst
print(unique_array())

