 # Q1 = What will be the output of 5 + 3 *2?

# 11 ✅
# 20
# 16
# 13
# Solve
# First, we are performing a mathematical operation:
var = 5 + 3 * 2

# According to the order of operations (PEMDAS/BODMAS), multiplication (*) is done before addition (+)
# So, 3 * 2 = 6
# Then, 5 + 6 = 11

# The result of the calculation is stored in the variable 'var'
# Now we print the value of 'var' to the screen
print(var)  # This will output: 11


# Q2 = What is the result of 10 % 3 in python ?

# 2
# 4
# 0
# 1 ✅

# Solve
# The % operator is called the modulus operator.
# It returns the remainder when one number is divided by another.

# Here, we are dividing 10 by 3:
# 10 ÷ 3 = 3 with a remainder of 1
# Because 3 goes into 10 three times (3 * 3 = 9), and 1 is left over.

# So, 10 % 3 = 1

print(10 % 3)  # Output: 1

# or 

# We are using the modulus operator % to find the remainder
# when 10 is divided by 3.

m = 10 % 3   # 10 divided by 3 gives 3 remainder 1, so m = 1

print(m)     # Output: 1


# Q3 = What does // operator do in Python?


# Normal division
# Modulus
# Floor division  ✅
# Exponentiation

# Solve
# The // operator is called **floor division**
# It divides the number and **rounds down** (takes only the whole number part, ignoring the remainder)

x = 7 // 2  # 7 divided by 2 is 3.5, but floor division gives only the whole number part: 3

print(x)    # Output: 3

# Or

x = 9       # Assign 9 to variable x
y = 2       # Assign 2 to variable y

z = x // y  # Floor division: 9 // 2
            # 9 divided by 2 is 4.5
            # Floor division (//) drops the decimal part
            # So, z = 4

print(z)    # Output: 4


# Q4 = What is the output of 2 ** 3 ** 2?

# 64
# 512 ✅
# 16
# 8
# Solve 

# We are using the exponentiation operator '**' in Python.
# '**' means "to the power of"

# Python evaluates '**' from right to left (right-associative).
# So, 2 ** 3 ** 2 is evaluated as: 2 ** (3 ** 2)

# Step 1: Evaluate the inner exponent first
# 3 ** 2 = 9

# Step 2: Now evaluate the result of 2 ** 9
# 2 ** 9 = 512

print(2 ** 3 ** 2)  # Output: 512



# or


# Store the result in a variable 'v'
v = 2 ** 3 ** 2  # Same logic: 2 ** (3 ** 2) → 2 ** 9 → 512

print(v)  # Output: 512

# Q5 =      What is the output of 5 + 2 * 3 - 4 / 2?
# 9.0 ✅
# 10.0
# 8.0
# 7.0
# 6.0


# Solve

# Given expression:
# 5 + 2 * 3 - 4 / 2

# Step 1: According to the order of operations (PEMDAS/BODMAS),
# we first handle multiplication (*) and division (/), from left to right.

# Multiplication:
# 2 * 3 = 6
# Now the expression becomes:
# 5 + 6 - 4 / 2

# Division:
# 4 / 2 = 2.0 (Note: This gives a float value in Python)
# Now the expression becomes:
# 5 + 6 - 2.0

# Step 2: Now we do addition and subtraction from left to right.

# Addition:
# 5 + 6 = 11

# Subtraction:
# 11 - 2.0 = 9.0

# Final result is:
print(5 + 2 * 3 - 4 / 2)  # Output: 9.0

# or

x = 2 * 3       # x = 6
y = 4 / 2       # y = 2.0
z = x - y       # z = 6 - 2.0 = 4.0
r = 5 + z       # r = 5 + 4.0 = 9.0
print(r)        # Output: 9.0


# Q6 = What is the output of 3 * (4 + 5) - 2 ** 3 / 2?








#Q5b = What is the result of -3**2?
#-9✅
#6
#9
#Error

#Solve

print(-3**2)    # Output: -9
print((-3)**2)  # Output: 9

#or 

x = -3**2
print(x)

# Q6 = What will be the result of 7/2 in the Python
#3.5✅
#3.0
#4
#3

# solve

# We are assigning the result of 7 divided by 2 to the variable v
v = 7 / 2

# In Python, the '/' operator performs floating-point (decimal) division
# So even though 7 and 2 are integers, the result will be a float
# 7 divided by 2 equals 3.5

# Now we print the value of v
print(v)  # Output: 3.5


# Q7= What will be the output of int(5.8) + float(3)
# 9
# 8.0
# 8 ✅
# 9.0


# First, we are converting the integer 3 to a float:
# float(3) -> 3.0
# So the expression becomes:
# 5.3 + 3.0

# Adding the two float values:
# 5.3 + 3.0 = 8.3

