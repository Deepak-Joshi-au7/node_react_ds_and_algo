'''
Assignments:

1) Given a sorted array of integers A(0 based index) of size N, find the starting and ending position of a given integer B in array A.
Your algorithm runtime complexity must be in the order of O(log n). Return an array of size 2, such that first element = starting position of B in A and second element = ending position of B in A, if B is not found in A return [-1, -1].

Input 1:
    A = [5, 7, 7, 8, 8, 10]
    B = 8
Output 1:
    [3, 4]
Explanation 1:
    First occurence of 8 in A is at index 3
    Second occurence of 8 in A is at index 4
    ans = [3, 4]

Input 2:
    A = [5, 17, 100, 111]
    B = 3
Output 2:
    [-1, -1]

2) Write the code for binary search without using loops. [optional]
'''
# Question 1
#  Return an array of size 2, such that first element = starting position of B in A and second element = ending position of B in A, if B is not found in A return [-1, -1].
# A = [5, 7, 7, 8, 8, 10]
# B = 8
# def index_position(A,B):
#     arr = [i for i in range(len(A)) if A[i] == B]
#     print([arr[0],arr[-1]])
#     for j in A:
#         c = 0
#         if j == B:
            
# index_position(A,B)

#ques 2
pos = -1
def search(list,n):
    lower_bound = 0
    upper_bound = len(list)-1
    while lower_bound <= upper_bound:
        mid  =  (lower_bound + upper_bound ) // 2
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else : 
            if list[mid]<n:
                lower_bound = mid+1;
            else:
                upper_bound = mid-1;    
    return False

list = [4,7,8,12,45,99]
n = 99
if search(list,n):
    print("Found at", pos+1)
else:
    print("Not Found")