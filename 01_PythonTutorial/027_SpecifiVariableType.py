#Specify a Variable Type
'''
There may be times when you want to specify a type on to a variable. This can be done with casting.
Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

Casting in python is therefore done using constructor functions:

int() - constructs an integer number from an integer literal, a float literal (by rounding down to the previous whole number), or a string literal (providing the string represents a whole number)

float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)

str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
'''

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

a = float(1)     # x will be 1.0
b = float(2.8)   # y will be 2.8
c = float("3")   # z will be 3.0
d = float("4.2") # w will be 4.2

e = str("s1") # x will be 's1'
f = str(2)    # y will be '2'
g = str(3.0)  # z will be '3.0'

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(x)
print(y)
print(z)

'''
Terminal:
1.0
2.8
3.0
4.2
s1
2
3.0
1
2
3
'''