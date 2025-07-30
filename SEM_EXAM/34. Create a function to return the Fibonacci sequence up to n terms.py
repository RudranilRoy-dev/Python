# Recursive function to return the nth Fibonacci number
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# Function to generate Fibonacci sequence up to n terms using recursion
def fibonacci_sequence(n):
    sequence = []
    for i in range(n+1):
        sequence.append(fib(i))
    return sequence

# Example usage
terms = 10
result = fibonacci_sequence(terms)
print("Fibonacci sequence up to",terms,"terms:",result)
