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