#Escape Characters

#The Table is in 051_TableEscapeCharacters.txt 

SingleQuote = "The humans are \'Inhumans\' sometimes."
print(SingleQuote)

Backslash = "This will insert one \\ (backslash)."
print(Backslash) 

NewLine = "Hello\nWorld!"
print(NewLine) 

CarriageReturn = "Hello\rWorld!"
print(CarriageReturn) 

AnSpace = "So\tSpace!"
print(AnSpace)

#This example erases one character (backspace):
EraseBackSpace = "Little \bSpace!"
print(EraseBackSpace)

#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 

#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 


'''
Terminal:
The humans are 'Inhumans' sometimes.
This will insert one \ (backslash).
Hello
World!
World!
So      Space!
LittleSpace!
Hello
Hello
'''
#