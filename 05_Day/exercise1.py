lst=list()
print(lst)

print()
#--------------------------------------------

lst=[1,2,3,4,5]
print(lst)
print(len(lst))
print(lst[0])
print(lst[int(len(lst)/2)])
print(lst[len(lst)-1])

print()
#--------------------------------------------

mixed_data_types=['Abi', 21, 1.65, 'Single', '33 Dunfield Ave']
print(mixed_data_types)

print()
#--------------------------------------------

it_companies=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))
print(it_companies[0])
print(it_companies[int(len(it_companies)/2)])
print(it_companies[len(it_companies)-1])
it_companies[2]='Alphabet'
print(it_companies)
it_companies.append('Tesla')
print(it_companies)
it_companies.insert(4,'Netflix')
print(it_companies)
it_companies[0]=it_companies[0].upper()
print(it_companies)
print('#; '.join(it_companies))
print('Google' in it_companies)
print(sorted(it_companies))
it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)
print(it_companies[0:3])
print(it_companies[-3:])
print(it_companies)
mid=int(len(it_companies)/2)
print(it_companies[mid])
it_companies.pop(0)
print(it_companies)
mid=int(len(it_companies)/2)
it_companies.pop(mid)
print(it_companies)
it_companies.pop(len(it_companies)-1)
print(it_companies)
it_companies.clear()
print(it_companies)
del it_companies
# print(it_companies) -> Gives NameError since now the it_companies list doesn't exist

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
print(front_end+back_end)
full_stack=front_end+back_end
full_stack.insert(5,'Python')
full_stack.insert(6,'SQL')
print(full_stack)
print()
#--------------------------------------------
