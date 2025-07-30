# Get input from the user
text = input("Enter a string with leading/trailing spaces: ")

# Remove leading and trailing spaces
words = text.split()
new_text=' '.join(words)
# Print the result
print(f"Modified Text: {new_text} ")
