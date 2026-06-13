me=28
you=int(input("Enter your age "))

if(me>you):
    diff=me-you
    if diff==1:
        print("You are",diff,"year younger than me")
    else:
        print("You are",diff,"years younger than me")
elif(you>me):
    diff=me-you
    if diff==1:
        print("You are",diff,"year older than me")
    else:
        print("You are",diff,"years older than me")
else:
    print("You are as old as me")
