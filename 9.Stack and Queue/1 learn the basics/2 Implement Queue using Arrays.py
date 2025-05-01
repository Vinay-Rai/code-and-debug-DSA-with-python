class Queue:
    def __init__(self):
        self.items = []  # Initialize an empty list to store queue elements

    def is_empty(self):
        return len(self.items) == 0  # Return True if queue has no elements

    def enqueue(self, item):
        self.items.append(item)  # Add item to the end of the list (rear of queue)

    def dequeue(self):
        if len(self.items) == 0:
            print("Cannot dequeue from empty queue")
            return
        x = self.items.pop(0)  # Remove and return the first element
        return x

    def front(self):
        if len(self.items) == 0:
            print("Cannot front, queue is empty")
            return
        return self.items[0]  # Return the first element without removing it

    def rear(self):
        if len(self.items) == 0:
            print("Cannot rear, queue is empty")
            return
        return self.items[-1]  # Return the last element without removing it

    def size(self):
        return len(self.items)  # Return the number of elements in the queue


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(f"Queue content = {queue}")  # Note: This will print the object reference, not contents
    print(f"Dequeued item = {queue.dequeue()}")
    print(f"Queue content = {queue}")