# name=input("enter the name")
# age=int(input("enter the age:"))
# national=input("enter the nation:")

# if age>=18 and nationality=="Indian":
#    print("eligible for vote")
# else:
#    print("not eligible")
 
# from user and check if it is square or not.

# length= int(input())
# breadth= int(input())
# if length==breadth:
#    print("itsa square")
# else:
# print("its not square")


#! Eg:4
# python program to check whether the
# given integer is a multiple of both 5 and 7


# char=int(input("enter the number:"))
# if n%5==0 and n%7==0:

#     print("yes")
# else:
#   print("no")


# !Eg:5
# write a program to accept the cost price of a bike and display the
# road tax to be paid
# according to the following criteria:

#         cost price (in Rs)
#         >100000
#         >50000 and <=100000
#        <=50000


# price = int(input("enter the price:"))
#  amount = 0
# if price>=100000:
#    discount =price*(6/100)
#    value=price-discount
#    tax=value*(15/100)
#    total=value+tax
# else:
#    tax=price*(51/100)
#   total=price+tax
# print("The onroad cost of bike is: ",total)

#! Eg:6
# Accent The age of 4 people and display the oldest one
# !---------> if elif else
# Eg:1
# a=7
# b=9
# c=30
# elif b>a and b>c:
#   print("B is greater")
# elif c>a and c>b:
#    print("c is greater")

# A school has following rules for grading system:
# a. Below 25 -F
# b. 25 to 45 -E
# c. 45 to 50-D
# d. 50 to 60-c
# e. 60 to 80-B
# if. Above 80-A
# Ask user to enter marks and print the corresponding grade.
# mark=int(input("Enter mark:"))
# if  mark>=80 and mark<=100:
#   print("A")
# elif mark>=60 and mark<=80:
#         print("B")
# elif mark>=50 and mark<=60:
#      print("C")
# elif mark>=40 and mark<=50:
#  (print("D")
# else:
# print("Fail")


#  Eg:6
# Acccept the age of 4 people and display
     
# ! ---> short hand if else
# Eg:1
# a=90
# b=60
# if a>b:
#  print("A")
# else:
# --> using short hand if else

# 1.)statement inside the if condition have to be prsent at first  #2.)elif cannot be used in short hand if else  #3.)Always it have to end with else
# print("A") if a>b else print ("B")

# !code to check the given char is vowel or consonent
# char= input("Enter the char:"

# ! ---> elif ladder using short hand if else
# Eg:1
#  find greatest among 3 variables using short hand if else 
# a= 8
# b=5
# c=9

# print("A is greater") if a>b and a>c else print("B is greater")
# if a<b and b<c else print ("c is greater")

# ! --------------> looping

# looping can be implemented using
# for loop
# while loop

# ! ----> for loop
# for loop is used for iteration, if we know the number of times the loop have
# it is used to iterate the iterables eg(string,list,tuple,etc...)

# todo ---> syntax for loop

# ! for syntax in c
# for(i=0;i<10,i++){
#     printf("hello");
# }

# ! for syntax in python
# for userdefined_variable in range(start, end, step value is 1
#     statement
#     statement
#     statement

#  Eg:1
# To print the value from 1 to 10 using for loop

# for i in range(0,10): #(n, n-1)
#      # print(i)
#      print("hello")

#  Eg:2
# for val in range(1, 15, 2):
#     print(val)

# for val in range(1, 15, 3):
#     print(val)

#  Eg:3
# to decrement the value

# for val in range(10, 0, -1):
    # print(val)

# for val in range(10, 0 -2):
#     print(val)

# for val in range(10, 0, 1);
#     print val # no output

# Eg:4
# ! print the output of 7th multiplication table from 21 t0 43
for val in range(1, 10+1):
    # print('7','x',val,'=',val*7
#     ---> method:1

 # --> method:2
    # ans="7 x {} = {}"
    # print(ans.format(val, val*7))

 # ---> method:3
      print(f"7 x {val}={val*7}")

# Eg:5
# break ---> used to teerminate the loop

for val in range(1,10):
    print(val)
    if val ==6:
       break 
      
# Eg:6
# for val in range(1,10):
#     print(val)
#     if val ==6;
#        break

# Eg:7
# for val in range(1,10):
#     if val ==6:
#        print(val)
#        break

# ! continue
# Eg:1
for val in range(1,10):
    if val ==6:
       continue
    print(val)
for val in range(1,30):
    if val==6 or val==8 or val ==21:
        continue
    print(val)
    
# ! practise problems
#   print the even number between 20 to 40
'''for val in range(21,40):
    if val&2==0:
        print(val)'''

#!-----------> while loop
# while is used when we do not know the number of times the loop have too
# to iterate the non iterable elements while loop is used

# todo syntax

# initialisation
#while condition:
#    statement
#    incre or decre

#! Eg:1
# to iterate number from 1 to 10

i=0
while i<11:
     print(i)
     i=i+1 # OR I+=1
    

i=10
while i>0:
     print(i)
     i=i-1 # OR I+=1
    






    
    





             

     
 
     



     
     
    




























    






























    



