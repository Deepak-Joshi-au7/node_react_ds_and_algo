'''
Ques. We have determined the minimum number of operations for a given matrix chain multiplication. Show the sequence it should follow in order to reach this minimum value.
'''
'''
Answer.
'''
import sys 

def MatrixChainOrder(p, i, j): 
  
    if i == j: 
        return 0
  
    mini = sys.maxsize 
     
    for k in range(i, j): 
      
        count = (MatrixChainOrder(p, i, k)  
             + MatrixChainOrder(p, k+1, j) 
                   + p[i-1] * p[k] * p[j]) 
  
        if count < mini: 
            mini = count; 
 
    return mini; 

arr = [1, 2, 3, 4, 5, 6, 3]; 
n = len(arr); 
  
print("Minimum number of multiplications is ", 
                MatrixChainOrder(arr, 1, n-1));


input()