# Now we convert the result (8.3) to an integer using int():
# int(8.3) -> 8  (this **truncates** the decimal part, it does NOT round)

# We are assigning this final integer value to variable c, and also using a type hint to say it's an int.
c: int = int(5.3 + float(3))

# Print the value of c
print(c)  # Output: 8


#Q8 = Which of the following is a valid variable name in Python?
# 1st_variable
# 1stVariable
# first-variable
# first_variable ✅
# Solve
# In Python, variable names must follow certain rules:
# - They can contain letters (a-z, A-Z), digits (0-9), and underscores (_).
# - They cannot start with a digit.
# - They cannot contain special characters like hyphens (-).
# - They are case-sensitive.
# - They cannot be a reserved keyword in Python.
#
# - They can be of any length.
# - They can contain letters, digits, and underscores.
# - They cannot start with a digit.
# - They cannot contain special characters like hyphens (-).
# - They are case-sensitive.
# - They cannot be a reserved keyword in Python.
# - They can be of any length.
# - They can contain letters, digits, and underscores.
# - They cannot start with a digit.
# - They cannot contain special characters like hyphens (-).
# - They are case-sensitive.


# Q9 =Which of the following is not an arthemetic operator in Python?
# +
# % 
#**
#& ✅
# Solve 
# In Python, the following are arithmetic operators:
# - Addition (+)
# - Subtraction (-)
# - Multiplication (*)
# - Division (/)
# - Modulus (%)
# - Exponentiation (**)
# - Floor Division (//)
#
# The '&' operator is a bitwise AND operator, not an arithmetic operator.
# So, the answer is '&'.


# Q10 = What is the output of True and False or True?
# True ✅
# False
# Error
# None
# Solve
# In Python, the 'and' and 'or' operators are used for logical operations.
# - 'and' returns True if both operands are True.
# - 'or' returns True if at least one operand is True.
# - 'not' negates the boolean value.
# - 'True' is a boolean value representing truth.
# - 'False' is a boolean value representing falsehood.
# - 'None' is a special value representing the absence of a value.
# - 'Error' is not a valid Python value.
# - 'True and False' evaluates to False.
# - 'False or True' evaluates to True.
# - So, the final result is True.

print(True and False or True)  # Output: True

# Q11 = What is the output of 5 == 5 and 3 != 2?
# True
# False 
# Error
# None
# Solve
# In Python, '==' checks for equality and '!=' checks for inequality.   
# - '5 == 5' evaluates to True.
# - '3 != 2' evaluates to True.
# - 'True and True' evaluates to True.
# - So, the final result is True.

print(5 == 5 and 3 != 2)  # Output: True


# Q12 = What is the output of 5 > 3 and 2 < 4?
# True ✅
# False
# Error
# None
# Solve
# In Python, '>' checks if the left operand is greater than the right operand.
# - '5 > 3' evaluates to True.
# - '2 < 4' evaluates to True.
# - 'True and True' evaluates to True.
# - So, the final result is True.
print(5 > 3 and 2 < 4)  # Output: True


# Q13 =What is the output of not (False or False)?
# True ✅
# False
# Error
# None
# Solve
# In Python, 'not' negates the boolean value.
# - 'False or False' evaluates to False.
# - 'not False' evaluates to True.
# - So, the final result is True.
print(not (False or False))  # Output: True

# Q14 = What will the True and not False evaluate to?
# True ✅
# False
# Error
# None
# Solve
# In Python, 'and' checks if both operands are True.
# - 'True and not False' evaluates to True.
# - 'not False' evaluates to True.
# - 'True and True' evaluates to True.
# - So, the final result is True.
print(True and not False)  # Output: True

# Q15 = What is the output of 5 != 3 or 2 == 2?
# True ✅
# False
# Error
# None
# Solve
# In Python, '!=' checks for inequality and '==' checks for equality.
# - '5 != 3' evaluates to True.
# - '2 == 2' evaluates to True.
# - 'True or True' evaluates to True.
# - So, the final result is True.
print(5 != 3 or 2 == 2)  # Output: True


# Q16 =What will be the result of 1 and 0 or 1?
# 1 ✅
# True
# 0
# False
# Solve

# In Python, 'and' and 'or' are logical operators.
# - '1 and 0' evaluates to 0 (because 1 is True and 0 is False).
# - '0 or 1' evaluates to 1 (because at least one operand is True).
# - So, the final result is 1.
print(1 and 0 or 1)  # Output: 1

#Q17 = What is the output of not 10 >5?
# True
# False ✅
# Error
# None
# Solve
# In Python, 'not' negates the boolean value.
# - '10 > 5' evaluates to True.
# - 'not True' evaluates to False.
# - So, the final result is False.
print(not 10 > 5)  # Output: False

