class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class singlyLinledList:
    def __init__(self):
        self.head = None
    
    def append(self,val):
        new_node = Node(val)
        #for empty linked list

        if self.head == None:
            self.head = new_node
        
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
        #time complexity in worst case is 0(n)  in best case 0(1)  jab first element hi append ho raha ho
        #space complexity  o(1)
    
    
    def traversal(self):
        #for empty linked list
        
        if self.head is None:
            print("linkedlist is empty")
        else:
            curr = self.head
            while curr is not None:
                print(curr.data,end=" ")
                curr = curr.next
            print()

    def insert_at(self,val,position):
        new_node = Node(val)
        if position == 0:
            new_node.next = self.head
            self.head  = new_node
        else:
            current = self.head
            prev_node = None
            count = 0
            while current is not None and count < position:
                prev_node = current
                current = current.next
                count +=1
            prev_node.next = new_node
            new_node.next = current

    def delete(self,val):
        temp =self.head
        if temp.next is not None:
            if temp.data == val:
                self.head  = temp.next
                return
            else:
                found = False  #found is liye likha hai kyoki koi flaga hame bata to de ki found hua hai ya nahi
                prev = None
                while temp is not None:
                    if temp.data == val:
                        found = True
                        break
                    prev = temp
                    temp = temp.next
                
                if found:
                    prev.next = temp.next
                    return
                else:
                    print("Node not found")
    def middle(self):
        slow= self.head
        fast = self.head
        while fast != None and fast.next!= None:
            slow =slow.next
            fast = fast.next.next
        return slow.data
    
    def reverse(self):
        prev = None
        curr = self.head
        nxt = self.head.next
        while nxt != None:
            curr.next= prev
            prev = curr
            curr = nxt
            nxt = nxt.next

        curr.next = prev 
        self.head = curr
        return self.head

    def reversal(self):
        curr = self.head
        prev = None
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return curr
    
    def deleteNthNode(self,n):
        temp = self.head
        count = 0
        while temp is not None:
            count+=1
            temp=temp.next
        if n == count:
            self.head = self.head.next
            return self.head
        temp = self.head
        for i in range(1,count-n):
            temp = temp.next
        temp.next = temp.next.next

        return self.head




            





ll = singlyLinledList()
ll.append(10)
ll.append(12)
ll.append(13)
ll.append(4)
ll.append(1)
# ll.traversal()
print(ll.reversal())
ll.traversal()
# ll.deleteNthNode(5)
# ll.traversal()


