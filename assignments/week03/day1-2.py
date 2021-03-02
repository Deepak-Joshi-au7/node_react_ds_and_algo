'''
Assignments

1)Write a Python program to sort (ascending and descending) a dictionary by value. [use sorted()]
2)Write a Python program to combine two dictionary adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
'''
#ques 1
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
def sorted_dict_increasing(d1):
    sorted_d1 = sorted(d1.items(),key= lambda x: x[1])
    print(sorted_d1)
    sorted_d1 = sorted(d1.items(),key= lambda x: x[1],reverse=True)
    print(sorted_d1)
    return sorted_d1
sorted_dict_increasing(d1)

#   Ques 2
from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
def dict_combine(d1,d2):
    d_combine = Counter(d1) + Counter(d2)
    print(d_combine)
    return d_combine
dict_combine(d1,d2)