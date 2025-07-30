# Define two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Merge using unpacking
merged_dict = {**dict1, **dict2}

# Print the result
print("Merged dictionary:", merged_dict)

#Another Method
# Define two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Copy and update
merged_dict = dict1.copy()  # Make a copy to keep dict1 unchanged
merged_dict.update(dict2)

# Print the result
print("Merged dictionary:", merged_dict)
