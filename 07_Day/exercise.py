# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Exercise: Level 1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)
it_companies.update(['Netflix', 'Nvidia', 'Tesla'])
print(it_companies)
it_companies.remove('Facebook')
print(it_companies)

#Exercise: Level 2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.union(B))
print(B.union(A))
print(A.symmetric_difference(B))
del A
del B

#Exercise: Level 3
age = [22, 19, 24, 25, 26, 24, 25, 24]
age_st=set(age)
length_age=len(age)
length_age_st=len(age_st)
print('Comparing length of list and set',length_age-length_age_st)

sentence='I am a teacher and I love to inspire and teach people.'
lst=sentence.split()
st=set(lst)
print(st)
