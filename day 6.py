'''s1 =input("enter the string")
s1 =s1 [0:1].upper()+sl[1:len(sl(sl)-l) +s1[len]]
print(sl)'''

'''sl = input("enter string: ")
fst = sl[0].upper()
lst = sl[-1].upper()
print(fst+sl[1:len(sl)-1]+lst)'''

'''n = 128
temp = n
f1 = 0
while n!=0:
    rem = n%10
    check= temp % rem
    if check!=0:
         f1 =1
    n = n//10

if f1==0:
    print("yes")
else:
    print("no")'''

'''l1 = [8, 9, 0, 7]
l2 = [7, 6, 5, 4]
l3 =[]
for val in range(len(l1)):
    ans = l1[val]+l2[val]
    l3.append(ans)
print(l3)'''

# ! ---------> set

# characteristics of set
'''1.) set can be created using {}
2.) the elements inside set are not allowed
3.) does not allow duplicate values
4.) it unordered
5.) heterogenous
6.) mutable or changable'''

# Eg:1
'''sl = {9, 9, 89, 7.76, 8+7j, (8, 7, 5), "truck", 'e'}
print(s1)'''

# * Eg:2
'''s2 = {5, 8, 98, [9, 0]}
print(s2) --> error'''

# * Eg:3
# min(), max(), len()

# * eg
# to add element inside set

'''s1 = {8, 78, 67, 'u'}
add()
sl.add(43)
print(sl)'''

# update()
'''sl.update([9, 0])
print(sl)'''

# To delete element inside set
# sl={8, 78, 67, 'u'}

# pop() # to delete one element randomly
'''sl.pop()
print(sl)'''

# remove()
'''sl.remove(978)
print(sl)'''

# discard()
'''sl.discard(67)
print(sl)'''

# clear()
'''l1 = {}
print(type(l1)) --> data type is dict'''

# sl = set() # to create empty set
# print(type(sl))

# sl = {8, 9, 0}
'''sl.clear()
print(sl)'''

# del sl
# print(sl)

# * join the sets
'''s1 = {9, 0, 8}
s2 = {9.90, "card", 't', 56}
# # union() --> to combine 2 sets
s3 = sl.union(s2)
print(s3)'''

# * intersection() --> to get common elements inside set
'''s1 = {4, 5, 6}
s2 = {5, 6, 7, 8}
print(s1.intersection(s2))'''

# * difference()
'''s1 = {4, 5, 6}
s2 = {5, 6, 7, 8}
print(s1.difference(s2))
print(s2.difference(s1))
print(s1.symmetric_difference(s2))

# isdisjoit(), issubset(), issubset()
# s1 = {8, 9, 0}
# s2 = {6, 7, 5, 8, 9, 0}

# print(s1.issubset(s2))
# print(s2.issuperset(s1))'''

'''s1 = {1,2,3,4,5}
s2 = {3,2,7,8,9}'''

# n1 = {1, 2, 3} --> s1

'''for val in s1:
    if val in s2:
        str = "Its joint set"
print(str1)'''

# ! --------> dictionary
# eg:1
'''d1 = {1:100, 'a':200, 4.5:"hello"}
print(d1)
print(len(d1))'''

# char of dictionary
'''1.) have to be surrounded by {}
2.) it have to be in the form of key, value pair
3.) it is mutable
4.) duplicate keys are not allowed, duplicate values are allowed
5.) it is unindexed
6.) it is ordered
7.) key does not allow mutable datatypes, values allow mutable datatype'''

d1 = {1:100, 2:200, 3:300, 4:400}
# * to access element in dictionary

'''print(d1)
or
To access the values, have to use key
print(d1[1]) # o/p --> 100'''

# some common functions
'''len(), min(), max()
print(min(d1))
print(max(d1))'''

# To find min, max based functions
# to add element(key and value pair) in dict
'''d1 = {1:100, 2:200, 3:300, 4:400}
d1[5] = 500
print(d1)'''

# To replace a value in dictionary
'''d1 = {1:100, 2:200, 3:300, 4:400}
d1[2]="mango"
print(d1)'''

# delete element from dictionary
'''d1 = {1:100, 2:200, 3:300, 4:400}
popitem() # ----> to delete last key value pair in dict
d1.popitem()
print(d1) '''

# pop()
'''d1.pop(2) # 2 is the key in dictionary
print(d1)'''

# clear(), del

#join 2 dictionary
# update()
'''d1 = {1:100, 2:200, 3:300, 4:400}
d2 = {"a":"apple", "b":"boy", "g":"game"}
d1.update(d2)
print(d1)'''

# get() ------> used to get the value from a key
'''d1 = {1:100, 2:200, 3:300, 4:400}
print(d1[90])
print(d1.get(90))'''

# to print all the keys
'''print(d1.keys())
print(type(d1.values()))'''

# * Iterating dictionary
'''for val in d1: # to iterate keys alone
    print(val)'''

'''for val in d1.values(): # to iterate values alone
    print(val)'''

# # to get both key and values
'''for key, val in d1.items():
    print(key, val)'''

# ! problem:1

'''n = int(input("enter num of times : " ))
integer=[]
float_value =[]
string=[]

for val in range(n):
    value = eval(input("enter the values: "))
    if type(val)==int:
        integer.append(value)
    elif type(value) == float:
        float_value.append(value)
    elif type(value) == str:
        string.append(value)
    else:
       print("pls provide data in int, float, string")
print(integer)
print(float_value)
print(string)    '''
# -----> problem 2
'''set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set3 = set()
for val in set1:
    if val not in set2:
        set3.add(val)
for val in set2:
    if val not in set1:
        set3.add(val)
print(set3)'''
        
# ! --------> problem 3
l1 = [1,2,3,4] # key
l2 = ["a", "b", "c", "d"] # value        

d1= {}
for val in range(len(l1)):
    d1[l1[val]] = l2[val]
    print(d1)
    























