# Q18 = What will be the result of bool and bool(1)?
# True ✅
# False
# Error
# None
# Solve
# In Python, 'bool' is a built-in function that converts a value to a boolean.
# - 'bool(1)' evaluates to True (because 1 is a truthy value).
# - 'bool and bool(1)' evaluates to True (because both operands are True).
# - So, the final result is True.
print(bool and bool(1))  # Output: True

#Q19 = What does True or False and False evaluate to?
# True ✅
# False
# Error
# None
# Solve

# In Python, 'or' and 'and' are logical operators.
# - 'True or False' evaluates to True (because at least one operand is True).
# - 'False and False' evaluates to False (because both operands are False).
# - So, the final result is True.
print(True or False and False)  # Output: True

# Q20 = What is the result of not (True and False)
# True
# False ✅
# Error
# None
# Solve
# In Python, 'not' negates the boolean value.
# - 'True and False' evaluates to False (because both operands are not True).
# - 'not False' evaluates to True.
# - So, the final result is True.
print(not (True and False))  # Output: True

#Q21= What will 5==5.0 return in Python?
# True ✅
# False
# Error
# None
# Solve
# In Python, '==' checks for equality.
# - '5' is an integer and '5.0' is a float, but they are considered equal in Python.
# - So, the final result is True.
print(5 == 5.0)  # Output: True

#Q22= What will 5!=5.0 return in Python?
# True
# False ✅
# Error
# None
# Solve
# In Python, '!=' checks for inequality.
# - '5' is an integer and '5.0' is a float, but they are considered equal in Python.
# - So, the final result is False.
print(5 != 5.0)  # Output: False

# Q23= What is the result of "hello" == "Hello" in Python?
# True
# False ✅
# Error
# None
# Solve
# In Python, string comparison is case-sensitive.
# - "hello" and "Hello" are not equal because of the difference in case.
# - So, the final result is False.
print("hello" == "Hello")  # Output: False

#Q24 = What will 10 >=10.0 return in Python?
# True ✅
# False
# Error
# None
# Solve
# In Python, '>=' checks if the left operand is greater than or equal to the right operand.
# - '10' is an integer and '10.0' is a float, but they are considered equal in Python.
# - So, the final result is True.
print(10 >= 10.0)  # Output: True

#Q25 =What is the result of "5" >2 in Python?
# True
# False 
# TypeError✅
# None
# Solve
# In Python, string comparison is based on lexicographical order.
# - "5" is a string and '2' is an integer.
# - Comparing a string with an integer will raise a TypeError.
# - So, the final result is TypeError.
#print("5" > 2)  # Output: TypeError: '>' not supported between instances of 'str' and 'int'

# Q26 = What is the output of 5 + "3" in Python?
# 53
# 8
# TypeError ✅
# None
# Solve
# In Python, you cannot add an integer and a string directly.
# - '5' is an integer and "3" is a string.
# - Adding an integer and a string will raise a TypeError.
# - So, the final result is TypeError.
#print(5 + "3")  # Output: TypeError: unsupported operand type(s) for +: 'int' and 'str'


#Q27= What will 5 is 5 evaluate to in Python?
# True ✅
# False
# Error
# None
# Solve
# In Python, 'is' checks for identity (whether two variables point to the same object).
# - '5' is an integer and '5' is also an integer.
# - They are the same object in memory.

# - So, the final result is True.
print(5 is 5)  # Output: True

# Q28 =What will [] ==[] return in Python?
# True ✅
# False
# Error
# None
# Solve
# In Python, '==' checks for equality.
# - '[]' is an empty list.
# - Two empty lists are considered equal.
# - So, the final result is True.
print([] == [])  # Output: True

#Q29 = What does [1, 3] == [1, 2] return in Python?
# True
# False ✅
# Error
# None
# Solve
# In Python, '==' checks for equality.
# - '[1, 3]' is a list with elements 1 and 3.
# - '[1, 2]' is a list with elements 1 and 2.
# - They are not equal because the second elements are different.
# - So, the final result is False.
print([1, 3] == [1, 2])  # Output: False

#Q30 = What will [1, 2] is [1, 2] return in Python?
# True
# False
# Error ✅
# None
# Solve
# In Python, 'is' checks for identity (whether two variables point to the same object).
# - '[1, 2]' is a list with elements 1 and 2.
# - '[1, 2]' is another list with elements 1 and 2.
# - They are two different objects in memory, even though they have the same content.
# - So, the final result is False.
# - So, the final result is TypeError.
#print([1, 2] is [1, 2])  # Output: TypeError: 'is' not supported between instances of 'list' and 'list'

#Q31 =What does "python" < "java" return in Python?
# True ✅
# False
# Error
# None
# Solve
# In Python, string comparison is based on lexicographical order (like dictionary order).
# - "python" comes after "java" in lexicographical order.
# - So, the final result is False.

