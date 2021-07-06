"""
Refreshing different operations in Python
"""

# Division goes from left to right
print(1/2/2)

# Integer division
result = 5//2
print(result)

# Modulo/remainder
result = 5 % 2
print(result)

# With negatives
result = -9 % 7
print(result)

# Algebraically
n = 5
m = 2
a = n//m
print(a)
b = n%m
print(b)
print(n == a * m + b)

n = -9
m = 7
a = n//m
print(a)
b = n%m
print(b)
# -9 == -2*7 + 5
# -9 == -14 + 5 == -9
print(n == a * m + b)

# Exercises page 21
print(2 * 4 + 2) # 10
print(2**4 - 4**2) # 0
print(2 * (1 + 2 + 3)) #12
print(5 / 2) # 2.5

import math
print(math.floor(5/2)) # 2

print(2 / (1 + 2 + 3)) #0.33
print((1 + 2 + 3)**(1 + 2 + 3))
print((1 + 2 + 3) / 2) #3

print("hewwo")

# Splitting operations over several lines:
a = 2 * 5\
+ 7 \
* 8 

b = 2 * 5 + 7 * 8
print(a == b)

# Booleans
print(False and False) # False
print(False and True) # False
print(True and False) # False
print(True and True) # True

print(False or False) # False
print(False or True) # True
print(True or False) # True
print(True or True) # True

# Python specific Tuple substitution/Multiple assignment
a = 3
b = 4

a, b = b, a # reassignment a = b and b = a
print(a) # 4!
# Also works with larger tuples ;)
# Tuples will hold the values like normal variables

""" 
Working with strings
"""
# concatenation
a = "hello"
b = "world"
print(a + " " + b)

# multiple concatenation
print(a*5)

# f and format
print(f"the answer is {format(42)}")
print("The answer is {}".format(42))
print(f"{a} {b}")

# Naming the placeholders
print("Hello {name}, welcome to {hotel}".format(hotel = "Bellevue", name = "John"))

# Subscripting and slicing
print(a)
print(a[0])
print(a[-1])

print(a[2:4]) # Python does not include the second index

# Exercise page 30
print(a[1:1]) # empty
print(a[4:1]) # empty

# Using steps
print(a[0:5:2]) #hlo out of hello

# Lists
list1 = ["string"]
print(list1[0][0])

# Concatenation of lists
a = ["string"]
b = [42, "string2"]
print(a + b)
# Lengths of a list
print(len(a + b))

print(b * 3) # Concatenates 3 list b together

# Updating via indexation
b[1] = "new value"
print(b)

# Tables
n = 3 # Rows
m = 4 # Columns
T = [[0] * m for i in range(n)]

print(T)

# Insert and pop
# insert() pops in the value on th index position
x = [1, 2, 3]
print(x)
x.insert(1, 42)
print(x)
# pop() removes the value on the index position
x.pop(1)
print(x)

# Deleting stuff on a given index
del x[2]
print(x)

# remove() uses item not index
x = [1, 2, 3]
x.remove(3)
print(x)
# It only removes the first instance!

# append()
x.append(3)
print(x)

# Take the last value and store it in y
y = x.pop()
print(x, y)


# List comprehension for-loops
x = [2* i for i in range(5)]
[print(i,j) for i in range(5) for j in range(10)[0:6:2]]

x = [1, 2, 3, 2]
x = [a for a in x if a !=2]
print(x)

# Importing modules

## import module_name
## from module_name import function1, function2
## import module_name as new_module_name
## from module_name import function1 as new_function1, function2 as new_function2
