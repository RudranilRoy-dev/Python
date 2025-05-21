with open("replace.txt","r") as file:
    content=file.read()

print(content)

oldword=input("Enter the old word:")
newword=input("Enter the new word:")

content=content.replace(oldword,newword)

with open("replace.txt","w") as file:
    file.write(content)