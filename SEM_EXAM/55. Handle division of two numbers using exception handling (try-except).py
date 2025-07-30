# Step 1: Input two numbers
numerator = int(input("Enter numerator: "))
denominator = int(input("Enter denominator: "))

# Step 2: Try to divide and catch any errors
try:
    result = numerator / denominator
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Invalid input.")

except Exception as e:
    print("An unexpected error occurred:", e)