print("python" < "java")  # Output: False

#Q32= What will be the value of x after x=5; x+=2?
# 7 ✅
# 5
# 2
# 3
# Solve
# In Python, the '+=' operator adds the right operand to the left operand and assigns the result to the left operand.
# - 'x = 5' assigns the value 5 to the variable x.
# - 'x += 2' adds 2 to the current value of x (which is 5) and assigns the result to x.
# - So, x becomes 5 + 2 = 7.
# - So, the final result is 7.
print(x := 5)  # Output: 5
x += 2
print(x)  # Output: 7

# Q33= What will be the value of y =10; y*=2; print(y) in Python?
# 20 ✅
# 10
# 5
# 2
# Solve
# In Python, the '*=' operator multiplies the left operand by the right operand and assigns the result to the left operand.
# - 'y = 10' assigns the value 10 to the variable y.
# - 'y *= 2' multiplies the current value of y (which is 10) by 2 and assigns the result to y.
# - So, y becomes 10 * 2 = 20.
# - So, the final result is 20.
print(y := 10)  # Output: 10
y *= 2
print(y)  # Output: 20

#Q34 = What does x // =3 do in Python?
#None
# Raises an Error
# Performs normal division
# Performs floor division ✅
# Solve
# In Python, the '//=' operator performs floor division and assigns the result to the left operand.
# - It divides the left operand by the right operand and rounds down to the nearest whole number.
# - So, the final result is floor division.

print(x := 10)  # Output: 10
x //= 3
print(x)  # Output: 3 (10 // 3 = 3.33, rounded down to 3)

#Q35 = if a =10, What will a % =3 return in Python?
# 1 ✅
# 3
# 10
# 0
# Solve
# In Python, the '%=' operator calculates the modulus and assigns the result to the left operand.
# - It divides the left operand by the right operand and returns the remainder.
# - So, the final result is 1.
# - So, the final result is 1.
print(a := 10)  # Output: 10
a %= 3
print(a)  # Output: 1 (10 % 3 = 1, remainder of 10 divided by 3 is 1)

#Q36= What does a **=3 do in Python?
# Raises an Error
# Performs normal exponentiation
# Performs floor exponentiation
# Performs exponentiation ✅
# Solve
# In Python, the '**=' operator performs exponentiation and assigns the result to the left operand.
# - It raises the left operand to the power of the right operand.
# - So, the final result is exponentiation.

print(a := 2)  # Output: 2
a **= 3
print(a)  # Output: 8 (2 ** 3 = 8)


#Q37= What is the value of x after x=5; x**3; print(x) in Python?
# 125 ✅
# 5
# 8
# 3
# Solve
# In Python, the '**' operator performs exponentiation.
# - 'x = 5' assigns the value 5 to the variable x.
# - 'x ** 3' raises x (which is 5) to the power of 3.
# - So, x becomes 5 ** 3 = 125.
# - So, the final result is 125.
print(x := 5)  # Output: 5

x **= 3
print(x)  # Output: 125 (5 ** 3 = 125)

#Q=38= What does x & = y do in Python?
#Addition of x and y
#Subtraction of x and y
#Bitwise AND of x and y ✅
#Bitwise OR of x and y
# Solve
# In Python, the '&=' operator performs a bitwise AND operation and assigns the result to the left operand.
# - It takes the bitwise AND of the left operand and the right operand.
# - So, the final result is bitwise AND.

x = 6      # Binary: 110
y = 3      # Binary: 011

x &= y     # x = x & y → x = 6 & 3 → x = 2 (Binary: 010)

print(x)   # Output: 2


#Q39= What does x | = y do in Python?
#Addition of x and y
#Subtraction of x and y
#Bitwise AND of x and y
#Bitwise OR of x and y ✅
# Solve
# In Python, the '|=' operator performs a bitwise OR operation and assigns the result to the left operand.
# - It takes the bitwise OR of the left operand and the right operand.  
# - So, the final result is bitwise OR.

x = 6      # Binary: 110
y = 3      # Binary: 011

x |= y     # x = x | y → x = 6 | 3 → x = 7 (Binary: 111)

print(x)   # Output: 7

#Q40= What does x ^ = y do in Python?
#Addition of x and y
#Subtraction of x and y
#Bitwise AND of x and y
#Bitwise XOR of x and y ✅
# Solve
# In Python, the '^=' operator performs a bitwise XOR operation and assigns the result to the left operand.
# - It takes the bitwise XOR of the left operand and the right operand.
# - So, the final result is bitwise XOR.
x = 6      # Binary: 110
y = 3      # Binary: 011

x ^= y     # x = x ^ y → x = 6 ^ 3 → x = 5 (Binary: 101)

print(x)   # Output: 5
