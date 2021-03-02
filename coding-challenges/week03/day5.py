'''
Coding Challenges:

1)Given a sorted array and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order. 
[You may assume no duplicates in the array.]

[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
'''
#solution
def find_index(n,list_of_item):

    if n in list_of_item :
       print ("Index Number where the item is Present:",list_of_item.index(n))
    else :
      list_of_item.append(n)
      list_of_item=sorted(list_of_item)
      print("The Number Not Present In List")
      print("Index Number where the item Should Be Present :",list_of_item.index(n))
    
    
list_of_item = [1,3,5,6]
print("The Given List :" , list_of_item)
n=int(input("Enter the Number:"))
find_index(n,list_of_item)

'''
2) Optimize the counting sort algorithm.
'''
#solution
def counting_sort(array1, max_val):
    m = max_val + 1
    count = [0] * m                
    
    for a in array1:
        count[a] += 1             
    i = 0
    for a in range(m):            
        for c in range(count[a]):  
            array1[i] = a
            i += 1
    return array1


array_value=[1, 17, 2, 15, 11, 3, 4, 16, 8, 4, 23]
print("Array to be Sorted :",array_value)
max_val=23
sorted_array=counting_sort(array_value,max_val)
print("Sorted Array       :", sorted_array)