'''
ASSIGNMENT

GRAPH
1.https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/
'''
#solution
import sys 
  
class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
  
    def printSolution(self, dist): 
        print ("Vertex \tDistance from Source")
        for node in range(self.V): 
            print (node, "\t", dist[node]) 
  
    # A utility function to find the vertex with  
    # minimum distance value, from the set of vertices  
    # not yet included in shortest path tree 
    def minDistance(self, dist, sptSet): 
  
        # Initilaize minimum distance for next node 
        min = sys.maxint 
  
        # Search not nearest vertex not in the  
        # shortest path tree 
        for v in range(self.V): 
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v] 
                min_index = v 
  
        return min_index 
  
    # Funtion that implements Dijkstra's single source  
    # shortest path algorithm for a graph represented  
    # using adjacency matrix representation 
    def dijkstra(self, src): 
  
        dist = [sys.maxint] * self.V 
        dist[src] = 0
        sptSet = [False] * self.V 
  
        for cout in range(self.V): 
  
            # Pick the minimum distance vertex from  
            # the set of vertices not yet processed.  
            # u is always equal to src in first iteration 
            u = self.minDistance(dist, sptSet) 
  
            # Put the minimum distance vertex in the  
            # shotest path tree 
            sptSet[u] = True
  
            # Update dist value of the adjacent vertices  
            # of the picked vertex only if the current  
            # distance is greater than new distance and 
            # the vertex in not in the shotest path tree 
            for v in range(self.V): 
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]: 
                        dist[v] = dist[u] + self.graph[u][v] 
  
        self.printSolution(dist) 
  
# Driver program 
g = Graph(9) 
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
        [4, 0, 8, 0, 0, 0, 0, 11, 0], 
        [0, 8, 0, 7, 0, 4, 0, 0, 2], 
        [0, 0, 7, 0, 9, 14, 0, 0, 0], 
        [0, 0, 0, 9, 0, 10, 0, 0, 0], 
        [0, 0, 4, 14, 10, 0, 2, 0, 0], 
        [0, 0, 0, 0, 0, 2, 0, 1, 6], 
        [8, 11, 0, 0, 0, 0, 1, 0, 7], 
        [0, 0, 2, 0, 0, 0, 6, 7, 0] 
        ]; 
  
g.dijkstra(0);
'''
2.https://www.geeksforgeeks.org/dijkstras-algorithm-for-adjacency-list-representation-greedy-algo-8/
'''

#Answer:- 

from collections import defaultdict 
import sys 
  
class Heap(): 
  
    def __init__(self): 
        self.array = [] 
        self.size = 0
        self.pos = [] 
  
    def newMinHeapNode(self, v, dist): 
        minHeapNode = [v, dist] 
        return minHeapNode 
  
    # A utility function to swap two nodes  
    # of min heap. Needed for min heapify 
    def swapMinHeapNode(self,a, b): 
        t = self.array[a] 
        self.array[a] = self.array[b] 
        self.array[b] = t 
  
    # A standard function to heapify at given idx 
    # This function also updates position of nodes  
    # when they are swapped.Position is needed  
    # for decreaseKey() 
    def minHeapify(self, idx): 
        smallest = idx 
        left = 2*idx + 1
        right = 2*idx + 2
  
        if left < self.size and self.array[left][1]  < self.array[smallest][1]: 
            smallest = left 
  
        if right < self.size and self.array[right][1] < self.array[smallest][1]: 
            smallest = right 
  
        # The nodes to be swapped in min  
        # heap if idx is not smallest 
        if smallest != idx: 
  
            # Swap positions 
            self.pos[ self.array[smallest][0] ] = idx 
            self.pos[ self.array[idx][0] ] = smallest 
  
            # Swap nodes 
            self.swapMinHeapNode(smallest, idx) 
  
            self.minHeapify(smallest) 
  
    # Standard function to extract minimum  
    # node from heap 
    def extractMin(self): 
  
        # Return NULL wif heap is empty 
        if self.isEmpty() == True: 
            return
  
        # Store the root node 
        root = self.array[0] 
  
        # Replace root node with last node 
        lastNode = self.array[self.size - 1] 
        self.array[0] = lastNode 
  
        # Update position of last node 
        self.pos[lastNode[0]] = 0
        self.pos[root[0]] = self.size - 1
  
        # Reduce heap size and heapify root 
        self.size -= 1
        self.minHeapify(0) 
  
        return root 
  
    def isEmpty(self): 
        return True if self.size == 0 else False
  
    def decreaseKey(self, v, dist): 
  
        # Get the index of v in  heap array 
  
        i = self.pos[v] 
  
        # Get the node and update its dist value 
        self.array[i][1] = dist 
  
        # Travel up while the complete tree is  
        # not hepified. This is a O(Logn) loop 
        while i > 0 and self.array[i][1] < self.array[(i - 1) / 2][1]: 
  
            # Swap this node with its parent 
            self.pos[ self.array[i][0] ] = (i-1)/2
            self.pos[ self.array[(i-1)/2][0] ] = i 
            self.swapMinHeapNode(i, (i - 1)/2 ) 
  
            # move to parent index 
            i = (i - 1) / 2; 
  
    # A utility function to check if a given  
    # vertex 'v' is in min heap or not 
    def isInMinHeap(self, v): 
  
        if self.pos[v] < self.size: 
            return True
        return False
  
  
