string1= 'Thirty'+'Days'+'Of'+'Python'
print(string1)
print()
#-----------------------------------------------------

string2= 'Coding'+'For'+'All'
print(string2)
print()
#-----------------------------------------------------

company='Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[0:6])
print()
#-----------------------------------------------------

print('Coding' in company)
print(company.index('Coding'))
print(company.find('Coding'))
res=company.find('Coding')
if(res!=-1):
    print(True)
print()
#-----------------------------------------------------

print(company.replace('Coding','Python'))
print(company.replace('All','Everyone').replace('Coding', 'Python'))
print()
#-----------------------------------------------------

print(company.split(' '))
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(','))
print()
#-----------------------------------------------------

print(company[0])
print(company[-1])
print(company[10])
print()
#-----------------------------------------------------

company = 'Python For Everyone'
text=' '+company
acrn=''
pos=0
while(text.find(' ')!=-1):
    pos=text.find(' ')
    acrn=acrn+text[pos+1]
    text=text[pos+1:]
print(acrn)

company = 'Coding For All'
text=' '+company
acrn=''
pos=0
while(text.find(' ')!=-1):
    pos=text.find(' ')
    acrn=acrn+text[pos+1]
    text=text[pos+1:]
print(acrn)
print()
#-----------------------------------------------------

company = 'Coding For All'
print(company.index('C'))
print(company.index('F'))
print(company.rindex('l'))
print()
#-----------------------------------------------------

sentence='You cannot end a sentence with because because because is a conjunction'
print( sentence.find('because'))
print( sentence.index('because'))
print( sentence.rfind('because'))
print()
#-----------------------------------------------------

print( sentence.replace('because because because ',''))

start = sentence.find('because because because')
end = start + len('because because because')
print(sentence[start:end])
print()
#-----------------------------------------------------

company = 'Coding For All'
print(company.startswith('Coding'))
print(company.endswith('coding'))

print('   Coding For All      '.strip(' '))
print()
#-----------------------------------------------------

print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())
print()
#-----------------------------------------------------

python_lib=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(('# ').join(python_lib))
print()
#-----------------------------------------------------

print('I am enjoying this challenge. \nI just wonder what is next.')
print()
#-----------------------------------------------------

print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')
print()
#-----------------------------------------------------

radius=10
print('radius = {}'.format(radius))
print('area = 3.14 * radius ** 2')
print('The area of a circle with radius {} is {:.0f} meters square.'.format(radius, 3.14 * radius ** 2))
print()
#-----------------------------------------------------

a=8
b=6
print('{} + {} = {}'.format(a,b,a+b))
print('{} - {} = {}'.format(a,b,a-b))
print('{} * {} = {}'.format(a,b,a*b))
print('{} / {} = {:.2f}'.format(a,b,a/b))
print('{} % {} = {}'.format(a,b,a%b))
print('{} // {} = {}'.format(a,b,a//b))
print('{} ** {} = {}'.format(a,b,a**b))