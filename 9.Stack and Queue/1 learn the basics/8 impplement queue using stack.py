class MinStack:

    def __init__(self):
        self.items = []  # Stack to store pairs of [value, min_value]

    def push(self, val: int) -> None:
        if not self.items:
            # If stack is empty, the new element is also the minimum
            self.items.append([val, val])
        else:
            # Store value and the minimum between current value and previous minimum
            mini = min(val, self.items[-1][1])
            self.items.append([val, mini])

    def pop(self) -> None:
        if self.items:
            self.items.pop()  # Remove the top element

    def top(self) -> int:
        if len(self.items) == 0:
            return 0  # Handle empty stack case
        return self.items[-1][0]  # Return the value (not the minimum)

    def getMin(self) -> int:
        if len(self.items) == 0:
            return 0  # Handle empty stack case
        return self.items[-1][1]