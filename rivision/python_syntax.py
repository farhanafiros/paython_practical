#comment 
print("heelo world")
#variables = a variable is that  stores in values in memory

name  = "alice"
age = 18
price = 190.33
is_student =True

#if /elif/else =condition help paythin makes decition
if age >=18 :
    print("adult")
elif age>=13 :
    print("tenger")
else :
    print("child")


#for loop 
for i in range(5):
    print(i)
#list
fruits = ["apple","orenge","banana"]
for friuts in fruits:
    print(fruits)

#tuple
pair =([1,"a"],[2,"b"],)
for num,char in pair:
    print(num,char)

#set 
colurs ={"red","green","blue"}
for colurs in colurs:
    print(colurs)
#string
text ="hello"
for ch in text:
    print(ch)

#while loop
count = 0
while count <5:
    print(count)
    count += 1
#funtion
def greet(name):
    return "hello," + name
print (greet("alice"))

#list
fruits =["apple","banana","orenge"]
print(fruits[1])

#dictionary
person = {
    "name":"alice",
    "age": 25
}
print (person["name"])

#class 
class person:
    def __init__(self,name):
        self.name=name
    def greet(self):
        print("hello," + self.name)
p=person ("alice")
p.greet()

#arithametic oprators
# adding +
#substraction -
#multipliction *
#division /
#modulas % reminder
#squre expand **
#floor division //

#assingnment opraters
#
#+= 
#-=
#*=
#/=

#comparison oprator 
#== 
#!=
#>
#<
#>=
#<=

# logical opraters
#and true if both conditon are true 
# or true if atleat one codition are true 
# not reverse the result 

#identity oprations 
#is same object 
# is not = diffrent object

#membership oprator
#in value exit 
#not in value does nit exit 

#string 
name = "alice"
print(name)
print(name[3])
print(name[::-1])
age = 20 
print(f"my name is {name}  and i am {age} years old.")
print(name*3)

#list = a list  containr that can storemany values in one vareable
numbers =[1,2,3,4,5,6]
#list index
print (numbers[5])
#list slicing 
print (numbers[::-1])
numbers.append(7)
print(numbers)
#insert =adding a specific position
numbers. insert(7,8)
print (numbers)
# extend
a=[1,2]
b=[3,4]
a.extend(b)
print(a)
#list copmrehension = short and simple way to crate a new list
squre =[]
for num in numbers:
    squre.append(num*num)
print (squre)
#dictionary
student = {
    "name" : "farahana",
   "age": 18
}
student ["corese"]= "paython"
print(student)
del student["age"]
print(student)

#functions = a functon is a reusable block of code a specific task
def add(*args):
    total =0
    for num in args:
        total += num
    return total 

print(add(10,20,30))
#modules and packeges
from math import sqrt ,pi
print(sqrt(25))