def printArr(dist, n): 
    print ("Vertex\tDistance from source")
    for i in range(n): 
        print ("%d\t\t%d" % (i,dist[i])) 
  
  
class Graph(): 
  
    def __init__(self, V): 
        self.V = V 
        self.graph = defaultdict(list) 
  
    # Adds an edge to an undirected graph 
    def addEdge(self, src, dest, weight): 
  
        # Add an edge from src to dest.  A new node  
        # is added to the adjacency list of src. The  
        # node is added at the beginning. The first  
        # element of the node has the destination  
        # and the second elements has the weight 
        newNode = [dest, weight] 
        self.graph[src].insert(0, newNode) 
  
        # Since graph is undirected, add an edge  
        # from dest to src also 
        newNode = [src, weight] 
        self.graph[dest].insert(0, newNode) 
  
    # The main function that calulates distances  
    # of shortest paths from src to all vertices.  
    # It is a O(ELogV) function 
    def dijkstra(self, src): 
  
        V = self.V  # Get the number of vertices in graph 
        dist = []   # dist values used to pick minimum  
                    # weight edge in cut 
  
        # minHeap represents set E 
        minHeap = Heap() 
  
        #  Initialize min heap with all vertices.  
        # dist value of all vertices 
        for v in range(V): 
            dist.append(sys.maxint) 
            minHeap.array.append( minHeap.newMinHeapNode(v, dist[v]) ) 
            minHeap.pos.append(v) 
  
        # Make dist value of src vertex as 0 so  
        # that it is extracted first 
        minHeap.pos[src] = src 
        dist[src] = 0
        minHeap.decreaseKey(src, dist[src]) 
  
        # Initially size of min heap is equal to V 
        minHeap.size = V; 
  
        # In the following loop, min heap contains all nodes 
        # whose shortest distance is not yet finalized. 
        while minHeap.isEmpty() == False: 
  
            # Extract the vertex with minimum distance value 
            newHeapNode = minHeap.extractMin() 
            u = newHeapNode[0] 
  
            # Traverse through all adjacent vertices of  
            # u (the extracted vertex) and update their  
            # distance values 
            for pCrawl in self.graph[u]: 
  
                v = pCrawl[0] 
  
                # If shortest distance to v is not finalized  
                # yet, and distance to v through u is less  
                # than its previously calculated distance 
                if minHeap.isInMinHeap(v) and dist[u] != sys.maxint and pCrawl[1] + dist[u] < dist[v]: 
                        dist[v] = pCrawl[1] + dist[u] 
  
                        # update distance value  
                        # in min heap also 
                        minHeap.decreaseKey(v, dist[v]) 
  
        printArr(dist,V) 
  
  
# Driver program to test the above functions 
graph = Graph(9) 
graph.addEdge(0, 1, 4) 
graph.addEdge(0, 7, 8) 
graph.addEdge(1, 2, 8) 
graph.addEdge(1, 7, 11) 
graph.addEdge(2, 3, 7) 
graph.addEdge(2, 8, 2) 
graph.addEdge(2, 5, 4) 
graph.addEdge(3, 4, 9) 
graph.addEdge(3, 5, 14) 
graph.addEdge(4, 5, 10) 
graph.addEdge(5, 6, 2) 
graph.addEdge(6, 7, 1) 
graph.addEdge(6, 8, 6) 
graph.addEdge(7, 8, 7) 
graph.dijkstra(0) 
 
'''
TREE
1.https://www.geeksforgeeks.org/check-given-graph-tree/
'''
#solution
from collections import defaultdict 
  
