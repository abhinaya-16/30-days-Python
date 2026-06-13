fruit=input("Enter a fruit ")
fruits = ['banana', 'orange', 'mango', 'lemon']
if(fruit.lower() in fruits):
    print("That fruit already exist in the list")
else:
    fruits.append(fruit.lower())
    print("Fruit added:", fruits)