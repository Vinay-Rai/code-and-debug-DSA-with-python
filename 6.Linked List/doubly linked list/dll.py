class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None


class doublylinkedlist:
    def __init__(self):
        self.head = None

    def insert_at_head(self,val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node.prev
    
    def append(self,val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node

        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def insert_at(self,val,position):
        new_node = Node(val)
        if position == 0:
            self.insert_at_head(val)
            return

        current = self.head
        count = 0
        while current and count < position -1:
            current  = current.next
            count+=1
        
        if current is None:
            print("position out of bound")
            return
        
        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node
    
    def  traverse(self):
        curr =self.head
        while curr is not None:
            print(curr.val)
            curr = curr.next
        

    def reverse(self):
        curr = self.head
        prev = None
        while curr != None:
            prev = curr.prev
            curr.prev = curr.next
            curr.next = prev
            curr = curr.prev
        self.head = curr
        return curr
    


dll = doublylinkedlist()
dll.append(2)
dll.append(1)
dll.append(6)
dll.append(5)
dll.append(3)
dll.traverse()
dll.reverse()
print()
dll.traverse()
