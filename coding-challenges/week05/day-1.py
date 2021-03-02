'''
CC's

1) Is merge sort stable, inplace and find its time complexity?
'''
#answer
'''
Merge Sort, algorithm is stable by nature.
A sorting algorithm is said to be stable if two objects with equal keys appear in the same order in sorted output as they appear in the input array to be sorted. 
Time Complexity: 

Sorting arrays on different machines. 

Merge Sort is a recursive algorithm and time complexity can be expressed as following recurrence relation.

T (n) = 2T (n/2) + O (n)

The above recurrence can be solved either using Recurrence Tree method or Master method. 

It falls in case II of Master Method and solution of the recurrence is O (nLogn).
.
Time complexity of Merge Sort is O (nLogn) in all 3 cases (worst, average and best) as merge sort always divides the array into two halves and take linear time to merge two halves.

Auxiliary Space: O (n)
Algorithmic Paradigm: Divide and Conquer
Sorting In Place: No in a typical implementation
Stable: Yes
'''
'''
2) Write a python program to do merge sort iteratively.
'''
#solution
def mergeSort(arr):   
    current_size = 1
    while current_size < len(arr) - 1:   
        left = 0
        while left < len(arr)-1: 
            mid = left + current_size - 1
            right = ((2 * current_size + left - 1, 
                    len(arr) - 1)[2 * current_size  
                          + left - 1 > len(arr)-1]) 
            merge(arr, left, mid, right) 
            left = left + current_size*2
        current_size = 2 * current_size
      

def merge(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r - m 
    L = [0] * n1 
    R = [0] * n2 
    for i in range(0, n1): 
        L[i] = arr[l + i] 
    for i in range(0, n2): 
        R[i] = arr[m + i + 1] 
  
    i, j, k = 0, 0, l 
    while i < n1 and j < n2: 
        if L[i] > R[j]: 
            arr[k] = R[j] 
            j += 1
        else: 
            arr[k] = L[i] 
            i += 1
        k += 1
  
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
  
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1

arr = [70,50,30,10,20,40,60]
print("Given array is  :",arr)
print("\n") 
mergeSort(arr) 
print("Sorted array is :",arr)

input()

'''
3) Explain merge sort with [70,50,30,10,20,40,60] in 100 words.
'''
#solution
def merge(left, right):
    if not len(left) or not len(right):
        return left or right
 
    result = []
    i, j = 0, 0
    while (len(result) < len(left) + len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i+= 1
        else:
            result.append(right[j])
            j+= 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break
 
    return result
 
def merge_sort(arr):
    if len(arr) < 2:
        return arr
 
    middle = len(arr)//2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
 
    return merge(left, right)
     
arr = [70,50,30,10,20,40,60]
print("Given array is  :"  ,arr); 
print("\n")
print("Sorted array is :" ,merge_sort(arr))

input()