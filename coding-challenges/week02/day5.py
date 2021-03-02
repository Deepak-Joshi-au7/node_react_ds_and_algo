'''
1) Another sorting method, the counting sort, does not require comparison. Instead, you create an integer array whose index range covers the entire range of values in your array to sort. 
Each time a value occurs in the original array, you increment the counter at that index. 
At the end, run through your counting array, printing the value of each non-zero valued index that number of times.
For example, consider an array . All of the values are in the range , so create an array of zeroes, . 
The results of each iteration follow:
i    arr[i]    result
0    1    [0, 1, 0, 0]
1    1    [0, 2, 0, 0]
2    3    [0, 2, 0, 1]
3    2    [0, 2, 1, 1]
4    1    [0, 3, 1, 1]
Now we can print the list of occurrences,0 3 1 1  or determine the sorted array: sorted = [1,1,1,2,3]
[Hint: Think in terms of space] 
'''
# solution
def counting_sort(array1, max_val):
    m = max_val + 1
    count = [0] * m                
    
    for i in array1:
        count[i] += 1             
    a = 0
    for i in range(m):            
        for j in range(count[i]):  
            array1[a] = i
            a += 1
    return array1


array_value=[2, 4, 6, 19, 21, 14, 5, 3, 10, 17, 13]
print("Array to be Sorted :",array_value)
max_val = 21
sorted_array=counting_sort(array_value,max_val)
print("Sorted Array       :", sorted_array)


input("")
'''
2) As you can see this code is much faster than selection sort. (it has no nested loop) 
What do you think is the reason this is not very widely used?
'''
#solution
Disadvantages of Counting Sort:
    • It is not suitable for sorting large data sets
    • It is not suitable for sorting string values
    • if non-primitive (object) elements are sorted, another helper array is needed to store the sorted elements. Second and the major disadvantage is that counting sort can be used only to sort discrete values, because otherwise the array of frequencies cannot be constructed.
    • Thus space complexity becomes O(k). Hence for a very large range of numbers, counting sort requires a very large array. This reduces its memory efficiency and increase space consumption. Hence it’s not a good choice for sorting a large range of numbers.
    • Restricted inputs. Counting sort only works when the range of potential items in the input is known ahead of time.
    • Space cost. If the range of potential values is big, then counting sort requires a lot of space (perhaps more than O(n)O(n)).