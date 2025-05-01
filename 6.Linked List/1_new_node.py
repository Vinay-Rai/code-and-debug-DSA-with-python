class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

node1 = Node(3)
node2 = Node(4)
node3 = Node(5)
node4 = Node(6)
node5 = Node(7)
node6 = Node(8)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
# node6.next = node5

print(node1)        #ye object address print karega
print(node1.next)   #ye object address print karega
print(node1.next.data)

def loop(head):
    slow = head
    fast = head
    while fast != None and fast.next is not None:    #fast walw ko isliye none kiya kyonki agar slow wale  ko karte to fast pehle none ho jata or erro dene lagta

        #node compare kara reahe hain na ki node ki value
        slow  = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

print(loop(node1))

def positionlopp(head):
    di={}
    count = 0
    slow = head
    while slow != None:
        if slow not in di:
            di[slow]=count
            slow = slow.next
            count +=1
        else:
            return di[slow]
    return -1

print(positionlopp(node1))