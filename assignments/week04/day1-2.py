'''
Assignments

1) https://www.hackerrank.com/challenges/countingsort4/problem
'''
#counting sort
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(arr,n):
    count = 0
    count_sort = 0
    sorted_arr = list()
    string = ''
    for items in arr:
        if int(items[0]) > int(count_sort):
            count_sort = int(items[0])
        if count < n/2:      
            items[1] ='-'  
            count += 1
    for i in range(0,count_sort+1):
        sorted_arr.append([])
    for items in arr:
        sorted_arr[int(items[0])].append(items[1])
    for i in sorted_arr:
        for j in i:
            string += j+' '
    print(string)


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

countSort(arr,n)