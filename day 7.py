#Assessment
#p1:
'''dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict1.update(dict2)
print(dict1)'''
#p2:
'''set1 = {'Python', 'Java', 'Data Science'}
set2 = {'ML', 'AI', 'R Language', 'Python'}
set3 = {'Data Analytics', 'Robotics', 'Deep Learning'}
for i in set1:
    if i not in set2:
        print('yes')
    else:
        print('no')
for i in set1:
    if i not in set3:
        print('yes')
    else:
        print('no')
for i in set2:
    if i not in set1:
         print('yes')
    else:
        print('no')
for i in set2:
    if i not in set3:
         print('yes')
    else:
        print('no')
for i in set3:
    if i not in set1:
         print('yes')
    else:
        print('no')
for i in set3:
    if i not in set2:
         print('yes')
    else:
        print('no')'''
'''for i in  range(3):
   c=c+1
if c==1:
       for val in set1:
          if val in set2 or val in set3:
             flag=1
             break'''
'''if c==2:
   for val in set2:
      if val in set2 or val in set3:
         flag=1
      break  '''
'''if flag==0:
   print("Disjoint")
else:
   print("joint")'''
      
'''#p3
l1 = ["M", "na", "i", "Ke"]
l2 = ["y", "me", "s", "lly"]

l3=[]
i=0
for i in range (len(l1)):
    s=l1[i]+l2[i]
    l3.append(s)
print(l3) '''
    
'''i=0
while i<len(list1):
   l3.append(list1[i]+list2[i])
   i+=1
print(l3)'''

# ! Functions
# DEF
# Function is a block of code which is used to perform a specific functionality
# Function can be created using def keyword

# Function has  3 parts
# Function declaration
# Function definition
# Function call

# Eg:1
'''def greet():  
   print("Greetings User!!")

 greet()
 greet()
 greet()
 greet()
 greet()
 greet()
 greet() # function calling'''
 
# ! Eg:2
# function with parameter
'''def greeting(name):
   print("welcome", name)
for val in range(3):
   username = input("Enter the name: ")
   greeting(username) # username is argument'''

# for val in range(3):
       username = input("Enter the name: ")
      greeting(username) # username is argument







 











      \



