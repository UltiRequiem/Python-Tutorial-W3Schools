#String Format

'''
As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
age = 36
txt = "My name is John, I am " + age
print(txt)

Console:can only concatenate str (not "int") to str
'''
'''But we can combine strings and numbers by using the format() method!

The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:'''
#Use the format() method to insert numbers into strings:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

'''
Terminal:
My name is John, and I am 36
'''
#https://www.w3schools.com/python/python_strings_format.asp