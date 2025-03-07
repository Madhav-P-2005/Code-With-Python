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




#  WriteLines()  Method :-   The writelines() method in Python is used to write multiple lines to a file at once. It does not add a newline (\n) automatically, so you need to include \n at the end of each line.


# Syntax :-   file.writelines(list_of_strings)


'''

   a) list_of_strings :-   A list of strings that will be written to the file.

   b) Unlike write(), it writes multiple lines at once.

'''


# Example 1 :-  Writing Multiple Lines to a File


# Open file in write mode
with open("sample.txt", "w") as file:

    lines = ["Hello, World!\n", "Python is great!\n", "File handling is easy.\n"]

    file.writelines(lines)

print("Lines written successfully!")

# Note :-  Since writelines() does not add \n, we manually include it in each string




# Example 2 :-  Writing a List Without Newlines  -->  If you forget \n, everything will be written in a single line:

with open("sample.txt", "w") as file:

    lines = ["Hello, World!", "Python is great!", "File handling is easy."]

    file.writelines(lines)

# Output in file :-  Hello, World!Python is great!File handling is easy.




# Example 3 :-  Using writelines() with User Input

lines = []
for i in range(3):

    line = input(f"Enter line {i+1}: ") + "\n"

    lines.append(line)

with open("user_input.txt", "w") as file:

    file.writelines(lines)

print("User input written to file!")




# ✅ Use Cases of writelines() ? 

'''

   1) Writing multiple lines at once to a file.

   2) Writing data from a list to a file efficiently.

   3) Writing user inputs or logs to a file.

'''




# Delete a File :- To delete a file, you must import the OS module, and run its os.remove() function :-

# # Example :-  Remove the file
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




# seek() and tell() Functions ?

'''

>>> These functions are used to manipulate and track the file cursor (pointer) in file handling operations.

'''


# 1) seek() Function :- The seek() function is used to move the file cursor (pointer) to a specific position in a file.


# 📝 Syntax :-   file.seek(offset, whence)

'''

1) offset → Number of bytes to move (positive/negative).

2) whence (Optional) → Determines the reference position :- 

    a)  0 (default) → Beginning of the file.

    b)  1  →  Move relative to current position.

    c)  2  →  Move relative to end of file.

'''



# Example :-   Using seek() 

with open(r"E:\Python Tutorial - Code With Harry\MyEnvironment\Files\this.txt"  ,"r", encoding="utf-8") as file:

    print(type(file))                # Ouput :-   <class '_io.TextIOWrapper'>


    # Move to the 10th byte in the file 
    file.seek(10)

     # Read the next 18 bytes 
    data  = file.read(18)
    print(data)



'''

Output :- 

<class '_io.TextIOWrapper'>
we fall, Bruce? So


'''


#  Why is seek(10, 1) will Not Work ?

'''

   1) In text mode ("r"), Python automatically decodes the file, handling line endings and character encodings.

   2) This means relative seeks (whence=1 for current position) don't work properly because characters may not always have the same byte size (e.g., UTF-8 encoding).

'''



# ✅ Solution :-  Use Binary Mode ("rb")   

["Note :-  This works because in binary mode, every character is treated as a single byte."]

'''  

    If you need to use whence=1 (relative seek), open the file in binary mode ("rb") instead :-     

'''



with open(r"E:\Python Tutorial - Code With Harry\MyEnvironment\Files\this.txt"  ,"rb") as file:

    print(type(file))                # Ouput :-   <class '_io.TextIOWrapper'>


    # Move to the 10th byte in the file 
    # file.seek(10,2)           # Output :- b''

    '''
    
    Output :-  <class '_io.BufferedReader'>
               b''

    '''



    # Move relative to end of file 
    file.seek(-20,2)

    
    # Read the next 19 bytes 
    data  = file.read(19)

    print(data)


    '''

    Output :-    <class '_io.BufferedReader'>
                 b'act according to it'
    
    '''


# The Problem  ? 


'''

1) When you use seek(10, 2), you're trying to move 10 bytes beyond the end of the file.
2) If the file is shorter than 10 bytes, seek(10, 2) goes past the end, and reading (file.read()) returns nothing (b'').
3) Many operating systems don't allow seeking beyond EOF (End of File), so it simply positions at EOF.


'''



