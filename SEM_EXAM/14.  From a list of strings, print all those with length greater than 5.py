# Step 1: Predefined list of strings
words = ["apple", "banana", "cherry", "kiwi", "mango", "pineapple"]

# Step 2: Loop through the list and check length
print("Words with length greater than 5:")
for word in words:
    if len(word) > 5:
        print(word)
