name = "Harry"
print(type(name))          # Output :-   <class 'str'>

# Slicing :- 

# slice(start, stop[, step])

'''

    i)  Start is the starting index from which we need to slice the array arr. By
    default set to 0.

    ii)  stop is the ending index, before which the slicing operation would end. By
    default equal to the length of the array.

    iii) step is the steps the slicing process would take from start to stop. By default
    set to 1.
    
'''

nameShort = name[0:3] # Start from index 0 all the way till 3 (excluding 3)
print(nameShort)        # Output :- Har


print(name[-4 : -1])    # Output :-  arr

print(name[1: 4])       # Output :-  arr 

print(name[:4])  # is same as print(name[0:4])       # Output :- Harr

print(name[1:])  # is same as print(name[1:5])       # Output :- arry

print(name[1:5])       # Output :-  arry
print()




# Slicing With Skip Value
word = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print(word[1:6:2])     # Output :-   BDF

print(word[1:9])       # Output :-   BCDEFGHI

print(word[1:9:4])     # Output :-   BF
print()



# Repeating the Strings :-  The repetition operator is denoted by '*'symbol and is useful to repeat the string for several times. For example, str * n repeats the string for n times.
str = 'Core Python '
print(str * 2)         # Output :-  Core Python Core Python 

print()

s = str[5:7] * 3
print(s)               # Output :-  PyPyPy
print()



# Python Concatenation Strings :- We can use '+' on strings to attach a string at the end of another string. This operator '+' is called addition operator when used on numbers. But, when used on strings, it is called 'concatenation ' operator since it joins or concatenates the strings.

s1 = 'Core'
s2 = "Python"
s3 = s1 + " " +  s2
print("Concatenated output :- ", s3)           # Output :-   Concatenated output :-  Core Python
print()



# String Functions 

# 1) len() :- Returns the length of the string.

s = "Hello, World!"

print(len(s))            # Output :-  13



# 2) str.lower() :- Converts all characters in the string to lowercase.

s = "Hello, World!"

print(s.lower())         # Output :-  hello, world!



# 3) str.upper() :- Converts all characters in the string to uppercase.

s = "Hello, World!"

print(s.upper())         # Output :-  HELLO, WORLD!



# 4) str.title() :- Converts the first character of each word to uppercase and the remaining characters to lowercase.

s = "hello, world!"

print(s.title())         # Output :-  Hello, World!



# 5) str.capitalize() :- Capitalizes the first character of the string.

s = "hello, world!"

print(s.capitalize())    # Output :-  Hello, world!



# 6) str.casefold() :- Converts the string to lowercase for case insensitive comparisons.

s = "HELLO, WORLD!"

print(s.casefold())      # Output :-  hello, world!



# 7) str.strip() :- Removes leading and trailing whitespace from the string.


s = "   Hello, World!   "

print(s.strip())        # Output :-  "Hello, World!"



# 8) str.lstrip() :- Removes leading whitespace from the string.

s = "   Hello, World!"

print(s.lstrip())       # Output :-  "Hello, World!"



# 9) str.rstrip() :- Removes trailing whitespace from the string.

s = "Hello, World!   "

print(s.rstrip())       # Output :-  "Hello, World!"



# 10)  str.split() :- Splits the string into a list of substrings based on the specified delimiter (default is whitespace).

s = "Hello, World!"

print(s.split())       # Output :-  ['Hello,', 'World!']



# 11) str.rsplit() :-  Splits the string from the right based on the specified delimiter.


s = "apple, banana, cherry"

print(s.rsplit(", ", 1))         # Output :-  ['apple, banana', 'cherry']



# 12) str.splitlines() :-  Splits the string at line breaks and returns a list.

s = "Hello\nWorld!"

print(s.splitlines())         # Output :-  ['Hello', 'World!']



# 13) str.join() :-   Joins the elements of an iterable (like a list) into a single string, with a specified separator.

words = ["Hello", "World"]

print(" ".join(words))        # Output :-  Hello World



# 14) str.find() :-   Returns the index of the first occurrence of a substring. Returns -1 if the substring is not found.

s = "Hello, World!"

print(s.find("World"))       # Output :-  7



# 15) str.rfind() :-   Returns the highest index of the substring if found. Returns -1 if not found.

s = "Hello, World! World!"

print(s.rfind("World"))      # Output :-  14



# 16) str.index() :-  Returns the index of the first occurrence of a substring. Raises ValueError if the substring is not found.

s = "Hello, World!"

print(s.index("World"))      # Output :-  7



# 17) str.rindex() :-  Returns the highest index of the substring if found. Raises ValueError if the substring is not found.

s = "Hello, World! World!"

print(s.rindex("World"))      # Output :-  14



# 18) str.replace() :-  Replaces all occurrences of a substring with another substring.

s = "Hello, World!"

print(s.replace("World", "Python"))     # Output :-  Hello, Python!



# 19) str.startswith() :- Checks if the string starts with a specified prefix. Returns True or False.

s = "Hello, World!"

print(s.startswith("Hello"))          # Output :- True



# 20) str.endswith() :- Checks if the string ends with a specified suffix. Returns True or False.

s = "Hello, World!"

print(s.endswith("World!"))          # Output :-  True



# 21) str.isdigit() :- Checks if all characters in the string are digits. Returns True or False.

s = "12345"

print(s.isdigit())                  # Output :-  True



# 22) str.isalpha() :-   Checks if all characters in the string are alphabetic. Returns True or False.

s = "Hello"

print(s.isalpha())               # Output :-  True



