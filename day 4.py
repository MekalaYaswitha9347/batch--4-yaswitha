
# --------> while loop
# --------> break using while loop


# eg:1
# i = 20
# while i<31:
#     if i==27
#         break
#     print(i)
#     i+=1

# 2.)
i = 20
# while i<31:
#   print(i)
#   i+1
#   if i==27:
#   break'''

# 3.)
# i = 20
# while i<31:
#   print(i)
#   if i ==27: 
#       break
#    i+1
       
# i = 20
# while i<31:
#   if i==27:
#      print(i)
#      break
#    i+1

#  ! --------> continue
# ----> Eg:1
''' i = 20
# while i<31:
#     if  i==27:
#         continue
#     print(i)
#     i=i+1

# i = 20
# while i<31:
#     i=i+1
#     if i==27:
#         continue
#        print(i)'''

# ! Eg:5
# while to iterate from 12 to 22
# find the sum of all numbers
# i =12
# sum=0
# while i<23:
#    sum=sum+i
#    i+=1
#    print(sum)

# ! Eg:6
# i=12
# sum=0
# while i<26:
#    sum=sum+i
#    i+=1
# temp=(sum/5)
# print(temp)

# ! ---------> Nested for loop
# Eg:1
# for row in range(1, 3+1):
#    for col in range(1, 4+1):
#        print(row, col)

# Eg:2
# * * * *
# * * * *
# * * * *
# * * * *

# rows= int(input("enter the rows: "))
# cols=int(input("enter the cols: "))
# for row in range(rows):
#    for col in range(cols):
#    print()

# for row in range(5):
#    for col in range(5):
#        print(row, end=" ")
#    print()

    
#sum =0
# for row in range(5):
#    for col in range(5):
#        sum=sum+1
#        print(sum, end=" ")
#   print()

#! to print stars in right angled triangle


# for row in range(0,6):
# for col in range(0, row):
#       print("*", end=" ")
#       print() 

# for row in range(0,6,-1):
#     for color in range(0,row):
#         print("*", end="")

# for row in range(5):
#   for col in range(5):
#       if col==0 or col==5-1 or row ==0 or row ==5-1:
#           print("*", end=" ")
#        else:
#            print(" ", end=" ")
#   print()

'''for row in range(0,5):
    for col in range(0,6):
        if ((row==0 and col==3) or (row==1 and(col>=2 and col<=4)) or
                                   (row==2 and(col>=1 and col<=5))):
             print("*", end=" ")
        else:
            print(" ",  end=" ")
    print()'''

# ! ----> Datatypes
#primary

# Number ---> int,float complex
#string
#Boolean
#None

#collection
#List
#tuple
#set
#dictionary

# ----> List

# 1.) if the coolection of elements are sourrounded by square brackets, it is to be listed

# ! eg:
   # 11 =[4,7,9,9.89, "hello", 7+9j, [8,9,0]]
    
# * characteristics of list
# 1.) list have to be sourrounded by []
# 2.) It is mutable (elements in the list are changable)
# 3.) Every element inside list is indexed
# 4.) The elements  inside list will be ordered format
# 5.) it can hold duplicative values
# 6.) Its heterogeneous

# To access the elements in list
l1 = [1, 4, 7,89.7, 7.5, "p" "i"]
# print(11)

# --> Indexing
# In the  collection datatypes like, list, tuple, string, The elements will be alloted
# with pre-defined unique value called index value

# we have 2 types of Indexing
# positive indexing --> starts with 0 from left hand side
# Negative indexing --> starts with -1 from right hand side

# ---> positive indexing
# lst1 = [1, 4, 1, 7,89.7, 7.5, "p", "i"]
# print(lst1[0])
# print(lst1[4])
# print(lst1[20]) --> error

# -------> Negative indexing
# lst1 = [1, 4, 1, 7,89.7, 7.5, "p", "i"
# print(lst1[-1])
# print(1st1[-5])

# ----> slicing
lst1 = [1, 4, 1, 7,89.7, 7.5, "p", "i"]
# lst1[start_index:end_index:step]

# print(lst1[0.4])
# print(lst1[6.8])
# print(lst1[3.6])
# print(lst1[:5])
# print(lst1[3:])
# print(lst1[:])

# print(lst1[0:7:1]) # lst1[0:7] --> both are same
# print(lst1[0:7:2])

# trail = int(input())


lst1 = [1, 4, 7,89.7, 7.5, "p", "i"]
# print(lst1[-4:-1])
# print(lst1[-1:-4]) --> []
# print(lst1[-7:-1])
# print(lst1[-7:-1:2])


















  















 


        
   
   
        
     
     















       
