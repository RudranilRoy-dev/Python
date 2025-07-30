name = input("Enter a name: ")
char=input("Enter the single character: ")
name=name.lower()
count=0
for ch in name:
    if ch==char:
        count+=1
print(f"{char} occurs {count} times.")