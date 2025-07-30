# Step 1: Create a dictionary of students with marks
students = {
    "Alice": 82,
    "Bob": 68,
    "Charlie": 90,
    "Diana": 74,
    "Ethan": 77
}

# Step 2: Print names of students scoring more than 75
print("Students scoring more than 75:")

for name, marks in students.items():
    if marks > 75:
        print(name)
