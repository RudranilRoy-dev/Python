def pattern(n):

    if(n==1):
        print("*"*n)
    else:
        print("*"*n)
        return pattern(n-1)
    
n=int(input("Enter the numebr:"))
pattern(n)