# Input from the user
sentence = input("Enter a sentence: ")
word_to_find = "is"

# Split the sentence into words
words = sentence.split()

# Initialize counters
count = 0
index = 0

# Loop through each word manually tracking index
for word in words:
    if word == word_to_find:
        count += 1
        if count == 3:
            print(f"The third occurrence of '{word_to_find}' is at word position {index}")
            break
    index += 1

# If the word doesn't occur 3 times
if count < 3:
    print(f"The word '{word_to_find}' does not occur 3 times.")
