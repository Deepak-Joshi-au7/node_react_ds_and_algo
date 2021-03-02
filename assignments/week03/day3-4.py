'''
Assignment:

c) https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
d) https://www.hackerrank.com/challenges/list-comprehensions/problem
'''
# Ques (c)
# find second maximum number
def runner_up(n,arr):
    if n == 0 :
        return false
    else:
        sorted_arr = sorted(arr,reverse = -1)
        for i in range(len(sorted_arr)):
            if sorted_arr[i] != sorted_arr[i+1]:
                print (sorted_arr[i+1])
                break
            else:
                continue
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
runner_up(n,arr)
# Ques (d)
# list-comprehensions
def list_comprehension(x,y,z):
    arr = list([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if ((i+j+k) != n)])
    print(arr)
list_comprehension(x,y,z)
