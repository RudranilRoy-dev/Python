def prime(n):
    if n<=1:
        return False
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    return count==2

num=int(input("Enter a Number: "))
if prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")