# Create a sample dictionary
students = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78
}

# Use .get() to safely access a key that exists
print("Alice's marks:", students.get("Alice"))

# Try to access a key that does NOT exist using .get()
print("Ethan's marks:", students.get("Ethan"))  # Returns None

# Provide a default message if the key is not found
print("Ethan's marks:", students.get("Ethan", "Not found"))
