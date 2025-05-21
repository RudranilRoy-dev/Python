letter= '''Dear Name \nYou are selected!\nDate'''

name=input("Enter the Name: ")
date=input("Enter date (dd/mm/yyyy): ")

print(letter.replace("Name",name).replace("Date",date))