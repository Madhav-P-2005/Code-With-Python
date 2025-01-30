# FILE HANDLING IN PYTHON

'''

>>> Ram :- volatile (temporary)
>>> HDD :- Non Volatile (permanent)

File handling is an important part of any web application.
Python has several functions for creating, reading, updating, and deleting files. 

'''

# File Handling

'''

>>>  The key function for working with files in Python is the open() function. The open() function takes two parameters; filename, and mode. There are four different methods (modes) for opening a file :-

'''

'''

1) r  :- Read - Default value. Opens a file for reading, error if the file does not exist
2) a  :-  Append - Opens a file for appending, creates the file if it does not exist
3) w  :- Write - Opens a file for writing, creates the file if it does not exist
4) x  :-  Create - Creates the specified file, returns an error if the file exists
5) +  :-  Open for Updating.

In addition you can specify if the file should be handled as binary or text mode :- (Types of files)
5) t - Text Files- Default value. Text mode
6) b - Binary Files - Binary mode.(Example:Images)

'''

# Syntax :- 

'''

To open a file for reading it is enough to specify the name of the file :-
    
f = open("demofile.txt")
The code above is the same as:
f = open("demofile.txt", "r")

Because "r" for read, and "t" for text are the default values, you do not need to specify
them.

'''


# I) Open a File on the Server :-

'''

# To open the file, use the built-in open() function.
# The open() function returns a file object, which has a read() method for reading the content of the file :-

# Example :- 
f = open("demofile.txt", "r")
print(f.read())

'''


f = open("E:\Python Tutorial - Code With Harry\MyEnvironment\Files\Open-a-File-on-the-Server.txt")

data = f.read()   # To Read the file 

print(data)            # Output :-  Madhav is a Bad Boy

f.close



# Close Files :- It is a good practice to always close the file when you are done with it.

# Example :-  Close the file when you are finish with it :-

f = open("demofile.txt", "r")

print(f.readline())

f.close()




# Create a New File : - To create a new file in Python, use the open() method, with one of the following parameters :-

'''

1) "x" :- Create - will create a file, returns an error if the file exist. 

# Example :- Create a file called "myfile.txt"

f = open("myfile.txt", "x")  # Output :- Result: a new empty file is created!


2) "a" :- Append - will create a file if the specified file does not exist.

3) "w" :- Write - will create a file if the specified file does not exist

# Example :- Create a new file if it does not exist :- 
f = open("myfile.txt", "w")

'''



# II) To Write a File :- 

st = "Hey Harry You are amazing"

f = open("To-Write-a-File.txt" , "w")

f.write(st)

f.close

'''

Output :-  Hey Harry You are amazing . This is a demo file which Represents how to create a file in your desired Path

'''


# or 


import os

# Define the content
st = "Hey Harry You are amazing . This is a demo file which Represents how to create a file in your desired Path"

# Define the path where you want to create the file

folder_path = r"E:\Python Tutorial - Code With Harry\MyEnvironment\Files"



# 1) Using r before the File Path

'''

#  The r before the file path stands for a raw string literal. In Python, a raw string literal is a string where backslashes are treated as literal characters. This is particularly useful for file paths in Windows, which often contain backslashes (\).

# a) Without r :- 
path = "E:\Python Tutorial - Code With Harry\MyEnvironment\Files\To-Write-a-File.txt"
# This might cause issues if any escape sequences are present, e.g., "\t" for a tab character.

# b) With r :-
path = r"E:\Python Tutorial - Code With Harry\MyEnvironment\Files\To-Write-a-File.txt"
# The string is treated exactly as it is, without interpreting backslashes as escape characters.

# 2) Using with open(file_path, "w") as f :-

#) The with open syntax is a context manager that is used to handle resources such as files. It ensures that the file is properly closed after its suite finishes, even if an exception is raised at some point. This makes the code cleaner and safer.

   ●) open(file_path, "w"): This opens the file at file_path in write mode ("w"). If the file does not exist, it will be created. If it does exist, its content will be overwritten.

   ●) as f: This assigns the opened file object to the variable f.

   ●) f.write(st): This writes the string st to the file.

   

# Benefits of Using Context Managers (with) :-

1) Automatic Resource Management: Ensures that the file is closed when the block is exited, even if an error occurs.

2) Cleaner Syntax: Reduces the need for explicitly calling close().

3) Error Handling: Improves error handling and reduces the chances of resource leaks.

'''



