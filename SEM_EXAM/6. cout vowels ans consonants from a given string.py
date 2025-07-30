# Input from the user
text = input("Enter a string: ")

# Initialize counters
vowel_count = 0
consonant_count = 0

# Define vowels
vowels = "aeiouAEIOU"

# Loop through each character
for char in text:
    if char.isalpha():  # Check if it's a letter
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

# Display results
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
