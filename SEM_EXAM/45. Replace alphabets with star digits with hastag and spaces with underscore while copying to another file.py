with open("41. file.txt",'r') as input_file:
    text=input_file.read()
    modified_text=""
    for char in text:
        if char.isalpha():
            modified_text+="*"
        elif char.isdigit():
            modified_text+="#"
        elif char.isspace():
            modified_text+="_"
        else:
            modified_text+=char
with open("45. file.txt",'w') as output_file:
    output_file.write(modified_text)
        