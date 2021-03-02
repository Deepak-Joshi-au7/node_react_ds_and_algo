'''
Coding Challenges:

a) https://www.hackerrank.com/challenges/python-string-formatting/problem
'''
#solution
def print_formatted(n):
    w=len(bin(n)[2:])
    for i in range(1,n+1):
        d=str(i)
        o=oct(i)[2:]
        h=(hex(i)[2:]).upper()
        b=bin(i)[2:]
        print(d.rjust(w),o.rjust(w),h.rjust(w),b.rjust(w))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
'''
b) https://www.hackerrank.com/challenges/write-a-function/problem

'''
#solution
def is_leap(year):
    
    if year % 4 != 0:
        leap = False
    elif year % 4 == 0:
        if (year % 100 == 0) and (year % 400 != 0):
            leap = False
        else:
            leap = True
    
    
    return leap

year = int(input())
print(is_leap(year))