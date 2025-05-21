file=open("file.txt")
text=file.read()

if("twinkle" in text):
    print("This file contains twinkle word.")
else:
    print("This file NOT contains twinkle word.")