# Modules 
# https://pypi.org/project/pyjokes/

import pyjokes # type: ignore

joke = pyjokes.get_joke()
print(joke)

# Comments 
# Single Line Comments

''' 
Example 

for Multiple line

, comments 

'''




# OS Module in Python  ? 


# 1️⃣) Definition :-   The os module in Python provides functions for interacting with the operating system. It allows you to perform tasks like file handling, directory management, process management, and environment variable access.



# # 2️⃣) Syntax  :-    import os


'''

🔹 You first need to import the os module before using its functions.

'''


# # 3️⃣ How os Module Works ?

'''

1)  It provides an interface to interact with the operating system.

2) Allows us to create, delete, and modify files & directories.

3) Can be used to execute system commands.

4) Helps manage environment variables and system paths.

'''




# 4️⃣) Commonly Used os Functions & Examples  ? 

# a) Getting the Current Working Directory :- 

import os
print(os.getcwd())      # Prints the current directory



# b) Changing the Current Working Directory  :- 

os.chdir("C:/Users/YourName/Desktop")  # Changes working directory
print(os.getcwd())  # Verify change



# c)  Listing Files & Directories  :- 

print(os.listdir())  # Lists all files & folders in the current directory



# d) Creating & Removing a Directory :- 

os.mkdir("NewFolder")  # Creates a new folder

os.rmdir("NewFolder")  # Removes the empty folder



# e)  Creating & Removing Files :- 

with open("test.txt", "w") as file:
    file.write("Hello!")

os.remove("test.txt")  # Deletes the file



# f) Checking If a File or Directory Exists  :- 

print(os.path.exists("test.txt"))  # Returns True if file exists



# g) Running System Commands (e.g., Opening Notepad on Windows) :- 

os.system("notepad")  # Opens Notepad



# h) Getting Environment Variables  :- 

print(os.environ['PATH'])  # Prints system's PATH variable


# i) Change Directory in Python  :-  You can use os.chdir() to change the directory before running os.listdir():


import os

os.chdir(r"E:\Python Tutorial - Code With Harry\MyEnvironment")  # Change to the correct directory
print(os.getcwd())  # Verify the new working directory

folders = os.listdir("Files")  # Now it should work if "Files" exists
print(folders)



# Example 

# import os

if(not os.path.exists("data")):
    os.mkdir("data")


# Creates 1 to 100 files automatically in the data folder 
for i in range(0,100):
    os.mkdir(f"data/Day{i+1}")


# Rename Day to Tutorial.txt

for i in range(0,100):
    os.rename(f"data/Day{i+1}", f"data/Tutorial{i+1}")




# Os List ? 

import os

# folders = os.listdir("Files")

# print(folders)

print(os.getcwd())       # Output :-   E:\Python Tutorial - Code With Harry

folders = os.listdir(r"E:\Python Tutorial - Code With Harry\MyEnvironment\Files")

print(folders)


# Output :- 

['Appending-A-File.txt', 'Donkey.txt', 'hiscore.txt', 'log.txt', 'Old.txt', 'Open-a-File-on-the-Server.txt', 'Parenthesized Context Manager.txt', 'poems.txt', 'renamed_by_python.txt', 'Tables.txt', 'table_Of_10.txt', 'table_Of_11.txt', 'table_Of_12.txt', 'table_Of_13.txt', 'table_Of_14.txt', 'table_Of_15.txt', 'table_Of_16.txt', 'table_Of_17.txt', 'table_Of_18.txt', 'table_Of_19.txt', 'table_Of_2.txt', 'table_Of_20.txt', 'table_Of_3.txt', 'table_Of_4.txt', 'table_Of_5.txt', 'table_Of_6.txt', 'table_Of_7.txt', 'table_Of_8.txt', 'table_Of_9.txt', 'this.txt', 'this_copy.txt', 'To-Write-a-File.txt', 'Words-Q5.txt']



for folder in folders :
    print(folder)


# Output :- 


