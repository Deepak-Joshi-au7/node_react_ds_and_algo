'''
CC

1) Using the recursive fibonacci number function, print first n fibonacci numbers. (Any Answer containing loops will not be checked)
'''
#solution
def Fibonacci(number): 
    if number<0: 
        print("Incorrect input") 
    elif number==0: 
        return 0
    elif number==1: 
        return 1
    else: 
        return Fibonacci(number-1)+Fibonacci(number-2) 

if __name__ == '__main__':
    number = int(input("Enter The Number : "))
print(Fibonacci(number))

'''
2) https://www.hackerearth.com/practice/basic-programming/recursion/recursion-and-backtracking/practice-problems/algorithm/n-queensrecursion-tutorial/
'''
def printSolution(board):  
    for i in range(size):  
        for j in range(size): 
            print(board[i][j], end = " ") 
        print("\n") 
    print("\n")  
  

def isSafe(board, row, col) : 
    for i in range(col):  
        if (board[row][i]):  
            return False

    i = row
    j = col 
    while i >= 0 and j >= 0: 
        if(board[i][j]): 
            return False; 
        i -= 1
        j -= 1
  

    i = row 
    j = col 
    while j >= 0 and i < size: 
        if(board[i][j]): 
            return False
        i = i + 1
        j = j - 1
  
    return True

def solveNQUtil(board, col) : 
    if (col == size):  
        printSolution(board)  
        return True
  
    res = False
    for i in range(size): 
      
        if (isSafe(board, i, col)):  
            board[i][col] = 1;  
            res = solveNQUtil(board, col + 1) or res;  
            board[i][col] = 0
 
    return res 

def solveNQ(size) : 
    board = [[0 for j in range(10)]  
                for i in range(10)] 
  
    if (solveNQUtil(board, 0) == False):  
      
        print("Solution does not exist")  
        return
    return
if __name__ == '__main__':
    size=int(input("Enter The Size :"))
solveNQ(size) 