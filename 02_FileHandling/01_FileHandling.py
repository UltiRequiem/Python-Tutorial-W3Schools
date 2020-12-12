'''
File Handling
The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:

-----------------------------------------------------------------------------------------
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists
-----------------------------------------------------------------------------------------
In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)
-----------------------------------------------------------------------------------------
'''

#Syntax: To open a file for reading it is enough to specify the name of the file:

#f = open("demofile.txt")  --its equal to--  f = open("demofile.txt", "rt")

f = open("demofile.txt")