'''

Appending-A-File.txt
Donkey.txt
hiscore.txt
log.txt
Old.txt
Open-a-File-on-the-Server.txt
Parenthesized Context Manager.txt
poems.txt
renamed_by_python.txt
Tables.txt
table_Of_10.txt
table_Of_11.txt
table_Of_12.txt
table_Of_13.txt
table_Of_14.txt
table_Of_15.txt
table_Of_16.txt
table_Of_17.txt
table_Of_18.txt
table_Of_19.txt
table_Of_2.txt
table_Of_20.txt
table_Of_3.txt
table_Of_4.txt
table_Of_5.txt
table_Of_6.txt
table_Of_7.txt
table_Of_8.txt
table_Of_9.txt
this.txt
this_copy.txt
To-Write-a-File.txt
Words-Q5.txt

'''


# 5️⃣)  Usage of os Module :- 

'''

✅ File & Directory Management → Create, delete, and navigate files/folders.

✅ System Information & Environment Variables → Access OS-level data.

✅ Executing System Commands → Run terminal/command prompt commands.

✅ Cross-Platform Compatibility → Works on Windows, macOS, Linux.


'''





# 🕒 Time Module in Python ?

'''

⭐) The time module in Python provides a suite of functions to handle time-related tasks like fetching the current time, pausing program execution, and formatting time values. It is part of Python’s standard library and can be used for operations involving timestamps and delays.

'''


# ✅ Key Features of the Time Module

'''

1) Measure Execution Time :-  Useful for benchmarking or tracking how long specific tasks take.

2) Pause Execution :- Delay program execution for a specified time using functions like time.sleep().

3) Work with Epoch Time :- Fetch and manipulate time since the epoch (January 1, 1970, 00:00:00 UTC).

4) Format Time :- Convert time to readable formats using functions like time.strftime() and time.ctime().

'''


# Example :- 
import time
def usingWhile():
    i = 0
    while i < 5:
        i = i + 1
        print(i)


def usingFor():
    for i in range(5):
        print(i)




init = time.time()

usingFor()
# print(" For Using :- ",time.time() - init)

t1  = time.time() - init 
init = time.time()   
usingWhile()
print("After calling usingwhile() :- ",time.time() - init)
print("Now calling usingFor() at last :- ", t1)



print(4)

time.sleep(3)

print("This is printed after 3 seconds")



t = time.localtime()
formatted_time = time.strftime("%Y - %m - %d %H:%M:%S" , t)

print(formatted_time)

'''

Output :- 

0
1
2
3
4
1
2
3
4
5
After calling usingwhile() :-  1.430511474609375e-05
Now calling usingFor() at last :-  5.7697296142578125e-05
4
This is printed after 3 seconds
2025 - 02 - 16 15:24:54

'''




# 🛠️ Common Functions in the Time Module  ? 

# 1️⃣ time.time()  :- Returns the current time in seconds since the epoch.

# Syntax :-  time.time()

# Example :- 
import time
print(f"Current Time in Seconds: {time.time()}")       # Output :- Current Time in Seconds: 1739719602.236971




# 2️⃣ time.sleep(seconds) :-  Suspends program execution for the specified number of seconds.


# Syntax :- time.sleep(seconds)


# Example :- 
print("Sleeping for 3 seconds...")
time.sleep(3)
print("Woke up!")


'''
Output :- 

Sleeping for 3 seconds...
Woke up!

'''




# 3️⃣ time.localtime() :- Converts the time in seconds (since the epoch) to a struct_time object in local time.

# Syntax :-  time.localtime([seconds])

# Example :- 
local_time = time.localtime()
print(f"Local Time: {local_time}")    # Output :- Local Time: time.struct_time(tm_year=2025, tm_mon=2, tm_mday=16, tm_hour=15, tm_min=31, tm_sec=29, tm_wday=6, tm_yday=47, tm_isdst=0)





# 4️⃣ time.strftime(format, time_object)  :- Formats a struct_time object as a string according to a specified format.


# Syntax :-    time.strftime(format, time_object)


# Example :- 
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(f"Formatted Local Time: {formatted_time}")      # Output :- Formatted Local Time: 2025-02-16 15:32:48





# 5️⃣ time.ctime()  :-  Converts time in seconds (since the epoch) into a human-readable string.


