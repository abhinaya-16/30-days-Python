def is_prime(num):
    count=0
    for i in range(2,num+1):
        if num%i==0:
            count=count+1
    if count==1:
        return True
    else:
        return False
print(is_prime(7))
print(is_prime(9))
print()
#----------------------------------------------

def is_unique(lst):
    for i in lst:
        count=0
        for j in lst:
            if i==j:
                count=count+1
            if count>1:
                return False
    return True
print(is_unique([1,2,3,4,5,6,7,8,9]))
print(is_unique([1,2,3,3,3,3,4,5,6,7,8,9]))  
print()
#----------------------------------------------

def same_type(lst):
    t=type(lst[1])
    for i in lst:
        if(type(i)!=t):
            return False
    return True
print(same_type([1,2,3,4,5]))
print(same_type([1,2,3,4,'a']))
print()
#----------------------------------------------

def is_valid_variable(variable):
    return variable.isidentifier()
print(is_valid_variable("name"))        # True
print(is_valid_variable("first_name"))  # True
print(is_valid_variable("_count"))      # True
print(is_valid_variable("1name"))       # False
print(is_valid_variable("first-name"))  # False
print(is_valid_variable("my variable")) # False
print()
#----------------------------------------------



