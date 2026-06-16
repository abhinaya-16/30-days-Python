##With While loop
# Break: We use break when we like to get out of or stop the loop:
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break
print()
#------------------------------------

#Continue: With the continue statement we can skip the current iteration, and continue with the next:
count = 0
while count < 5:
    if count == 3:
        count=count+1
        continue
    print(count)
    count = count + 1
print()
#------------------------------------

## With for loop
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break
print()
#------------------------------------

numbers = (0,1,2,3,4,5)
for number in numbers:
    if number == 3:
        continue
    print(number)
print('outside the loop')

print()
#------------------------------------