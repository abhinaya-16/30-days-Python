for i in range(11):
    print(i)

i=0
while i<=10:
    print(i)
    i=i+1

print()
#------------------------------------
for i in range(10,-1,-1):
    print(i)

i=10
while i>=0:
    print(i)
    i=i-1

print()
#------------------------------------

x='#'
for i in range(7):
    for j in range(i):
        print(x,end='')
    print()

print()
#------------------------------------

x='# '
for i in range(8):
    for j in range(8):
        print(x,end='')
    print()

print()
#------------------------------------

for i in range(11):
    product=i*i
    print(i,'x',i,'=',product)
print()
#------------------------------------

lst=['Python', 'Numpy','Pandas','Django', 'Flask']
for i in lst:
    print(i)
print()
#------------------------------------

print('Even:')
for i in range(0,11,2):
    print(i) #even
    
print('Odd:')
for i in range(1,11,2):
    print(i) #odd
    
