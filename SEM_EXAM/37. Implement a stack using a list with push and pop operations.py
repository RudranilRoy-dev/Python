# Stack implementation using list
stack = []

# Push operation
def push(item):
    stack.append(item)
    print(f"Pushed: {item}")
    print(stack)

# Pop operation
def pop():
    if not stack:
        print("Stack is empty. Cannot pop.")
        return
    else:
        removed = stack.pop()
        print(f"Popped: {removed}")
    print(stack)

# Example usage
push(10)
push(20)
push(30)

pop()
pop()
pop()
pop()  # Trying to pop from an empty stack
