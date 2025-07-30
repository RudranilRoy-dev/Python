# Function to return a dictionary of cubes from 1 to n using dict comprehension
def cubes_dict(n):
    return {i: i**3 for i in range(1, n + 1)}

# Example usage
n = 5
result = cubes_dict(n)

# Print the resulting dictionary
print(f"Cubes from 1 to {n}:")
print(result)