# Syntax :-    time.ctime([seconds])

# Example :- 
print(f"Human-Readable Time: {time.ctime()}")    # Output :- Human-Readable Time: Sun Feb 16 15:33:52 2025





# 6️⃣ time.perf_counter()  :- High-resolution timer for measuring time intervals.


# Syntax :-    time.perf_counter()


# Example :- 
start = time.perf_counter()
time.sleep(2)
end = time.perf_counter()
print(f"Elapsed Time: {end - start:.2f} seconds")          # Output :- Elapsed Time: 2.00 seconds




# 7️⃣ time.gmtime()  :-   Converts seconds (since the epoch) to struct_time in UTC.


# Syntax :-    time.gmtime([seconds])


# Example :- 
print(f"GMT Time: {time.gmtime()}")          # Output :- GMT Time: time.struct_time(tm_year=2025, tm_mon=2, tm_mday=16, tm_hour=15, tm_min=35, tm_sec=59, tm_wday=6, tm_yday=47, tm_isdst=0)





# 📚 How Does the time Module Work?

'''

1️⃣) Epoch Time :-  Most functions in the time module work with time as the number of seconds since the epoch.

2️⃣) Time Objects :-  Functions like time.localtime() and time.gmtime() 
return a struct_time object with attributes such as tm_year, tm_mon, etc.

3️⃣) Delays and Timers :-  Functions like time.sleep() and time.perf_counter() allow you to control program flow and measure time intervals.

'''



# Shutil Module in Python ? 

'''
⭐) The shutil module in Python is a part of the standard library and provides high-level operations for file and directory management. It simplifies tasks like copying, moving, removing files and directories, and even managing file metadata. It is particularly useful when you need to work with files or directories in a programmatic way.

'''



# ✅ Key Features of the Shutil Module

'''

1️⃣) File Operations :- 

    a) Copying files or metadata 
      
    b) Moving or renaming files.

    c) Deleting files or directories.

    
2️⃣) Directory Operations :- 

    a) Copying entire directories.

    b) Archiving directories (e.g., 
    creating ZIP or TAR files).


3️⃣) Disk Space Handling :- 

    a)  Checking available disk space.

4️⃣) Advanced File Management  :- 

    a) Manipulating file permissions and symbolic links.'''



# 📚 Commonly Used Functions ? 

'''
1️⃣ Copying Files :- 
      
    a) shutil.copy(src, dst) :- Copies the content of a file from src to dst.

        If dst is a directory, the file is copied into that directory with the same name.

        Does not copy file metadata (like permissions).

'''

# Example :- 

import shutil

shutil.copy("source.txt" , "destination.txt")


''''

    b) shutil.copy2(src, dst) :- Similar to copy(), but also copies metadata like timestamps and permissions.

'''

# Example :- 

shutil.copy2("source.txt", "destination.txt")



'''

    c) shutil.copytree(src, dst) :-  This function recursively copies the directory located at src to a new location specified by dst. If the destination location already exists, the original directory will be merged with it.

'''

# Example :- 

# Copying a directory
shutil.copytree("src_dir", "dst_dir")




'''

2️⃣ Moving or Renaming Files 
  
       a) shutil.move(src, dst)  :- Moves a file or directory from src to dst.  If the destination exists, it may overwrite it.

'''

       
# Example :- 
shutil.move("source.txt", "new_folder/source.txt")



'''

3️⃣ Deleting Files or Directories  :- 

      
       a) shutil.rmtree(path)  :- Recursively deletes a directory and all its contents.

'''

# Example :- 
shutil.rmtree("my_directory")




'''

4️⃣ Archiving Directories  :- 
 

          a) shutil.make_archive(base_name, format, root_dir) :-  Creates an archive (e.g., ZIP or TAR) from a directory.

          Parameters :- 

            base_name :-  Name of the archive file to create.

            format :-  Archive format (e.g., 'zip', 'tar').

            root_dir :-  The directory to archive.
            
'''


# Example :- 
shutil.make_archive("backup", "zip", "my_directory")


'''         
           b) shutil.unpack_archive(filename, extract_dir) :- Extracts an archive into a directory.

'''


