sum=0
for i in range(0,101):
    sum=sum+i
print('The sum of all numbers is', sum)
print()
#------------------------------------------------

print('Even:')
sum_even=0
for i in range(0,101,2):
    sum_even=sum_even+i
print('The sum of all even numbers is', sum_even)
print()
#------------------------------------------------
    
print('Odd:')
sum_odd=0
for i in range(1,101,2):
    sum_odd=sum_odd+i
print('The sum of all odd numbers is', sum_odd)