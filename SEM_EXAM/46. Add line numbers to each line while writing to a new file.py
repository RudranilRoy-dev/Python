with open ("41. file.txt",'r') as input_file:
    lines=input_file.readlines()

with open("46. file.txt",'w') as output_file:
    i=1
    for line in lines:
        output_file.write(f"{i}: {line}")
        i+=1