# 🚀 Summary !

'''

seek(offset, whence)                      	Meaning	                                                  Works?
------------------------------------------------------------------------------------------------------------------------------------
seek(10, 0)	                            Move to 10th byte from start	                             ✅ Yes

seek(10, 1)	                            Move 10 bytes forward from current	                         ⚠ Only in "rb" mode

seek(10, 2)                             Move 10 bytes beyond end	                                 ❌ Won't work (EOF issue)

seek(-10, 2)	                        Move 10 bytes before EOF	                                 ✅ Works if file is large enough 

'''




# 2) tell() Function   :-   The tell() function returns the current cursor position in the file.



# 📝 Syntax :-   position = file.tell()


'''   

    Returns an integer representing the cursor position (in bytes).   

'''




# Example :-   Using tell()

with open(r"E:\Python Tutorial - Code With Harry\MyEnvironment\Files\this.txt"  ,"r", encoding="utf-8") as file:

    print(type(file))                # Ouput :-   <class '_io.TextIOWrapper'>


    # Move to the 10th byte in the file 
    file.seek(10)

    # Read the next 18 bytes 
    print(file.tell())

    data  = file.read(18)

    print(data)



'''

Output :-   <class '_io.TextIOWrapper'>
            10
            we fall, Bruce? So

'''




# 3) truncate() Function    :-    The truncate() function in Python is used to resize a file to a specified size (in bytes). If the file is larger than the specified size, it will be cut off. If it is smaller, it will be extended with null bytes (\x00).



#  Syntax  :-   file.truncate(size)


'''
 
  1) size → (Optional) The new size of the file in bytes.

    a) If size is not specified, it will truncate at the current file position.

    b) If size is greater than the file size, it adds null bytes (\x00).

    c) If size is less than the file size, it removes extra content.

'''




# How truncate() Works  ? 

'''

    1) Truncate to a specific size (in bytes).

    2) Reduce file content if the size is smaller.

    3) Extend file with null bytes if the size is larger.

    4) By default, it truncates at the current file pointer position.

'''




# ✅ Usage of truncate()  ? 


#   1) Truncating to a Smaller Size (Removes Data)  :- The file is cut off after 10 or n  bytes.



with open(r"E:\Python Tutorial - Code With Harry\MyEnvironment\Files\truncate-Example.txt"  ,"w", encoding="utf-8") as file:
         

        file.write(" This is a truncate.txt  Example file ")

        file.truncate(9)
  


with open(r"E:\Python Tutorial - Code With Harry\MyEnvironment\Files\truncate-Example.txt" , 'r')  as  file :
                
                print(file.read())




# without file.truncate(9)  ? 

'''

Output :-    This is a truncate.txt  Example file 

'''




# With file.truncate(9)  ? 

'''

Output :-    This is

'''




#  2) Truncate Without Arguments (Uses Current Position)   :- 


with open("example.txt", "w") as file:
    file.write("Hello, this is a test file.")  # Writing initial content

with open("example.txt", "r+") as file:
    file.seek(6)    # Move the pointer to the 6th byte (after "Hello,")
    file.truncate()  # Truncate from here

with open("example.txt", "r") as file:
    print(file.read())  # Output: 'Hello,'





'''

Original File :- 

H  e  l  l  o  ,  _  t  h  i  s  _  i  s  _  a  _  t  e  s  t  _  f  i  l  e  .
0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26

seek(6) → Moves pointer to position 6 (after "Hello,")
truncate() → Removes everything after position 6

Final File :-

H  e  l  l  o  ,
0  1  2  3  4  5  (Truncated here)

'''




#  3) Expanding a File (Adds Null Bytes \x00) :-   The file is extended with null bytes.


with open("example.txt", "r+") as file:

    file.truncate(30)                       # Extend the file to 30 bytes


with open("example.txt", "rb") as file:
    
    print(file.read())                      # Output :-  b'Hello,\x00\x00\x00\x00\x00\x00\x00\x00\x00'







# 🚀 Summary   ! 

'''

Scenario	                                                       Result

truncate(10)	                                            Cuts file to 10 bytes

truncate()	                                                Truncates from current position

truncate(50)	                                            Extends file to 50 bytes (adds \x00 if needed)


'''