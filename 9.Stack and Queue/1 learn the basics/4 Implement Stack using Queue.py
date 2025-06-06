from collections import deque


class StackUsingQueue:
    def __init__(self):
        self.queue = deque()  # Initialize a single queue using Python's deque

    def push(self, item):
        self.queue.append(item)  # Add the new item to the queue
        # Rotate the queue so the newest item is at the front
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        if len(self.queue) == 0:
            return "Stack is empty"
        return self.queue.popleft()  # Remove the front item (most recently added)

    def peek(self):
        if len(self.queue) == 0:
            return "Stack is empty"
        return self.queue[0]  # View the front item without removing

    def is_empty(self):
        return len(self.queue) == 0  # Check if the queue is empty

    def size(self):
        return len(self.queue)  # Return the size of the queue


if __name__ == "__main__":
    stack = StackUsingQueue()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Stack content = {stack}")  # Note: This will print the object reference
    print(f"Popped item = {stack.pop()}")
    print(f"Stack content = {stack}")
    print(f"Top item after pop = {stack.peek()}")
    print(f"Stack is empty = {stack.is_empty()}")