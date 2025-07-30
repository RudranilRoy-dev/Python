import pickle

filename = "48. file.dat"
student_to_update = "rudra"
new_marks = 95

# Step 1: Read the dictionary (assuming only one is stored)
with open(filename, 'rb') as file:
    data = pickle.load(file)

# Step 2: Update the student's marks
if student_to_update in data:
    data[student_to_update] = new_marks
else:
    print(f"Student '{student_to_update}' not found.")

# Step 3: Write back the updated dictionary
with open(filename, 'wb') as file:
    pickle.dump(data, file)

print("Updated data:", data)
