class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):   #o(1)
        return len(self.items) == 0
    
    def push(self,item):   #o(1)
        self.items.append(item)
    
    def pop(self):   #o(1)
        if len(self.items)==0:
            return "cannot pop stack is empty"
        x = self.items.pop()
        return x
    def top(self):    #o(1)
        if len(self.items)==0:
            return "cannot pop stack is empty"
        return self.items[-1]
    def size(self):     #o(1)
        return len(self.items)


stack = Stack()
stack.push(1)   
stack.push(4)
stack.push(8)
stack.push(6)
print(stack.pop())
print(stack.is_empty())
print(stack.top())
print(stack.size())