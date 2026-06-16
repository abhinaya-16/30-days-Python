import math
def evens_and_odds(n):
    count_even=0
    count_odd=0
    for i in range(0,n+1):
        if(i%2==0):
            count_even+=1
        if(i%2!=0):
            count_odd+=1
    print('The number of odds are', count_odd)
    print('The number of evens are', count_even)
evens_and_odds(100)
# The number of odds are 50.
# The number of evens are 51.
print()
#----------------------------------------------------------

def factorial(num):
    pro=1
    for i in range(1,num+1):
        pro=pro*i
    return pro
print(factorial(5))
print()
#----------------------------------------------------------

def is_empty(item):
    if item:
        return False
    return True
print()
#----------------------------------------------------------

def calculate_mean(lst):
    length=len(lst)
    summation=sum(lst)
    return summation/length
print(calculate_mean([1,2,3,4,5,6,7,8,9]))

def calculate_median(lst):
    lst.sort()
    length=len(lst)
    if(length%2==1):
        median=lst[int(length/2)]
    elif(length%2==0):
        median=int((lst[int(length/2)]+lst[int(length/2)+1])/2)
    return median
print(calculate_median([1,2,3,4,5,6,7,8,9]))

def calculate_mode (lst):
    max=0
    mode=''
    for i in lst:
        count=0
        for j in lst:
            if i==j:
                count=count+1
        if count>max:
            max=count
            mode=i
    return mode
print(calculate_mode([1,2,3,3,3,3,4,5,6,7,8,9]))    

def calculate_range (lst):
    maximum=max(lst)
    minimum=min(lst)
    return maximum-minimum
print(calculate_range([1,2,3,4,5,6,7,8,9])) 

# variance = ∑((xi​−μ)^2)/N
# where xi is each item
# μ is mean of the list
# N is number of items

def calculate_variance(lst):
    length = len(lst)
    mean = calculate_mean(lst)

    squared_differences = 0
    for i in lst:
        squared_differences = squared_differences + ((i - mean) ** 2)
    variance = squared_differences / length
    return variance
print(calculate_variance([1, 2, 3, 4, 5, 6, 7, 8, 9]))
        
# std is standard deviation = sqrt(variance)
def calculate_std (lst):
    variance = calculate_variance(lst)
    return math.sqrt(variance)
print(calculate_std([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print()
#----------------------------------------------------------

def greet(name= 'Guest'):
    print('Hello,',name,'!')
greet()
# "Hello, Guest!
greet("Alice")
# "Hello, Alice!"
print()
#----------------------------------------------------------

def show_args(**kwargs):
    print("Received:", end=" ")
    items = []
    for key, value in kwargs.items():
        items.append(f"{'key'}: {value}")
    print(", ".join(items))
show_args(name="Alice", age=30, city="New York")
show_args(name="Bob", pet="Fluffy, the bunny")
    


    