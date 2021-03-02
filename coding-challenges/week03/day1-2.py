'''
Coding challenges
1) Write a Python program to iterate over dictionaries using for loops.
'''
#solution
travel_data = {"Name":"deepak-joshi",
"Age":30,
"Airline":"flying Jaat",
"Class":"Ecnmy",
"Date_of_Travel":"05/10/2020",
"Travel_Time":"1:20 PM",
"Location-from":"delhi",
"Location-to":"uttrakhand"
}

for i,j in travel_data.items():
  print(i,":",j)

input()
'''
2) Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
'''
#solution
num=int(input("Enter a number :"))
dict_dic = {}
for i in range(1,num+1):
    dict_dic[i]=i*i
print(dict_dic)

input()

'''
3) Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string : 'w3resource'
Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
'''
#solution
ip_string = 'w3resource'
count_dict = {}

for char in ip_string:
    count_dict[char] = count_dict.get(char, 0) + 1

print(count_dict)

input()