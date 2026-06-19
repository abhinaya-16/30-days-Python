numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
new_numbers_lst=[i for i in numbers if i<=0]
print(new_numbers_lst)
print()
#---------------------------------------------------------

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_lst=[i for row in list_of_lists for i in row]
print(new_lst)
print()
#---------------------------------------------------------

list_of_tuples=[tuple([n] + [n**i for i in range(6)]) for n in range(11)]
print(list_of_tuples)
# Another way to do it
# result = [(n, n**0, n**1, n**2, n**3, n**4, n**5) for n in range(11)]
# print(result)
print()
#---------------------------------------------------------

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
new_countries=[[count.upper(), count[:4].upper(), cap.upper()]for[(count,cap)] in countries]
output=[{'countries':count.upper(),'city':cap.upper()} for[(count,cap)] in countries]
print(new_countries)
print(output)
# output:
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
print()
#---------------------------------------------------------

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
new_names=[st[0]+' '+st[1] for row in names for st in row]
# shorter way
# new_names=[first + ' ' + last for [(first, last)] in names]
print(new_names)
# output
# ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
print()
#---------------------------------------------------------

slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
print(slope(1, 2, 3, 6))

y_intercept = lambda x, y, m: y - m * x
print(y_intercept(2, 5, 1))