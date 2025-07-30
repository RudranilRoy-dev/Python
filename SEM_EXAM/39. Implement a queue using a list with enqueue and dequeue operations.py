# Queue implementation using list
queue = []

# Enqueue operation (add to end)
def enqueue(item):
    queue.append(item)
    print(f"Enqueued: {item}")
    print("Queue: ",queue)

# Dequeue operation (remove from front)
def dequeue():
    if not queue:
        print("Queue is empty. Cannot dequeue.")
    else:
        removed = queue.pop(0)
        print(f"Dequeued: {removed}")
        print("Queue: ",queue)

# Example usage
enqueue(10)
enqueue(20)
enqueue(30)

dequeue()
dequeue()
dequeue()
dequeue()  # Attempting to dequeue from empty queue