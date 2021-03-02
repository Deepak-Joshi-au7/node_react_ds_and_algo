
'''
GRAPH
1.https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/
'''
#solution
class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] 
                      for row in range(vertices)]

    def printMST(self, parent):
        print ("Edge \tWeight")
        for i in range(1,self.V):
            print (parent[i],"-",i,"\t",self.graph[i][ parent[i] ])
    
    def minKey(self, key, mstSet):
      
        min = 1000000
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
        return min_index
  
    def primMST(self):
     
        key = [1000000] * self.V
        parent = [None] * self.V 
        key[0] = 0  
        mstSet = [False] * self.V
        parent[0] = -1 

        for cout in range(self.V):

            u = self.minKey(key, mstSet)
            mstSet[u] = True
            
            for v in range(self.V):
               
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                        key[v] = self.graph[u][v]
                        parent[v] = u
        self.printMST(parent)
g  = Graph(5)
g.graph = [  [0, 2, 0, 6, 0],
             [2, 0, 3, 8, 5],
             [0, 3, 0, 0, 7],
             [6, 8, 0, 0, 9],
             [0, 5, 7, 9, 0],
          ]
g.primMST();

input()

'''
2.https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
'''
#solution
from collections import defaultdict

class Graph:

    def __init__(self,vertices):
        self.V= vertices
        self.graph = [] 

    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else :
            parent[yroot] = xroot
            rank[xroot] += 1

    def KruskalMST(self):
        result =[]
        i,e = 0,0 
        self.graph =  sorted(self.graph,key=lambda item: item[2])
        parent = [] ; rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0) 

        while e < self.V -1 :
            u,v,w =  self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent ,v)
            if x != y:
                e = e + 1  
                result.append([u,v,w])
                self.union(parent, rank, x, y)          
        print("Constructed MST :")
        print("Vertex A    Vertex B  Weight")
        for u,v,weight  in result:
            print ("    %d          %d        %d" % (u,v,weight))

g = Graph(4) 
g.addEdge(0, 1, 10) 
g.addEdge(0, 2, 6) 
g.addEdge(0, 3, 5) 
g.addEdge(1, 3, 15) 
g.addEdge(2, 3, 4) 

g.KruskalMST()

input()
'''
3.https://www.geeksforgeeks.org/minimum-cost-connect-cities/
'''
#solution
def minnode(n, keyval, mstset): 
      mini = 999999999999
      mini_index = None
      
      for i in range(n): 
          if (mstset[i] == False and 
              keyval[i] < mini):  
              mini = keyval[i] 
              mini_index = i 
      return mini_index 
  
 
def findcost(n, city): 
  
      parent = [None] * n 
      keyval = [None] * n  
      mstset = [None] * n 
    
      for i in range(n): 
          keyval[i] = 9999999999999
          mstset[i] = False
      
      parent[0] = -1
      keyval[0] = 0
      
      for i in range(n - 1): 
      
          u = minnode(n, keyval, mstset)  
          mstset[u] = True
     
          for v in range(n): 
              if (city[u][v] and mstset[v] == False and 
                  city[u][v] < keyval[v]):  
                  keyval[v] = city[u][v]  
                  parent[v] = u 
 
      cost = 0
      
      for i in range(1, n):
          cost += city[parent[i]][i]
      
      print(" Cost :",cost)
    

if __name__ == '__main__': 

      n1 = 5
      city1 = [[0, 1, 2, 3, 4],  
               [1, 0, 5, 0, 7],  
               [2, 5, 0, 6, 0], 
               [3, 0, 6, 0, 0],  
               [4, 7, 0, 0, 0]]  
      findcost(n1, city1)  
      
      n2 = 6
      city2 = [[0, 1, 1, 100, 0, 0], 
               [1, 0, 1,   0, 0, 0],  
               [1, 1, 0,   0, 0, 0],  
               [100,  0, 0,0, 2, 2], 
               [0, 0, 0,   2, 0, 2],  
               [0, 0, 0,   2, 2, 0]]  
      
      findcost(n2, city2)

input()
'''
TREE
1.https://www.geeksforgeeks.org/level-order-tree-traversal/
'''
#solution
class Node: 

    def __init__(self, key): 
        self.data = key  
        self.left = None
        self.right = None

def printLevelOrder(root): 
    h = height(root) 
    for i in range(1, h+1): 
        printGivenLevel(root, i) 
  
def printGivenLevel(root , level): 
    if root is None: 
        return
    if level == 1: 
        print ("%d") %(root.data), 
    elif level > 1 : 
        printGivenLevel(root.left , level-1) 
        printGivenLevel(root.right , level-1) 

def height(node): 
    if node is None: 
        return 0 
    else : 
        # Compute the height of each subtree  
        lheight = height(node.left) 
        rheight = height(node.right) 
  
        #Use the larger one 
        if lheight > rheight : 
            return lheight+1
        else: 
            return rheight+1

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
  
print ("Level order traversal of binary tree is -")
printLevelOrder(root)


input()

'''
2.https://www.geeksforgeeks.org/check-if-two-trees-are-mirror/
'''
#solution
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
  
def areMirror(a, b): 

    if a is None and b is None: 
        return True

    if a is None or b is None: 
        return False

    return (a.data == b.data and 
            areMirror(a.left, b.right) and 
            areMirror(a.right , b.left)) 
  
root1 = Node(1) 
root2 = Node(1) 
  
root1.left = Node(2) 
root1.right = Node(3) 
root1.left.left = Node(4) 
root1.left.right = Node(5) 
  
root2.left = Node(3) 
root2.right = Node(2) 
root2.right.left = Node(5) 
root2.right.right = Node(4) 
  
if areMirror(root1, root2): 
    print ("Yes") 
else: 
    print ("No")
    
input()

'''
3.https://www.geeksforgeeks.org/given-level-order-traversal-binary-tree-check-tree-min-heap/
'''
#solution
def isMinHeap(level, n): 
      
    for i in range(int(n / 2) - 1, -1, -1): 

        if level[i] > level[2 * i + 1]:  
            return False
  
        if 2 * i + 2 < n: 
               
            if level[i] > level[2 * i + 2]: 
                return False
    return True
  

if __name__ == '__main__': 
    level = [10, 15, 14, 25, 30]  
    n = len(level) 
    if isMinHeap(level, n):  
        print("True")  
    else: 
        print("False")

input()