n=int(input("Enter the Number:"))
j=1
while(n>0):
    print(" "*(n-1),end="")
    print("*"*j)
    n-=1
    j+=2