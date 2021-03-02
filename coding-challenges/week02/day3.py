'''
1) Using range and for loop, print all multiples of 5, 7, 11 from 1 to 1001 
2) Print multiplication table of 14
 
 
Optional
1)https://www.hackerrank.com/challenges/text-alignment/problem
'''
# Ques 1 for sample
for n in range(0,1000) :
    multiply_5 = n * 5
    if multiply_5 <  1001 :
        print("5 multiply by",n,"is equal to",multiply_5)
    else :
        break
for n in range(0,1000) :
    multiply_7 =  n*7
    if multiply_7 < 1001 :
        print("7 multiply by",n,"is equal to",multiply_7)
    else :
        break   
for n in range(0,1000) :
    multiply_11 =  n * 11
    if multiply_11 < 1001 :
        print("11 multiply by",n,"is equal to",multiply_11)
    else :
        break

# ques no 3.
# multiples of 14
for n in range(1,11) :
    multiply_14 =  14 * n
    if multiply_14 < 141 :
        print("14 * ",n," = ",multiply_14)
    else :
        break