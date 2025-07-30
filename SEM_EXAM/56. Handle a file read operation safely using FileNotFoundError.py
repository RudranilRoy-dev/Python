filename = "sample.txt"

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("File content:\n", content)

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