class Graph(): 
  
    def __init__(self, V): 
        self.V = V 
        self.graph  = defaultdict(list) 
  
    def addEdge(self, v, w): 
        # Add w to v ist. 
        self.graph[v].append(w)  
        # Add v to w list. 
        self.graph[w].append(v)  
  
    # A recursive function that uses visited[]  
    # and parent to detect cycle in subgraph  
    # reachable from vertex v. 
    def isCyclicUtil(self, v, visited, parent): 
  
        # Mark current node as visited 
        visited[v] = True
  
        # Recur for all the vertices adjacent  
        # for this vertex 
        for i in self.graph[v]: 
            # If an adjacent is not visited,  
            # then recur for that adjacent 
            if visited[i] == False: 
                if self.isCyclicUtil(i, visited, v) == True: 
                    return True
  
            # If an adjacent is visited and not  
            # parent of current vertex, then there  
            # is a cycle. 
            elif i != parent: 
                return True
  
        return False
  
    # Returns true if the graph is a tree,  
    # else false. 
    def isTree(self): 
        # Mark all the vertices as not visited  
        # and not part of recursion stack 
        visited = [False] * self.V 
  
        # The call to isCyclicUtil serves multiple  
        # purposes. It returns true if graph reachable  
        # from vertex 0 is cyclcic. It also marks  
        # all vertices reachable from 0. 
        if self.isCyclicUtil(0, visited, -1) == True: 
            return False
  
        # If we find a vertex which is not reachable 
        # from 0 (not marked by isCyclicUtil(),  
        # then we return false 
        for i in range(self.V): 
            if visited[i] == False: 
                return False
  
        return True
  
# Driver program to test above functions 
g1 = Graph(5) 
g1.addEdge(1, 0) 
g1.addEdge(0, 2) 
g1.addEdge(0, 3) 
g1.addEdge(3, 4) 
if g1.isTree() == True :
    print ("Graph is a Tree")

else: 
    print("Graph is a not a Tree")
  
g2 = Graph(5) 
g2.addEdge(1, 0) 
g2.addEdge(0, 2) 
g2.addEdge(2, 1) 
g2.addEdge(0, 3) 
g2.addEdge(3, 4) 
if g2.isTree() == True :
    print ("Graph is a Tree") 

else:
    print("Graph is a not a Tree")


'''
2.https://www.geeksforgeeks.org/print-root-leaf-path-without-using-recursion/

'''
#solution
# Python3 program to Print root to  
# leaf path without using recursion 
  
# Helper function that allocates a new  
# node with the given data and None left  
# and right pointers. 
class newNode: 
    def __init__(self, data):  
        self.data = data  
        self.left = self.right = None
  
# Function to print root to leaf path for a  
# leaf using parent nodes stored in map  
def printTopToBottomPath(curr, parent): 
    stk = []  
  
    # start from leaf node and keep on appending  
    # nodes into stack till root node is reached  
    while (curr): 
        stk.append(curr)  
        curr = parent[curr] 
  
    # Start popping nodes from stack 
    # and print them  
    while len(stk) != 0: 
        curr = stk[-1]  
        stk.pop(-1)  
        print(curr.data, end = " ") 
    print() 
  
# An iterative function to do preorder  
# traversal of binary tree and print  
# root to leaf path without using recursion  
def printRootToLeaf(root): 
      
    # Corner Case  
    if (root == None):  
        return
  
    # Create an empty stack and  
    # append root to it  
    nodeStack = [] 
    nodeStack.append(root)  
  
    # Create a map to store parent  
    # pointers of binary tree nodes  
    parent = {} 
  
    # parent of root is None  
    parent[root] = None
  
    # Pop all items one by one. Do following  
    # for every popped item  
    # a) append its right child and set its   
    #     parent pointer  
    # b) append its left child and set its  
    #     parent pointer  
    # Note that right child is appended first  
    # so that left is processed first  
    while len(nodeStack) != 0: 
          
        # Pop the top item from stack  
        current = nodeStack[-1] 
        nodeStack.pop(-1)  
  
        # If leaf node encountered, print  
        # Top To Bottom path  
        if (not (current.left) and
            not (current.right)):  
            printTopToBottomPath(current, parent)  
  
        # append right & left children of the  
        # popped node to stack. Also set their  
        # parent pointer in the map  
        if (current.right): 
            parent[current.right] = current  
            nodeStack.append(current.right) 
        if (current.left): 
            parent[current.left] = current  
            nodeStack.append(current.left) 
  
# Driver Code 
if __name__ == '__main__': 
      
    # Constructed binary tree is  
    #     10  
    # / \  
    # 8 2  
    # / \ /  
    # 3 5 2      
    root = newNode(10)  
    root.left = newNode(8)  
    root.right = newNode(2)  
    root.left.left = newNode(3)  
    root.left.right = newNode(5)  
    root.right.left = newNode(2)  
  
    printRootToLeaf(root) 