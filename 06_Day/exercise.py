tpl=()
sisters=('Nobara','Tsumiki','Maki')
brothers=('Toge','Yuji','Yuta')
siblings=sisters+brothers
print(siblings)
print('I have ', len(siblings), 'siblings')
family_members = list(siblings)
family_members.extend(['Gojo', 'Utahime'])
print(family_members)

*siblings, father, mother = family_members

print(siblings)
print(father)
print(mother)

fruits=('mango', 'apple','strawberry', 'banana', 'dragon fruit' )
vegetables=('carrots', 'tomatoes', 'potatoes', 'cauliflower', 'broccoli')
animal_products=('milk', 'cheese', 'butter', 'meat', 'yogurt')
food_stuff_tp=fruits+vegetables+animal_products
print(food_stuff_tp)
food_stuff_ls=list(food_stuff_tp)
print(food_stuff_ls)
length=len(food_stuff_tp)
mid_tp=()
if(length%2==0):
    mid=int((length/2)) - 1
    mid_tp=(food_stuff_tp[mid], food_stuff_tp[mid+1])
elif(length%2!=0):
    mid=int((length/2))
    mid_tp=(food_stuff_tp[mid])
print(mid_tp)

print(food_stuff_ls[:3])
print(food_stuff_ls[-3:])

del food_stuff_tp
# print(food_stuff_tp)
# prints error

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)