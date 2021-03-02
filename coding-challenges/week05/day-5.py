'''
CC:

1) https://www.geeksforgeeks.org/rotate-doubly-linked-list-n-nodes/
'''
#solution
class Node:  
    def __init__(self, next = None,  
                       prev = None, data = None):  
        self.next = next 
        self.prev = prev  
        self.data = data  
  
def push(head, new_data):  
  
    new_node = Node(data = new_data)  
  
    new_node.next = head  
    new_node.prev = None
  
    if head is not None:  
        head.prev = new_node  
  
    head = new_node 
    return head 
  
def printList(head): 
  
    node = head 
  
    print("Given linked list") 
    while(node is not None):  
        print(node.data, end = " "),  
        last = node  
        node = node.next
      
def rotate(start, N): 
    if N == 0 : 
        return

    current = start  
    count = 1
    while count < N and current != None : 
        current = current.next
        count += 1

    if current == None : 
        return
    NthNode = current  
  
    while current.next != None : 
        current = current.next  
    current.next = start    
    start.prev = current    
    start = NthNode.next
    start.prev = None
    NthNode.next = None
  
    return start
if __name__ == "__main__": 
    head = None
  
    head = push(head, 1) 
    head = push(head, 2) 
    head = push(head, 3) 
    head = push(head, 4) 
    head = push(head, 5) 
  
    printList(head) 
    print("\n") 
      
    N = 2
    head = rotate(head, 3) 
  
    printList(head) 

input()  
'''
2) https://www.geeksforgeeks.org/insertion-sort-doubly-linked-list/
'''
#solution
class Node:  
      
    def __init__(self, data):  
        self.data = data  
        self.prev = None
        self.next = None

def getNode(data): 
    newNode = Node(0) 
    newNode.data = data 
    newNode.prev = newNode.next = None
    return newNode 

def sortedInsert(head_ref, newNode): 
  
    current = None
    if (head_ref == None): 
        head_ref = newNode 
    elif ((head_ref).data >= newNode.data) : 
        newNode.next = head_ref 
        newNode.next.prev = newNode 
        head_ref = newNode 
    else : 
        current = head_ref 
  
        while (current.next != None and
            current.next.data < newNode.data): 
            current = current.next
        newNode.next = current.next
  
        if (current.next != None): 
            newNode.next.prev = newNode 
        current.next = newNode 
        newNode.prev = current 
    return head_ref; 
      

def insertionSort( head_ref): 
    sorted = None
    current = head_ref 
    while (current != None) : 
        next = current.next
        current.prev = current.next = None
        sorted = sortedInsert(sorted, current) 
        current = next
    head_ref = sorted
    return head_ref 
  

def printList(head): 
    while (head != None) : 
        print( head.data, end = " ") 
        head = head.next

def push(head_ref, new_data): 
    new_node = Node(0) 
    new_node.data = new_data 
    new_node.next = (head_ref) 
    new_node.prev = None
  
    if ((head_ref) != None): 
        (head_ref).prev = new_node 
    (head_ref) = new_node 
    return head_ref 
  
if __name__ == "__main__":  
  
    head = None
    head = push(head, 5) 
    head = push(head, 1) 
    head = push(head, 5) 
    head = push(head, 14) 
    head = push(head, 10) 
    head = push(head, 8) 
  
    print( "Doubly Linked List Before Sorting") 
    printList(head) 
  
    head = insertionSort(head) 
  
    print("\n\nDoubly Linked List After Sorting") 
    printList(head) 
  
input()