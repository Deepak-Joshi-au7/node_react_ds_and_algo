'''
CC-
1) https://www.hackerrank.com/challenges/magic-square-forming/problem
'''
#solution
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    sq = [[[8,1,6],[3,5,7],[4,9,2]],
             [[6,1,8],[7,5,3],[2,9,4]],
             [[4,9,2],[3,5,7],[8,1,6]],
             [[2,9,4],[7,5,3],[6,1,8]],
             [[8,3,4],[1,5,9],[6,7,2]],
             [[4,3,8],[9,5,1],[2,7,6]],
             [[6,7,2],[1,5,9],[8,3,4]],
             [[2,7,6],[9,5,1],[4,3,8]]]
    cost_list = []
    for c in sq:
        cost = 0
        for i in range(3):
            for j in range(3):
                cost += abs(c[i][j]-s[i][j])
        cost_list.append(cost)
    return min(cost_list)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()

'''
2) https://www.hackerrank.com/challenges/lisa-workbook/problem
'''
#solution
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the workbook function below.
def workbook(n, k, arr):
    num=0 
    p_num=0 
    i=0
    j=0
    s_prob=0
    
    while num<len(arr):
        
        j=i+1
        p_num+=1

        if i+k>arr[num]:
           i=arr[num]
        else:
            i+=k

        if p_num<=i and p_num>=j:
            spl_prob+=1
        
        if i==arr[num]:
            num+=1
            i=0
            j=0
    
    return s_prob

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()