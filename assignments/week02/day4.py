# Assignments
# 1) Write a program to find greatest common divisor (GCD) or highest common factor (HCF) of given two numbers.

# Greatest Common Divisor
x = int(input("enter First number: "))
y = int(input("Enter Second number: "))
def gcd(x,y):
    gcd = 1
    if x % y == 0:
        return y
    for k in range(int(y/2), 0 ,-1):
        if x %  k == 0 and y % k == 0:
            gcd = k
            break
    return gcd

print(gcd(x,y))

# Highest Common Factor
def hcf(x,y):
    hcf = 0
    smaller = 0
    if x > y:
        smaller = y
    else:
        smaller = x
        for i in range(1,smaller+1):
            if (x%i== 0)and (y%i==0):
                hcf = i
    return hcf

print(hcf(x,y))