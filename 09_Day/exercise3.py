person={
    'first_name': 'Satoru',
    'last_name': 'Gojo',
    'age': 28,
    'country': 'Tokyo',
    'is_married': False,
    'skills': ['Reversal-Red', 'Amplification-Blue', 'Domain Expansion: Infinte Void', 'Hollow Purple', 'Black Flash', 'Teleportation', 'Limitless Technique', 'Infinity', '', 'Reversed Cursed Technique', 'Six eyes', 'Barrier Techniques'],
    'address': {
        'street': 'Roppongi',
        'zipcode': '02210'
    }
}

if('skills' in person):
    length=len(person['skills'])
    lst=person['skills']
    mid=lst[length//2]
    print(mid)
    print('Six eyes' in lst)
    if (person['is_married']==True):
        status='married' 
    else:
        status='not married'
    print(person['first_name'],person['last_name'],'lives in',person['country'],'. He is', status)
    if('Six eyes' in lst and 'Limitless Technique' in lst and 'Hollow Purple' not in lst):
        print('The strongest')
    if('Six eyes' in lst and 'Limitless Technique' in lst and 'Hollow Purple' in lst):
        print('The honored one')
    if('Six eyes' not in lst and 'Limitless Technique' in lst):
        print('Limitless User')