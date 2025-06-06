class StackQueue:
    def __init__(self):
        self.st1 = []  # Main stack for storing elements in queue order
        self.st2 = []  # Auxiliary stack for temporary storage during operations

    def push(self, x):
        # Move everything from st1 to st2
        while self.st1:
            self.st2.append(self.st1.pop())
        
        # Add the new element to the bottom of st1
        self.st1.append(x)
        
        # Move everything back from st2 to st1
        while self.st2:
            self.st1.append(self.st2.pop())

    def pop(self):
        if not self.st1:
            print("Stack is empty")
            return -1  # Representing empty queue
        
        # Simply pop from st1 since elements are stored in queue order
        top_element = self.st1.pop()
        return top_element

    def peek(self):
        if not self.st1:
            print("Stack is empty")
            return -1
        
        # Return the top element without removing it
        return self.st1[-1]

    def is_empty(self):
        return not self.st1  # Return True if st1 is empty


if __name__ == "__main__":
    q = StackQueue()

    # List of commands
    commands = ["StackQueue", "push", "push", "pop", "peek", "isEmpty"]
    # List of inputs
    inputs = [[], [4], [8], [], [], []]

    for i in range(len(commands)):
        if commands[i] == "push":
            q.push(inputs[i][0])
            print("null", end=" ")
        elif commands[i] == "pop":
            print(q.pop(), end=" ")
        elif commands[i] == "peek":
            print(q.peek(), end=" ")
        elif commands[i] == "isEmpty":
            print("true" if q.is_empty() else "false", end=" ")
        elif commands[i] == "StackQueue":
            print("null", end=" ")

