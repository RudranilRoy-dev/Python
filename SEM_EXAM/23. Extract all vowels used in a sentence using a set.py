# Input sentence
sentence = "PYTHON is An Amazing Programming Language"

# Define the set of vowels
vowels = {'a', 'e', 'i', 'o', 'u'}

# Create an empty set to store the vowels used
used_vowels = set()

# Loop through each character in the sentence
for char in sentence:
    # Convert the character to lowercase
    lower_char = char.lower()
    
    # Check if it is a vowel
    if lower_char in vowels:
        # Add it to the set
        used_vowels.add(lower_char)

# Print the result
print("Vowels used in the sentence:", used_vowels)
