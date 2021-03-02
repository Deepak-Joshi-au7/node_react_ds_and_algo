'''
1) In python, the size of float and integer is the same in terms of bytes then how is it able to store such large values?
# 
2) How many bits are there in 1GB and 1MB?
'''
#  bits in 1GB
# 1GB = 8,589,934,592 bits # (8*1024*1024*1024) 1 byte = 8 bits , 1kb = 1024 byte , 1mb = 1024 kb , 1gb = 1024 mb ; 

print("1GB has"+ str(8*1024*1024*1024) + "bits")

#  bits in 1MB
# 1MB = 8,388,608 bits # (8*1024*1024) ,1 byte = 8 bits , 1kb = 1024 byte , 1mb = 1024 kb ;

print("1MB has" + str(8*1024*1024) + "bits")

'''
3) write a program that takes input from the user as marks in 5 subjects and assigns a grade according to the following rules:
Perc = (s1+s2+s3+s4+s5)/5.
A, if Perc is 90 or more
B, if Perc is between 70 and 90(not equal to 90)
C, if Perc is between 50 and 70(not equal to 90)
D, if Perc is between 30 and 50(not equal to 90)
E, if Perc is less than 30
'''
# calculate the percentage and assign them accordingly
s1 = int(input("Enter the marks: "))
s2 = int(input("Enter the marks: "))
s3 = int(input("Enter the marks: "))
s4 = int(input("Enter the marks: "))
s5 = int(input("Enter the marks: "))
perc = (s1+s2+s3+s4+s5)/5
if perc >= 90:
    print("A grade")
elif perc >= 70 and perc < 90 :
    print("B")
elif perc >= 50 and perc < 70 :
    print("C")
elif perc >= 30 and perc < 50 :
    print("D")
elif perc < 30 :
    print("E")
else :
    print("invalid perc")   

'''    
4)Build a very basic login system that takes in input from the username password. checks if username is "Priyesh" and password is "password" and responds with:
  Username Doesnot Exist
  Passwords donot match
  Entered the System
'''
Username = input("enter the username: ")
password = input("enter the password: ")
if Username == "priyesh" and password== "password" :
    print("Congratulations!!! You\'re inside the system")
else :
    print("You\'re a FOOL!!!! This is not YOUR PROPERTY")