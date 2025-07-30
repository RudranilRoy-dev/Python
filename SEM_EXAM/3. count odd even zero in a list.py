# Sample list
numbers = [0, 1, 2, 3, 4, 0, 5, 6, 0, 7, 8, 9, 10]

# Initialize counters
even_count = 0
odd_count = 0
zero_count = 0

# Loop through the list
for num in numbers:
    if num == 0:
        zero_count += 1
    elif num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Display results
print("Zero count:", zero_count)
print("Even count:", even_count)
print("Odd count:", odd_count)
