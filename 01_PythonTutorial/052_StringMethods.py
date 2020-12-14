#String Methods
'''Python has a set of built-in methods that you can use on strings.'''
#Note: All string methods returns new values. They do not change the original string.

#Upper case the first letter in this sentence:
Capitalize = "hello, and welcome to my world."

x = Capitalize.capitalize()

print (x)

#Make the string lower case:
Casefold = "Hello, And Welcome To My World!"

x = Casefold.casefold()

print(x)

#Return the number of times the value "apple" appears in the string:
Count = "Pedro,Pedro,Pedro,Pedro,Pedro,Pedro,Pedro,Pedro,Pedro,Pedro,Pedro,Pedro,Pedro,Pedro,Pedro."

x = Count.count("Pedro")

print(x)

#Print the word "banana", taking up the space of 20 characters, with "banana" in the middle:
Center = "banana"

x = Center.center(20)

print(x)

#UTF-8 encode the string:
Encode = "My name is Ståle"

x = Encode.encode()

print(x)

#Check if the string ends with a punctuation sign (.):
EndsWith = "Hello, welcome to my world!"

x = EndsWith.endswith(".")

print(x)

#Set the tab size to 2 whitespaces:
WhiteTabs = "H\te\tl\tl\to"

x =  WhiteTabs.expandtabs(2)

print(x)

#Where in the text is the word "welcome"?:
Finder = "Hello, welcome to my world."

x = Finder.find("welcome")

print(x)

#Insert the price inside the placeholder, the price should be in fixed point, two-decimal format:
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

#Where in the text is the word "welcome"?:
txt = "Hello, welcome to my world."

x = txt.index("welcome")

print(x)

#Check if all the characters in the text are alphanumeric:
txt = "Company12"

x = txt.isalnum()

print(x)

#Check if all the characters in the text are letters:
txt = "CompanyX"

x = txt.isalpha()

print(x)

#Check if all the characters in the unicode object are decimals:
txt = "\u0033" #unicode for 3

x = txt.isdecimal()

print(x)

#Check if all the characters in the text are digits:
txt = "One"

x = txt.isdigit()

print(x)

#Check if the string is a valid identifier:
txt = "2bring"

x = txt.isidentifier()

print(x)

#Check if all the characters in the text are in lower case:
txt = "Hello World!"

x = txt.islower()

print(x)

#Check if all the characters in the text are numeric:
txt = "565543"

x = txt.isnumeric()

print(x)

#Check if all the characters in the text are printable:
txt = "Hello! Are you #1?"

x = txt.isprintable()

print(x)

#Check if all the characters in the text are whitespaces:
txt = "   "

x = txt.isspace()

print(x)

#Check if each word start with an upper case letter:
txt = "Hello, and welcome to my world!"

x = txt.istitle()

print(x)

#Check if all the characters in the text are in upper case:
txt = "THIS IS NOW!"

x = txt.isupper()

print(x)

#Join all items in a tuple into a string, using a hash character as separator:
myTuple = ("John", "Peter", "Vicky")

mySeparator = " and "

x = mySeparator.join(myTuple)

print(x)

#Return a 20 characters long, left justified version of the word "banana":
txt = "banana"

x = txt.ljust(20)

print(x, "is my favorite fruit.")

#Lower case the string:
txt = "HELLO FRIENDS"

x = txt.lower()

print(x)

#Remove spaces to the left of the string:
txt = "     banana     "

x = txt.lstrip()

print("of all fruits",x,"is my favorite")

#Create a mapping table, and use it in the translate() method to replace any "S" characters with a "P" character:
txt = "Hello Sam!";
mytable = txt.maketrans("Sam", "Paa");
print(txt.translate(mytable));

#Partitions
txt = "I could eat bananas all day"

x = txt.partition("bananas")

print(x)

#Replace the word "bananas":
txt = "I like bananas"

x = txt.replace("bananas", "chocolat")

print(x)

#Where in the text is the last occurrence of the string "casa"?:
txt = "Mi casa, su casa."

x = txt.rfind("casa")

print(x)

#Where in the text is the last occurrence of the string "casa"?:
txt = "banana"

x = txt.rjust(20)

print(x, "is my favorite fruit.")

#rpartition
'''
Search for the last occurrence of the word "bananas", and return a tuple with three elements:

1 - everything before the "match"
2 - the "match"
3 - everything after the "match"
'''
txt = "I could eat bananas all day, bananas are my favorite fruit!"

x = txt.rpartition("bananas")

print(x)

#rsplit: Split a string into a list, using comma, followed by a space (, ) as the separator:
txt = "apple, banana, cherry"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.rsplit(", ", 1)

print(x)

#Remove any white spaces at the end of the string:
txt = "     banana     "

x = txt.rstrip()

print("of all fruits", x, "is my favorite")




'''
Terminal:
Hello, and welcome to my world.
hello, and welcome to my world!
15
       banana
b'My name is St\xc3\xa5le'
False
H e l l o
7
For only 49.00 dollars!
7
True
True
True
False
False
False
True
True
True
False
True
John and Peter and Vicky
banana               is my favorite fruit.
hello friends
of all fruits banana      is my favorite
Hello Paa!
('I could eat ', 'bananas', ' all day')
'''
#https://www.w3schools.com/python/python_strings_methods.asp