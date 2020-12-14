#String Format Part 2

#The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 4
itemno = 456
price = 99.99
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

'''
Terminal:
I want 3 pieces of item 567 for 49.95 dollars.
I want to pay 99.99 dollars for 4 pieces of item 456.
'''
#Learn more about String Formatting in our String Formatting chapter: https://www.w3schools.com/python/python_string_formatting.asp
#https://www.w3schools.com/python/python_strings_format.asp
