'''
Assignment:
https://www.geeksforgeeks.org/find-number-pairs-xy-yx/ 

HW-Optional

Encapsulation: It describes the idea of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data.
Abstraction:  Abstraction is selecting data from a larger pool to show only the relevant details to the object. It helps to reduce programming complexity and effort.
Inheritance: Inheritance is one of the core concepts of object-oriented programming (OOP) languages. It is a mechanism where you can to derive a class from another class for a hierarchy of classes that share a set of attributes and methods.
getattr(obj, name[, default]) - gets the value of a specific attribute of the object. 
__doc__()
hasattr(obj, name) - returns true, false
setattr(obj, name, value) - changes a particular attribute value of an object. 
delattr(obj, name) - deletes  particular attribute value of an object. 
'''
import bisect  
def count(x, Y, n, NoOfY):  
    if x == 0: 
        return 0
    if x == 1: 
        return NoOfY[0] 
    idx = bisect.bisect_right(Y, x) 
    ans = n - idx 
    ans += NoOfY[0] + NoOfY[1] 
   
    if x == 2: 
        ans -= NoOfY[3] + NoOfY[4] 

    if x == 3: 
        ans += NoOfY[2] 
  
    return ans 

def count_pairs(X, Y, m, n): 
    NoOfY = [0] * 5
    for i in range(n): 
        if Y[i] < 5: 
            NoOfY[Y[i]] += 1
    Y.sort() 
    total_pairs = 0
  
    for x in X: 
        total_pairs += count(x, Y, n, NoOfY) 
  
    return total_pairs 

if __name__ == '__main__': 
  
    X = [2, 1, 6] 
    Y = [1, 5] 
    print("Total pairs = ",  
           count_pairs(X, Y, len(X), len(Y)))

input()