def fact(a):
    if(a==0 or a==1):
        return(1)
    else:
        return(a*fact(a-1))
a=int(input("enter the number to find factorial:-"))
b=fact(a)
print("factorial is:-",b)