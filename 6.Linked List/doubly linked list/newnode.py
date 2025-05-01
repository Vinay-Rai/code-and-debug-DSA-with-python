class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

n1 = Node(10)
n2 = Node(12)
n3 = Node(14)
n1.next = n2
n2.prev = n1
n2.next = n3
n3.prev = n2

print(n2.next.val)