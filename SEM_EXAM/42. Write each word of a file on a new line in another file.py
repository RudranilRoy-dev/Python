with open("41. file.txt") as input_file:
    text=input_file.read()
    words=text.split()


with open("42. file.txt",'w') as output_file:
    for word in words:
        output_file.write(f"{word}\n")