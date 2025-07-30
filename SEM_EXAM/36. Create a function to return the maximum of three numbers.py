# Function to return the maximum of three numbers
def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Example usage
num1 = 15
num2 = 42
num3 = 37

maximum = find_max(num1, num2, num3)
print(f"The maximum of {num1}, {num2}, and {num3} is {maximum}")
