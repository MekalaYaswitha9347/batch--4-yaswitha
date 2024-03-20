# 2.) Find the uncommon words from 2 strings
'''sl = "Hello how are you"
s2 = "Hello how is"

s1 = "Hello how are you"
s2 = "Hello how is"

s1 = s1.split(" ")
s2 = s2.split(" ")

for val in s1:
    if val not in s2:
        print(val)
for val in s2:
    if val not in s1:
        print(val)'''

#3.)Find the 8th fibanochi number
'''num = 8
n1 = 0
n2 = 1

for val in range(num):
    ans= n1+n2
    n1 = n2
    n2 = ans
print(ans)'''

# ! constructors
# Eg:2
# * unparametarised constructor
'''class profile:
    def _init_(self):
        print("hello world")

obj = profile()
obj._init_()'''

# Eg: 3
# * parametarised constructor
'''class profile:
    def_init_(self, id, name, age):
        print(id, name, age)
obj = profile(1, "sid", 29)'''

# Eg:4
'''class c1:
    email = "yasta@gmail.com"

    def m1(self):
        name = "yasta"
        place= "cbe"
        print(name, place)
        print(self.email)

object= c1()
object.m1()'''

# Eg:5
'''class c1:
    def m1(self):
        name = "yasta"
        age = 21
        return name, age
def display(self):
    # ! print(name, age)
    # ! print(self.name, self.age)
    print(self.m1())

object = c1()
object.display()'''

# Eg:6
# To use the variable  inside the constructor in another  methods
# class class1:
   #  email = "yasta@gmail.com"  #static variable
'''def_init_(self):
        self.name = "yasta"  # instance variable
        self.email = "yasta@gmail.com"
        # return name, email # error ---> cannot use return with  constructor

def display(self): # instance method
    print(self.name, self.email)

c1 = class1()
c1.display()'''

# ! ----------> Inheritence
# The process of utilising the methods and attributes of parent class
# throught the object of child class it is called as inheritance

# 5 types of Inheritence
'''single Inheritence
multi level Inheritance
multiple Inheritance
Hybrid Inheritence
Heirarichal inheritence'''

# * single Inheritence
# It has only one parent class and only one child class
# ! Eg:1
'''class parent:
   def m1():
       print("Iam parent class")

class child(parnt):
    def m2(self):
        print("Iam child class")

obj = child()
obj.m1()'''

# ! Eg:2
'''class c1:
    def __init__(self):
        print("Iam constructor from parent class")
class child1(c1):
            pass
obj= child()'''

# ! Eg:3
'''class parent:
    name = "sidhu"

class child(parent):
    name = "name1"

    def display(self):
        print(self.name)

d = child()
d.display()'''

# ! multilevel inheritence
# Eg:1
'''class voice:
    def sound(self):
        print("All the animals have their own voices")

class dog(voice):
    def dog_voice(self):
        print("bark")

class cat(dog):
    def cat_voice(self):
        print("meow")

class parrot(cat):
    def parrot_voice(self):
        print("speak")

all = parrot()
all.dog_voice()
all.cat_voice()
all.sound()
all.parrot_voice()'''

# ! multiple inheritance
# it has multiple parent and 1 child      

'''class while_petrol:
    def function_w(self):
        print("used to airplanes")

class organic_petrol:
    def function_p(self):
        print("used for bike, cars")

class premium_petrol:
    def function_p(self):
        print("spots cars, bikes")

class petrol(while_petrol, organic_petrol, premium_petrol):
    def definition(self):
        print("petrols types")

p= petrol
p.definition()
p.function_o()'''

# ! Eg:2
'''class addition:
    def add(self, a, b):
        print(a+b)
class subtract:
    def sub(self, a, b):
        print(a-b)
class multiply:
    def mul(self, a, b):
        print(a*b)
class division(addition, subtract, multiply):
    def div(self, a, b):
        print(a/b)

calc = division()
# calc.add(3,4)
calc.mul(4,2)'''

# ! Heirarical inheritence
# ! The one parent class will act a parent for all the child classes
'''class category:
    def weight(self,weight):
        print(weight)

    def display(self, color, taste):
        print(weight)

class Tomato(category):
    def tomato_specs(self):
        color="black"
        taste = "neutral taste"
        self.display(color, taste)

class carrot(category):
    def carrot_specs(self):
        color="green"
        taste = "sweet"
        self.display(color, taste)

c = carrot()
c.carrot_specs()
c.weight("30gms")

t = tomato()
t.tomato_specs()
t.weight("20gms")'''
    
# ! Hybrid inheritance
# The combination of above 4 inheritance is called Hybrid inheritance
'''class c1:
    def m1(self):
        print("class 1")

class c2(c1):
    def m2(self):
        print("class2")

class c3(c2):
    def m3(self):
        print("class 3")
    
class c4(c3):
    def m4 (self):
        print("iam m3 from c4")

class c5(c4):
    def m5 (self):
        print("class 4")

class c6(c3,c5):
    def m6(self):
        print("class 4")
obj = c6()
obj.m3()'''

# ! --------------> polymorphism
# poly - many, morph --> form
# A  function which has the ability to perform more than 1 functionality
# then it is considered to be as polymorphism

# * polymorphism in buttton functions
# len() ---> which is used to find the length of list, tuple, dict etc
# index()
#max()
#min()
#count()
#pop()
# and more...

# * polymorphism in operators
# +
# print(8+8)
# print("k+'1')
# print([1,2,3]+[5,6])

# *
'''print(6*7)
l1 = {12,3,4,5,6}
print(*l1)
def f1(*args)
l1 = [1,2,3,4]
print(l1*10)'''

# polymorphism in classes
# we can achieve polymorphism in 2 ways
# 1.) method overloading --> it is not possible in python
# 2.) method overriding












