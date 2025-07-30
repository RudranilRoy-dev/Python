# Step 1: Original tuple
weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

# Step 2: Convert tuple to list
weekdays_list = list(weekdays)

# Step 3: Update a value (e.g., change "Wednesday" to "WED")
weekdays_list[2] = "WED"

# Step 4: Convert the list back to a tuple
updated_weekdays = tuple(weekdays_list)

# Step 5: Print the final result
print("Updated tuple:", updated_weekdays)
