import csv

# Step 1: Define the new student record
new_student = {"Name": "Nilu", "Marks": 88, "Grade": "A"}

# Step 2: Open the existing CSV file in append mode
with open("52. file.csv", 'a', newline='') as file:
    fieldnames = ["Name", "Marks", "Grade"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    # Step 3: Write the new row (appended at the end)
    writer.writerow(new_student)