# Example :- 
shutil.unpack_archive("backup.zip", "extracted_files")



'''
5️⃣ Disk Space Utilities 

           a) shutil.disk_usage(path) :- Returns the total, used, and free disk space for a given path.

'''

# Example :- 
import shutil

usage = shutil.disk_usage("/")
print(f"Total: {usage.total // (1024 ** 3)} GB")
print(f"Used: {usage.used // (1024 ** 3)} GB")
print(f"Free: {usage.free // (1024 ** 3)} GB")




'''
6️⃣ File Permissions and Metadata :- 

            a) shutil.chown(path, user=None, group=None) :- Changes the owner and group of a file or directory.

'''


# Example :- 
shutil.chown("file.txt", user="username", group="groupname")



'''

           b) shutil.copystat(src, dst) :- Copies metadata (e.g., timestamps, permissions) from src to dst.

'''


# Example :- 
shutil.copystat("source.txt", "destination.txt")





# Requests Module in Python  ? 

'''

⭐) The requests module in Python is a popular and user-friendly library for making HTTP requests. It simplifies the process of sending HTTP/1.1 requests, such as GET, POST, PUT, DELETE, and more, without requiring manual handling of sockets, headers, or other low-level details.

'''


# ✅ Key Features of the Requests Module  :- 

'''

1️⃣) Easy-to-use interface for making HTTP requests.

2️⃣) Supports standard HTTP methods (e.g., GET, POST, PUT, DELETE).

3️⃣) Handles request headers, query parameters, and cookies seamlessly.

4️⃣) Built-in support for SSL/TLS and automatic redirection.

5️⃣) Provides response objects with methods to access status codes, headers, and content.

6️⃣) Offers robust support for JSON data.

'''


# 📦 Installation  :- Before using the requests module, ensure it is installed. You can install it via pip .  pip install requests



# ✅ Basic Syntax :-  response = requests.method(url, params=None, data=None, headers=None, json=None)


'''
method :-  HTTP method (e.g., get, post, put, etc.).
url :-  URL to send the request to.
params :-  Dictionary of query string parameters.
data :-  Dictionary of form data (for POST requests).
headers :-  Dictionary of HTTP headers.
json :-  Dictionary of JSON data to send in the request.

'''


# 📚 Commonly Used Methods ? 


# 1️⃣ GET Request  :- Used to retrieve data from a server.


# Syntax :-   response = requests.get(url, params=None, headers=None)


# Example :- 
# import requests

url = "https://api.github.com"
response = requests.get(url)

print(response.status_code)  # Status code (e.g., 200)
print(response.headers)      # Headers of the response
print(response.text)         # Response body as a string




# 2️⃣ POST Request :- Used to send data to a server.


# Syntax :-  response = requests.post(url, data=None, json=None, headers=None)


# Example :-

url = "https://httpbin.org/post"
data = {"key": "value"}
response = requests.post(url, json=data)

print(response.status_code)
print(response.json())  # Parses JSON response




# 3️⃣ PUT Request :- Used to update data on the server.


# Syntax :- response = requests.put(url, data=None, json=None)


# Example :- 
url = "https://httpbin.org/put"
data = {"key": "new_value"}
response = requests.put(url, json=data)

print(response.status_code)
print(response.json())




# 4️⃣ DELETE Request :- Used to delete data on the server.


# Syntax  :- response = requests.delete(url)


# Example :- 
url = "https://httpbin.org/delete"
response = requests.delete(url)

print(response.status_code)
print(response.json())




# bs4 Module  :- There is another module called BeautifulSoup which is used for web scraping in Python. I have personally used bs4 module to finish a lot of freelancing task.



import requests  # type: ignore
from bs4 import BeautifulSoup # type: ignore
url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"
r = requests.get(url)
# print(r.text)


soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
for heading in soup.find_all("h2"):
  print(heading.text)


url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": 'harry',
    "body": 'bhai',
    "userId": 12,
  }
headers =  {
    'Content-type': 'application/json; charset=UTF-8',
  }
response = requests.post(url, headers=headers, json=data)

print(response.text)