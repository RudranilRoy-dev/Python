p1="Make a lot of money"
p2="buy now"
p3="subcribe this"
p4="click this"

msg=input("Enter Massege: ")

if((p1 in msg)or(p2 in msg)or(p3 in msg)or(p4 in msg)):
    print("This is a spam.")
else:
    print("this is NOT a spam.")