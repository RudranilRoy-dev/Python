s1=int(input("Enter the marks of subject 1: "))
s2=int(input("Enter the marks of subject 2: "))
s3=int(input("Enter the marks of subject 3: "))

average=(s1+s2+s3)/3.0

if (average>=40 and s1>=33 and s2>=33 and s3>=33):
    print("Student is pass:",average)
else:
    print("Student is fail:",average)