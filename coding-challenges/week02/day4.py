'''
CC- Week-02 - Day-04                                                                                                                                                                                                                                   1) Write a program to find greatest common divisor (GCD) or highest common factor (HCF) of given two numbers.
1) Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ). Print average and product of all numbers.
2) Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
3) Write a Python function that takes a number as a parameter and check the number is prime or not.
'''
# QUes 1.
def q_rolePlay(intger) :
    while True:
        intger = input("enter the number: ")
        if intger == 'q' :
            break
        else :
            continue
        print('press Q to quit')
        return q
    print("done")
q_rolePlay(24)

# ques 2
string = input("enter the character: ")
def count_case(string):
    count_lower = 0
    count_upper = 0
    for i in string:
        if (i.islower()):
            count_lower = count_lower + 1
        elif(i.isupper()):
            count_upper = count_upper + 1
        else:
            print("only string character allowed")
    print("the number of lowercase is: " ,count_lower)
    print("the number of uppercase is: " ,count_upper)
count_case(string)

#QUes 3
number = int(input("enter the number: "))
def prime_number(number):
    if number > 1 :
        for i in range(2,number):
            if (number % i) == 0 :
                print(number ," is not a prime number")
                print(i ,"times ",number//i,"is ", number)
                break
        else:
            print(number ," is a prime number")
    else:
        print(number ," is not a prime number")
prime_number(number)