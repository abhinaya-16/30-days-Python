countries=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(countries)

length=len(countries)
mid=int(length/2)
mid_list=[]
if(length%2==1):
    mid_list=countries[mid]
elif(length%2==0):
    mid_list=countries[mid-1:mid+1]
print(mid_list)
print()

countries=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_half=[]
second_half=[]
length=len(countries)
mid=int(length/2)
if (length%2==1):
    first_half=countries[:mid+1]
    second_half=countries[mid+1:]
elif(length%2==0):
    first_half=countries[:mid]
    second_half=countries[mid:]

print(first_half)
print(second_half)
print()

countries=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
C1, C2, C3, *Scandic_C=countries
print(C1)
print(C2)
print(C3)
print(Scandic_C)