file_name = "To-Write-a-File.txt"

file_path = os.path.join(folder_path, file_name)


# Create and write to the file
with open(file_path, "w") as f:
    f.write(st)

print(f"File created at: {file_path}")        # Output :-  Hey Harry You are amazing . This is a demo file which Represents how to create a file in your desired Path


# Write to an Existing File :- To write to an existing file, you must add a parameter to the open() function :-

'''

i) "a" :-  Append - will append to the end of the file
ii) "w" :-  Write - will overwrite any existing content

'''

# i) Example :- 
# Create a File "Appending-A-File.txt"
f = open("E:\Python Tutorial - Code With Harry\MyEnvironment\Files\Appending-A-File.txt", "w")

data= f.write("Hello Guys , This is First Line I am writing ! ")           

print(data)               


# Appending :- 
f = open("E:\Python Tutorial - Code With Harry\MyEnvironment\Files\Appending-A-File.txt" , "a")

f.write("\n Now the file has more Content ! # Appending Content \n")

f.close()


# ii) Example :- Open the file "Appending-A-File.txt"  and overwrite the content :-
f = open("E:\Python Tutorial - Code With Harry\MyEnvironment\Files\Appending-A-File.txt", "w")

f.write("Woops! I have deleted the content!")

f.close()


# open and read the file after the overwriting :- 
f = open("E:\Python Tutorial - Code With Harry\MyEnvironment\Files\Appending-A-File.txt", "r")

print(f.read())

# Note :- ["the "w" method will overwrite the entire file."]




# III) Read Lines in a File  :-  You can return one line by using the readline() method:

# Example :- 
f = open("E:\Python Tutorial - Code With Harry\MyEnvironment\Files\Open-a-File-on-the-Server.txt")

lines = f.readlines()  # Returns a list 

print(lines , type(lines))          # Output :- ['Madhav is a Bad Boy . \n', 'ReadLines Body :- \n', 'I am third Line \n', 'This is a demo to represent how to use ReadLines() function  in a File . '] <class 'list'>


# ReadLine() :- 

line1 = f.readline()

print(line1 , type(line1))           # Output :- Madhav is a Bad Boy .  <class 'str'>


line2 = f.readline()

print(line2 , type(line2))           # Output :- ReadLines() and ReadLine() Body :-  <class 'str'>


line3 = f.readline()

print(line3 , type(line3))           # Output :- I am third Line  <class 'str'>


line4 = f.readline()

print(line4 , type(line4))           # Output :- This is a demo to represent how to use ReadLines() function  in a File .  <class 'str'>


line5 = f.readline()

print(line5=="" , type(line5))       # Output :- True <class 'str'>



# Using While Loop :- 
line = f.readline()

# while(line!=""):
print(line)                          # Output :-  Madhav is a Bad Boy . 
line = f.readline()

f.close()


# Output :- 

'''

Madhav is a Bad Boy . 

ReadLines() and ReadLine() Body :-  

I am third Line 

This is a demo to represent how to use ReadLines() function  in a File .


'''



# Delete a File :- To delete a file, you must import the OS module, and run its os.remove() function :-


# Example :-  Remove the file ""
import os
os.remove("demofile.txt")


# Check if File exist :- To avoid getting an error, you might want to check if the file exists before you try to delete it :-

# Example :- 
import os
if os.path.exists("demofile.txt"):
     os.remove("demofile.txt")
else:
     print("The file does not exist")



# With Statement :- The best way to open and close the file automatically is the with statement.

f = open("E:\Python Tutorial - Code With Harry\MyEnvironment\Files\Open-a-File-on-the-Server.txt")
print(f.read())
f.close


# The same can be written using with Statement like this :- 
with open("E:\Python Tutorial - Code With Harry\MyEnvironment\Files\Open-a-File-on-the-Server.txt") as f:
    print(f.read())


# You dont have to explicitly close the file 
