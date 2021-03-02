Assignment:
'''
1) Given 2 very very big numbers(10^1000) use doubly linked lists to perform operations on them(+,-,*,/).
'''
class Node:  
      
    def __init__(self, data):  
        self.data = data  
        self.prev = None
        self.next = None
 
def push(head_ref, new_data): 
    new_node =Node(0) 
    new_node.data = new_data 
    new_node.prev = None
    new_node.next = (head_ref) 
  
  
    if ((head_ref) != None): 
        (head_ref).prev = new_node 
    (head_ref) = new_node 
    return head_ref 
 
def operation(data1,data2): 
    add= 0
    sub = 0
    mul = 0
    div = 0
    mod = 0

    add = data1 + data2
    sub = data1 - data2
    mul = data1 * data2
    div = data1 / data2
    mod = data1 % data2

    return add,sub,mul,div,mod

if __name__ == "__main__":  

    head = None
  
    head = push(head,10) 
    head = push(head,20) 
    head = push(head,6) 
    head = push(head,9) 
    head = push(head,12) 
    head = push(head,16) 
    head = push(head,15) 
   
    sum = operation(10^1000,10^1000) 
    print("added value, Subracted value, Multiplied value, Divided value, Mod Value ", sum )


    input()
  

'''
2) Reverse a Doubly linked list using recursion
'''

import math 

class Node:  
    def __init__(self, data):  
        self.data = data  
        self.next = None

def getNode(data): 
    new_node = Node(data) 
    new_node.data = data 
    new_node.next = new_node.prev = None
    return new_node 

def push(head_ref, new_node):    
    new_node.prev = None
    new_node.next = head_ref 
    if (head_ref != None): 
        head_ref.prev = new_node 
    head_ref = new_node 
    return head_ref 
  
def Reverse(node):

    if not node: 
        return None
    temp = node.next
    node.next = node.prev 
    node.prev = temp 
  
    if not node.prev: 
        return node 
    return Reverse(node.prev) 
  
def printList(head): 
    while (head != None) : 
        print(head.data, end = " ") 
        head = head.next
      
if __name__=='__main__':  
    head = None
    head = push(head, getNode(5));  
    head = push(head, getNode(2));  
    head = push(head, getNode(10));  
    head = push(head, getNode(8)); 
    print("Original list: ", end = " ") 
    printList(head) 
  
    head = Reverse(head) 
    print("\nReversed list: ", end = " ") 
    printList(head) 

input()