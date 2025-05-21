def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c

a=int(input("Enter the 1st Number:"))
b=int(input("Enter the 2nd Number:"))
c=int(input("Enter the 3rd Number:"))
print(f"{greatest(a,b,c)} is the greatest")