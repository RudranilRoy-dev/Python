# Open source file for reading
with open("41. file.txt", "r") as input_file:
    lines = input_file.readlines()

# Open destination file for writing
with open("43. file.txt", "w") as output_file:
    for line in lines:
        title_line = line.title()       # Convert to title case
        output_file.write(title_line)   # Write to new file
