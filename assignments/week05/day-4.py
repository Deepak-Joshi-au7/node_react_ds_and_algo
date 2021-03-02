'''
Assignment-

1) https://www.geeksforgeeks.org/exchange-first-last-node-circular-linked-list/
'''
import math 
  
class Node:  
    def __init__(self, data):  
        self.data = data  
        self.next = None
  
def addToEmpty(head, data): 
 
    if (head != None): 
        return head 
  
    temp = Node(data) 
  
    temp.data = data 
    head = temp 
   
    head.next = head 
    return head 
  
def addBegin(head, data): 
  
    if (head == None): 
        return addToEmpty(head, data) 
  
    temp = Node(data) 
    temp.data = data 
    temp.next = head.next
    head.next = temp 
  
    return head 

def traverse(head): 
 
    if (head == None): 
      
        print("List is empty.") 
        return
    
    p = head 
    print(p.data, end = " ") 
    p = p.next
 
    while(p != head): 
      
        print(p.data, end = " ") 
        p = p.next
  
def exchangeNodes(head): 

    p = head 
    while (p.next.next != head): 
       p = p.next
   
    p.next.next = head.next
    head.next = p.next
    p.next = head 
    head = head.next
    
    return head 
   
if __name__=='__main__':  
  
    head = None
    head = addToEmpty(head, 6) 
    for x in range(5, 0, -1): 
        head = addBegin(head, x) 
    print("List Before: ", end = "") 
    traverse(head) 
    print() 
      
    print("List After: ", end = "") 
    head = exchangeNodes(head) 
    traverse(head) 

    input()


'''    
2) https://www.geeksforgeeks.org/josephus-circle-using-circular-linked-list/
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class CircularLinkedList:
    def __init__(self):
        self.head = None
 
    def append(self, data):
        node = Node(data)
        self.insert_at_end(node)
 
    def get_node(self, index, start):
        if self.head is None:
            return None
        current = start
        for i in range(index):
            current = current.next
        return current
 
    def get_prev_node(self, ref_node):
        if self.head is None:
            return None
        current = self.head
        while current.next != ref_node:
            current = current.next
        return current
 
    def insert_after(self, ref_node, new_node):
        new_node.next = ref_node.next
        ref_node.next = new_node
 
    def insert_before(self, ref_node, new_node):
        prev_node = self.get_prev_node(ref_node)
        self.insert_after(prev_node, new_node)
 
    def insert_at_end(self, new_node):
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
        else:
            self.insert_before(self.head, new_node)
 
    def remove(self, node):
        if self.head.next == self.head:
            self.head = None
        else:
            prev_node = self.get_prev_node(node)
            prev_node.next = node.next
            if self.head == node:
                self.head = node.next
 
 
def has_one_node(cllist):
    if cllist.head.next == cllist.head:
        return True
    else:
        return False
 
 
def get_josephus_solution(cllist, k):
    if cllist.head is None:
        return None
    start = cllist.head
    while not has_one_node(cllist):
        to_remove = cllist.get_node(k - 1, start)
        start = to_remove.next
        cllist.remove(to_remove)
    return cllist.head.data
 
 
a_cllist = CircularLinkedList()
n = int(input('Input number of people: '))
k = int(input('The kth person will be executed. Input k: '))
for i in range(1, n + 1):
    a_cllist.append(i)
 
ans = get_josephus_solution(a_cllist, k)
print('The person at position {} won\'t be killed.'.format(ans))

input()