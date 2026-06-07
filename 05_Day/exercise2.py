ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
min=ages[0]
max=ages[len(ages)-1]
print('Minimum age', min)
print('Maximum age', max)
ages.append(min)
ages.append(max)
print(ages)

print()
#--------------------------------------------

ages.sort()
print(ages)
length=len(ages)
if(length%2==1):
    median=ages[int(length/2)]
elif(length%2==0):
    median=int((ages[int(length/2)]+ages[int(length/2)+1])/2)
print('Median',median)

i=0
sum=0
avg=0
length=len(ages)
for i in range(0,length):
    sum=sum+ages[i]
avg=sum/length
print('Average: ',avg)

range=max-min
print('Range: ',range)

min_diff = abs(min - avg)
max_diff = abs(max - avg)

print('Min diff: ',min_diff)  # 20.0
print('Max diff: ',max_diff)  # 20.0


    
