
class Node:

# Function to initialise the node object
	def __init__(self, data):
		self.data = data # Assign data
		self.next = None # Initialize next as null
		self.prev = None # Initialize prev as null
		
		
# Queue class contains a Node object
class Queue:

	# Function to initialize head 
	def __init__(self):
		self.head = None
		self.last=None
		

# Function to add an element data in the Queue
	def enqueue(self, data):
		if self.last is None:
			self.head =Node(data)
			self.last =self.head
		else:
			self.last.next = Node(data)
			self.last.next.prev=self.last
			self.last = self.last.next
			
			
			
# Function to remove first element and return the element from the queue 
	def dequeue(self):

		if self.head is None:
			return None
		else:
			temp= self.head.data
			self.head = self.head.next
			self.head.prev=None
			return temp


# Function to return top element in the queue 
	def first(self):

		return self.head.data


# Function to return the size of the queue
	def size(self):

		temp=self.head
		count=0
		while temp is not None:
			count=count+1
			temp=temp.next
		return count
	
	
# Function to check if the queue is empty or not	 
	def isEmpty(self):

		if self.head is None:
			return True
		else:
			return False
			

# Function to print the stack 
	def printqueue(self):
		
		print("queue elements are:")
		temp=self.head
		while temp is not None:
			print(temp.data,end="->")
			temp=temp.next
	
		
# Code execution starts here		 
if __name__=='__main__': 

# Start with the empty queue
    queue = Queue()

    print("Queue operations using doubly linked list")

    # Insert 4 at the end. So queue becomes 4->None 
    queue.enqueue(4)

    # Insert 5 at the end. So queue becomes 4->5None 
    queue.enqueue(5)

    # Insert 6 at the end. So queue becomes 4->5->6->None 
    queue.enqueue(6)

    # Insert 7 at the end. So queue becomes 4->5->6->7->None 
    queue.enqueue(7)

    # Print the queue 
    queue.printqueue()

    # Print the first element 
    print("\nfirst element is ",queue.first())

    # Print the queue size 
    print("Size of the queue is ",queue.size())

    # remove the first element 
    queue.dequeue()

    # remove the first element 
    queue.dequeue()

    # first two elements are removed
    # Print the queue 
    print("After applying dequeue() two times")
    queue.printqueue()

    # Print True if queue is empty else False 
    print("\nqueue is empty:",queue.isEmpty())




# DLL Node structure
class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
        self.prev = None

# Doubly Linked List structure
class DLL:
    def __init__(self):
        self.start = None
        self.top = None

    # Check if stack is empty
    def isEmpty(self):
        return self.start is None

    # add element to stack
    def push(self, val):
        cur = Node(val)

        # if stack is empty, 
        # set start and top to cur
        if self.isEmpty():
            self.start = cur
            self.top = cur
        # else add cur to the top of stack
        else:
            self.top.next = cur
            cur.prev = self.top
            self.top = cur

    # remove top element from stack
    def pop(self):
        cur = self.top

        # if stack is empty, return
        if self.isEmpty():
            print("Stack is Empty", end="")
            return
        # else if there is only one element
        elif self.top == self.start:
            self.top = None
            self.start = None
            del cur
        # else remove the top element
        else:
            self.top.prev.next = None
            self.top = cur.prev
            del cur

    # print the top element
    def topElement(self):
        if self.isEmpty():
            print("Stack is empty", end="")
        else:
            print(self.top.data)

    # find the stack size
    def stackSize(self):
        cnt = 0
        ptr = self.start
        while ptr is not None:
            cnt += 1
            ptr = ptr.next
        print(cnt)

    # print the stack
    def printStack(self):
        ptr = self.start
        while ptr is not None:
            print(ptr.data, end=" ")
            ptr = ptr.next
        print()

if __name__ == "__main__":
    stack = DLL()
    stack.push(2)
    stack.push(5)
    stack.push(10)
    stack.printStack()
    stack.topElement()
    stack.stackSize()
    stack.pop()
    stack.printStack()
    stack.topElement()
    stack.stackSize()