def is_balanced(expression):
    stack = []

    for char in expression:
        if char == '(':
            stack.append(char)  # Push opening parenthesis
        elif char == ')':
            if not stack:
                return False  # No matching opening parenthesis
            stack.pop()  # Pop the matching opening parenthesis

    return len(stack) == 0  # True if all parentheses matched

# Example usage
expr1 = "()()"
expr2 = "(()"
expr3 = "(())"

print(f"'{expr1}' is Balanced: {is_balanced(expr1)}")
print(f"'{expr2}' is Balanced: {is_balanced(expr2)}")
print(f"'{expr3}' is Balanced: {is_balanced(expr3)}")
