'''
Assignment

1) Write Binary Search using recursion
'''

pos = -1
def binary_search(list,n,lower_bound,upper_bound):
    if lower_bound <= upper_bound:
        mid  =  (lower_bound + upper_bound ) // 2
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        elif list[mid]<n:
            binary_search(list,n,mid+1,upper_bound,)
        else:
            binary_search(list,n,lower_bound,mid-1,)
    return False

list = [4,7,8,12,45,99]
n = 99
Binary_search = binary_search(list,n,0,len(list)-1)
if Binary_search != -1:
    print("Found at", pos+1)
else:
    print("Not Found")