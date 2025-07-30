import csv

# ✅ Step 1: Predefined student data
students = [
    {"Name": "Riya", "Marks": 85, "Grade": "A"},
    {"Name": "Rudra", "Marks": 70, "Grade": "B"},
    {"Name": "Nil", "Marks": 90, "Grade": "A"},
    {"Name": "Roy", "Marks": 60, "Grade": "C"}
]

# ✅ Step 2: Filter students with marks > 75
filtered_students = []
for student in students:
    if student["Marks"] > 75:
        filtered_students.append(student)

# ✅ Step 3: Write to a new CSV file
with open("52. file.csv", 'w',newline='') as file:
    fieldnames = ["Name", "Marks", "Grade"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(filtered_students)
