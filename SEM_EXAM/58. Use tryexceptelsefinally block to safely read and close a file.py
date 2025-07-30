filename = "sample.txt"

try:
    file = open(filename, 'r')  # Try to open the file
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
else:
    content = file.read()       # If no error, read the file
    print("File content:\n", content)
finally:
    try:
        file.close()            # Always try to close the file
        print("File closed successfully.")
    except NameError:
        print("File was never opened, so nothing to close.")
