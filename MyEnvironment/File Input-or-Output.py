# FILE HANDLING IN PYTHON

#  File handling is an important part of any web application.
#  Python has several functions for creating, reading, updating, and deleting files. \


# File Handling

# The key function for working with files in Python is the open() function. The open() function takes two parameters; filename, and mode. There are four different methods (modes) for opening a file:
'''

1. &quot;r&quot; - Read - Default value. Opens a file for reading, error if the file does not exist
2. &quot;a&quot; - Append - Opens a file for appending, creates the file if it does not exist
3. &quot;w&quot; - Write - Opens a file for writing, creates the file if it does not exist
4. &quot;x&quot; - Create - Creates the specified file, returns an error if the file exists
In addition you can specify if the file should be handled as binary or text mode
1. &quot;t&quot; - Text - Default value. Text mode
2. &quot;b&quot; - Binary - Binary mode.(Example:Images)

'''