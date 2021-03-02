'''
CCs -

1) https://www.geeksforgeeks.org/pairwise-swap-elements-of-a-given-linked-list/
'''
#answer
 
class Node: 
  
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
class LinkedList: 

    def __init__(self): 
        self.head = None
 
    def pairwiseSwap(self): 
        temp = self.head 
     
        if temp is None: 
            return 
      
        while(temp is not None and temp.next is not None): 
  
            temp.data, temp.next.data = temp.next.data, temp.data  
       
            temp = temp.next.next
         
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
  

    def printList(self): 
        temp = self.head 
        while(temp): 
            print temp.data, 
            temp = temp.next
  
llist = LinkedList() 
llist.push(5) 
llist.push(4) 
llist.push(3) 
llist.push(2) 
llist.push(1) 
  
print "Linked list before calling pairWiseSwap() "
llist.printList() 
  
llist.pairwiseSwap() 
  
print  "\nLinked list after calling pairWiseSwap()"
llist.printList() 


input()
'''
2) https://www.geeksforgeeks.org/quicksort-on-singly-linked-list/
'''
#solution

'''
3) https://www.geeksforgeeks.org/reverse-a-linked-list/
'''
#solution
class Node: 
   
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
class LinkedList: 

    def __init__(self): 
        self.head = None

    def reverse(self): 
        prev = None
        current = self.head 
        while(current is not None): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        self.head = prev 
   
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
  
    def printList(self): 
        temp = self.head 
        while(temp): 
            print (temp.data, end=" ")
            temp = temp.next
  
llist = LinkedList() 
llist.push(20) 
llist.push(4) 
llist.push(15) 
llist.push(85) 
  
print ("Given Linked List")
llist.printList() 
llist.reverse() 
print ("\nReversed Linked List")
llist.printList() 

input()
  