## Topic01 Python Get Started


#Q1= What is the  correct file extension for python file?
# .py✅
#.pp
# .pyt
#.pp

# Answer is .py

# Q2= What is the correcr command line syntax for checking if installed on your conputer? and alse to check the python version?
# python --version ✅
# python --ver
# python --verion   
# python ## version

# Answer is python --version

# Q3= What is a correct syntax to exit the python command line interface?
# exit() ✅
# stop()
# quit()

#Answer is exit()

# print("Before exit")
# x = 45
# exit(x)
# print("This will not print")
# solve
# print("This will print")
# x=True
# exit(x)
# print("This will not print")


# Q4= True or False :Indentation in Python is for readability only.
# False ✅
# True

# Answer is False
# Python requires indentation to define blocks

x = 5
if x > 0:
    # this line is indented — it's part of the "if" block
    print("x is positive")
# this line is outside the block
print("This line runs regardless of the if condition")

#Q5= Complete the code block print "YES" if 5 is greater than 2,  Hint rember the indentation in python.

if  5 > 2:
    print("YES") #✅
#Answer is print("YES")

## Topic 02 Python Comments

# Q1= Which character is used to define a python comment?
# # ✅
# !
# *
# /
#Answer is #

# Q2= Comments in python are written with a special character which one?
# # ✅
# @ 
# !
# *
#Answer is #
# Q3= Use a multiline string to make the a mutiline comment.
# Answer is 
"""
Hello,
This is a comment.
This is a multiline comment.
"""

# Q4= True or False: Comments are not executed by the interpreter.
# True ✅
# False
# Answer is True


## Topic 03 Python Variables

# Q1= What is a correct way to create a variable in python?
# var  x = 5 
# var 5 =
# $var = 5
# #var = 5
# x = 5 ✅

# Answer is x = 5

# solve

y :int = 5
print(y)

#Q2 =True or False:
# You can declare string variable with single or doubles quoteas
# True ✅
# False
# Answer is True
#solve
# x= "Azeez"
# x='Azeez'
# print(x)

#Q3 = What is the correct way to declare a variable that is not case sensitive?
# var = "Hello"
# Var = "Hello"
# VAR = "Hello"
# all of the above ✅
# Answer is all of the above
# solve
# x = "Hello"
# X = "Hello"
# X = "Hello"
# print(x)
# print(X)
# print(X)

# Q5 = Select the correct function to print the datatype of a variable in python.


#print(type(my_var))✅
#print(datatype(my_var))

my_var =5.0
print(type(my_var)) # ✅

#Q6= Whic is not a legal variable name in python?
#1name="John"✅
# name1="John"
# name_1="John"
# _name="John"
# Answer is 1name="John"
# solve
# 1name="John"
# print(1name)
# print(name1)
# print(name_1)
# print(_name)


#Q7= Create a variable named carname and assign the value "BMW" to it.
# Answer is
carname = "BMW"
print(carname)



#Q8= Create a variable named x and assign the value 5 to it. Then print the value of x.

# Answer is
x = 5   
print(x)



##  Multiple Variables Value Assignment

#Q1 = What is the correct syntax to add the value "Hello World" to 3 variables in one statement?
# x = y = z = "Hello World" ✅
# x, y, z = "Hello World"
# x, y, z = "Hello", "World"


# Answer is x = y = z = "Hello World"


#Q2 =Insert the correct syntax to assign values to multiple variable in one line

# x, y, z = "Orange", "Banana", "Cherry" ✅
# x = "Orange", y = "Banana", z = "Cherry"
# x = "Orange" and y = "Banana" and z = "Cherry"
# x = "Orange" + y = "Banana" + z = "Cherry"    


# Answer is x, y, z = "Orange", "Banana", "Cherry"

# solve
x,y,z = "Orange", "Banana", "Cherry"
print(x)# output Orange


#Q3 = consider the following code:
fruits = ["apple", "banana", "cherry"]
a, b, c = fruits
print(a) # output apple

## Topic output variables in python

#Q1= Consider the following code:
print("Hello", "World")
# What is the output of the code?
# Hello World ✅
# Hello, World
# HelloWorld
# Hello World!

# Answer is Hello World
# solve
print("Hello", "World") # output Hello World
# print("Hello", "World", sep=",") # output Hello, World        
# print("Hello", "World", end="!") # output Hello World!
# print("Hello", "World", sep=",", end="!") # output Hello, World!

#Q2 = Consider the following code:
a='Hello'
b='World'
print(a + b)# output HelloWorld
print (a, b)# output Hello World

#Q3= Consider the following code:
c = 4
d = 5 
print(c + d) # output 9
print(c, d) # output 4 5


## Python Global Variables

#   Q1=  Consider the following code:

m = 'awesome'  # This is a global variable. It is accessible outside and inside functions unless shadowed.

def myfunc():
    m = 'is great'  # This is a local variable. It exists only within this function and does not affect the global 'm'.

myfunc()  # The function is called, but it only defines and uses its local variable 'm'. It doesn't change the global 'm'.

print("Python is " + m)  # This prints "Python is awesome" because the global variable 'm' is still 'awesome'.
# Answer is Python is awesome



#Q2= insert the keyword to make the variable x belong to the global scope.
# Answer is global
# solve
def myfunc():
    global x  # Declare 'x' as a global variable
    x = "Hello"  # Assign a value to the global variable 'x'
    print("Inside function:", x)  # This will print "Hello"

myfunc()  # Call the function to execute it
print("Outside function:", x)  # This will print "Hello" because 'x' is now a global variable
    

#Q3= Consider the following code:
v = 'awesome'  # This is a global variable
def myfunc():
    global v  # Declare 'v' as a global variable
    v = "is fantastic"  # This will change the global variable 'v'
    print("Python is " + v)  # This will print "Python is fantastic"

myfunc()  # Call the function to execute it
print("Python is " + v)  # This will also print "Python is fantastic" because 'v' was changed in the function       


# Answer is Python is fantastic



## Data Types in Python

#Q1 if x = 5 ,what is the correct syntax to check the data type of x?
# type(x) or print(type(x))✅
# type x
# x.type()
# x.type(x)


# Answer is type(x) or print(type(x))
# solve
# x = 5
# print(type(x)) # output <class 'int'>
type(x) # output <class 'int'>

#Q2= The following code example would print the data type of x. What is the output?
# x = 5.0
# print(type(x)) # output <class 'float'> ✅

#Q3= The following code example would print the data type of x , wat data type would that be?
l = "Hello World"
# print(type(x)) # output <class 'str'> ✅
# Answer is <class 'str'>
type(l) # output <class 'str'>


#Q4= The following code example would print the data type of x , wat data type would that be?
n=2.5
#print(type(n)) # output <class 'float'> ✅
# Answer is <class 'float'>
type(n)
# output <class 'float'>

#Q5= The following code example would print the data type of x , wat data type would that be?
X=[1,2,3,4,5]
# print(type(X)) # output <class 'list'> ✅
# Answer is <class 'list'>
#Q6= The following code example would print the data type of x , wat data type would that be?
# x = (1, 2, 3, 4, 5)
# print(type(x)) # output <class 'tuple'> ✅
# Answer is <class 'tuple'>

#Q7= The following code example would print data type of x, what data type would that be?
h={"name":"Azeez","age":34}
type(h)
print(type(h))

#Q7=The following code example would print the data type of x, what data type would that be ?
m=True
print(m)