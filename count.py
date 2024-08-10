str=input("enter a string:")
lower=0
upper=0
for i in str:
    if(i.islower()):
        lower+=1
    else:
        upper+=1
print("no of lower case:",lower)
print("no of upper case:",upper)