# 23) str.isalnum() :-   Checks if all characters in the string are alphanumeric (letters and digits). Returns True or False.

s = "Hello123"

print(s.isalnum())              # Output :-  True



# 24) str.islower() :-   Checks if all characters in the string are lowercase. Returns True or False.

s = "hello"

print(s.islower())        # Output :-  True



# 25) str.isupper() :-  Checks if all characters in the string are uppercase. Returns True or False.

s = "HELLO"

print(s.isupper())        # Output :-  True



# 26) str.isspace() :-  Checks if all characters in the string are whitespace. Returns True or False.

s = "   "

print(s.isspace())       # Output :-  True



# 27) str.istitle() :-  Checks if the string is titlecased. Returns True or False.

s = "Hello World"

print(s.istitle())       # Output :-  True



# 28) str.zfill() :-  Pads the string on the left with zeros to fill a width.

s = "42"

print(s.zfill(5))       # Output :-  00042



# 29) str.ljust() :-  Left-justifies the string in a field of a given width.

s = "Hello"

print(s.ljust(10, '-'))     # Output :-  Hello-----



# 30) str.rjust() :-   Right-justifies the string in a field of a given width.

s = "Hello"

print(s.rjust(10, '-'))     # Output :-  -----Hello



# 31) str.center() :-   Centers the string in a field of a given width.

s = "Hello"

print(s.center(11, '-'))    # Output :-  ---Hello---



# 32) str.partition() :-  Splits the string into three parts: the part before the separator, the separator itself, and the part after the separator.

s = "Hello, World!"

print(s.partition(", "))      # Output :-   ('Hello', ', ', 'World!')



# 33) str.rpartition() :- Splits the string into three parts using the last occurrence of the separator.

s = "Hello, World, Python!"

print(s.rpartition(", "))      # Output :-  ('Hello, World', ', ', 'Python!')



# 34) str.count() :-  Returns the number of non-overlapping occurrences of a substring.

s = "Hello, World! Hello, Python!"

print(s.count("Hello"))        # Output :-  2



# 35) str.expandtabs() :-   Replaces tab characters with spaces.

s = "Hello\tWorld!"

print(s.expandtabs(4))        # Output :-  Hello   World!



# 36) str.encode() :-  Encodes the string using the specified encoding.

s = "Hello, World!"

print(s.encode('utf-8'))      # Output :-  b'Hello, World!'



# Escape Sequence Characters 
# 1) Newline (\n) :-  Inserts a new line in the text at the specified position.

text = "Hello, World!\nWelcome to Python."
print(text)

'''
Output :- 

Hello, World!
Welcome to Python.

'''



# 2) Tab (\t) :-  Inserts a horizontal tab.

text = "Hello,\tWorld!"

print(text)         # Output :-  Hello,   World!



# 3) Backslash (\\) :-  Inserts a backslash character.

text = "This is a backslash: \\"

print(text)         # Output :-  This is a backslash: \



# 4) Single Quote (\') :-   Inserts a single quote character.

text = 'It\'s a beautiful day!'
print(text)         # Output :-  It's a beautiful day!



# 5) Double Quote (\") :-  Inserts a double quote character.

text = "She said, \"Hello!\""

print(text)         # Output :-  She said, "Hello!"



# 6) Carriage Return (\r) :-  Moves the cursor to the beginning of the line.

text = "Hello, World!\rWelcome"

print(text)        # Output :-  Welcome, World!



# 7) Bell (\a) :-   Triggers the system bell.

text = "Alert!\a"

print(text)        # Output :-  Alert! (and you will hear a bell sound)



# 8) Backspace (\b) :-  Inserts a backspace, deleting the previous character.

text = "Hello,\b World!"

print(text)       # Output :-  Hell, World!



# 9) Formfeed (\f) :-  Inserts a form feed.

text = "Hello,\fWorld!"

print(text)

'''

Output :-  Hello,
             World!
             
'''



# 10) Octal Value (\ooo) :-  Represents a character by its octal value.

text = "\101\102\103"

print(text)           # Output :-  ABC



# 11) Hexadecimal Value (\xhh) :-  Represents a character by its hexadecimal value.

text = "\x48\x65\x6c\x6c\x6f"

print(text)            # Output :-  Hello





# Q1) Write a Python program to demonstrate String Operators ? 


The_Dark_Knight = "Why do we fall , Bruce ?"
n = len(The_Dark_Knight)
print("The Length of the String is :- ",n)
print("Accessing the last element of the string  :- ",The_Dark_Knight[-1])


# Using for loop 
print("The Reverse order of the string (Using for loop):- ")
for i in range(1,n):
    print(The_Dark_Knight[-i] , end=" ")
    i+=1
    
    
print()
    
    
# Using While Loop
print("The Reverse order of the string (Using while loop):- ")
i=1
while(i<=n):
    print(The_Dark_Knight[-i], end=" ")
    i+=1

print()

str1 = input("Enter the element to be Replaced from the String ? :- ")
str2 = input("Enter the element to be Added to the Replaced position String ? :- ")


New_String = The_Dark_Knight.replace(str1, str2)

print(New_String)
    
    


'''

Output :- 


The Length of the String is :-  24

Accessing the last element of the string  :-  ?

The Reverse order of the string (Using for loop):- 
?   e c u r B   ,   l l a f   e w   o d   y h 

The Reverse order of the string (Using while loop):- 
?   e c u r B   ,   l l a f   e w   o d   y h W 

Enter the element to be Replaced from the String ? :- f

Enter the element to be Added to the Replaced position String ? :- T

Why do we Tall , Bruce ?


'''