name = "Harry"
print(type(name))

# Slicing 

nameShort = name[0:3] # Start from index 0 all the way till 3 (excluding 3)
print(nameShort)


print(name[-4 : -1])
print(name[1: 4])

print(name[:4])  # is same as print(name[0:4])
print(name[1:])  # is same as print(name[1:5])
print(name[1:5])


# Slicing With Skip Value
word = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(word[1:6:2]) 
print(word[1:9]) 
print(word[1:9:4]) 


# String Functions 
# 1. len() :- Returns the length of the string.

s = "Hello, World!"
print(len(s))  # Output: 13

# 2. str.lower() :- Converts all characters in the string to lowercase.

s = "Hello, World!"
print(s.lower())  # Output: hello, world!

# 3. str.upper() :- Converts all characters in the string to uppercase.

s = "Hello, World!"
print(s.upper())  # Output: HELLO, WORLD!

# 4. str.title() :- Converts the first character of each word to uppercase and the remaining characters to lowercase.

s = "hello, world!"
print(s.title())  # Output: Hello, World!

# 5. str.capitalize() :- Capitalizes the first character of the string.

s = "hello, world!"
print(s.capitalize())  # Output: Hello, world!

# 6. str.casefold() :- Converts the string to lowercase for case insensitive comparisons.

s = "HELLO, WORLD!"
print(s.casefold())  # Output: hello, world!

# 7. str.strip() :- Removes leading and trailing whitespace from the string.


s = "   Hello, World!   "
print(s.strip())  # Output: "Hello, World!"

# 8. str.lstrip() :- Removes leading whitespace from the string.

s = "   Hello, World!"
print(s.lstrip())  # Output: "Hello, World!"

# 9. str.rstrip() :- Removes trailing whitespace from the string.

s = "Hello, World!   "
print(s.rstrip())  # Output: "Hello, World!"

# 10. str.split() :- Splits the string into a list of substrings based on the specified delimiter (default is whitespace).

s = "Hello, World!"
print(s.split())  # Output: ['Hello,', 'World!']

# 11. str.rsplit() :- Splits the string from the right based on the specified delimiter.


s = "apple, banana, cherry"
print(s.rsplit(", ", 1))  # Output: ['apple, banana', 'cherry']

# 12. str.splitlines() :- Splits the string at line breaks and returns a list.

s = "Hello\nWorld!"
print(s.splitlines())  # Output: ['Hello', 'World!']

# 13. str.join() :- Joins the elements of an iterable (like a list) into a single string, with a specified separator.

words = ["Hello", "World"]
print(" ".join(words))  # Output: Hello World

# 14. str.find() :- Returns the index of the first occurrence of a substring. Returns -1 if the substring is not found.

s = "Hello, World!"
print(s.find("World"))  # Output: 7

# 15. str.rfind() :- Returns the highest index of the substring if found. Returns -1 if not found.

s = "Hello, World! World!"
print(s.rfind("World"))  # Output: 14

# 16. str.index() :- Returns the index of the first occurrence of a substring. Raises ValueError if the substring is not found.

s = "Hello, World!"
print(s.index("World"))  # Output: 7

# 17. str.rindex() :- Returns the highest index of the substring if found. Raises ValueError if the substring is not found.

s = "Hello, World! World!"
print(s.rindex("World"))  # Output: 14

# 18. str.replace() :- Replaces all occurrences of a substring with another substring.

s = "Hello, World!"
print(s.replace("World", "Python"))  # Output: Hello, Python!

# 19. str.startswith() :- Checks if the string starts with a specified prefix. Returns True or False.

s = "Hello, World!"
print(s.startswith("Hello"))  # Output: True

# 20. str.endswith() :- Checks if the string ends with a specified suffix. Returns True or False.

s = "Hello, World!"
print(s.endswith("World!"))  # Output: True

# 21. str.isdigit() :- Checks if all characters in the string are digits. Returns True or False.

s = "12345"
print(s.isdigit())  # Output: True

# 22. str.isalpha() :- Checks if all characters in the string are alphabetic. Returns True or False.

s = "Hello"
print(s.isalpha())  # Output: True

# 23. str.isalnum() :- Checks if all characters in the string are alphanumeric (letters and digits). Returns True or False.

s = "Hello123"
print(s.isalnum())  # Output: True

# 24. str.islower() :- Checks if all characters in the string are lowercase. Returns True or False.

s = "hello"
print(s.islower())  # Output: True

# 25. str.isupper() :- Checks if all characters in the string are uppercase. Returns True or False.

s = "HELLO"
print(s.isupper())  # Output: True

# 26. str.isspace() :- Checks if all characters in the string are whitespace. Returns True or False.

s = "   "
print(s.isspace())  # Output: True

# 27. str.istitle() :- Checks if the string is titlecased. Returns True or False.

s = "Hello World"
print(s.istitle())  # Output: True

# 28. str.zfill() :- Pads the string on the left with zeros to fill a width.

s = "42"
print(s.zfill(5))  # Output: 00042

# 29. str.ljust() :- Left-justifies the string in a field of a given width.

s = "Hello"
print(s.ljust(10, '-'))  # Output: Hello-----

# 30. str.rjust() :- Right-justifies the string in a field of a given width.

s = "Hello"
print(s.rjust(10, '-'))  # Output: -----Hello

# 31. str.center() :- Centers the string in a field of a given width.

s = "Hello"
print(s.center(11, '-'))  # Output: ---Hello---

# 32. str.partition() :- Splits the string into three parts: the part before the separator, the separator itself, and the part after the separator.

s = "Hello, World!"
print(s.partition(", "))  # Output: ('Hello', ', ', 'World!')

# 33. str.rpartition() :- Splits the string into three parts using the last occurrence of the separator.

s = "Hello, World, Python!"
print(s.rpartition(", "))  # Output: ('Hello, World', ', ', 'Python!')

# 34. str.count() :- Returns the number of non-overlapping occurrences of a substring.

s = "Hello, World! Hello, Python!"
print(s.count("Hello"))  # Output: 2

# 35. str.expandtabs() :- Replaces tab characters with spaces.

s = "Hello\tWorld!"
print(s.expandtabs(4))  # Output: Hello   World!

# 36. str.encode() :- Encodes the string using the specified encoding.

s = "Hello, World!"
print(s.encode('utf-8'))  # Output: b'Hello, World!'



# Escape Sequence Characters 
# 1) Newline (\n): Inserts a new line in the text at the specified position.

text = "Hello, World!\nWelcome to Python."
print(text)
# Output:
# Hello, World!
# Welcome to Python.

# 2) Tab (\t): Inserts a horizontal tab.

text = "Hello,\tWorld!"
print(text)
# Output: Hello,   World!

# 3) Backslash (\\): Inserts a backslash character.

text = "This is a backslash: \\"
print(text)
# Output: This is a backslash: \

# 4) Single Quote (\'): Inserts a single quote character.

text = 'It\'s a beautiful day!'
print(text)
# Output: It's a beautiful day!

# 5) Double Quote (\") :- Inserts a double quote character.

text = "She said, \"Hello!\""
print(text)
# Output: She said, "Hello!"

# 6) Carriage Return (\r) :- Moves the cursor to the beginning of the line.

text = "Hello, World!\rWelcome"
print(text)
# Output: Welcome, World!

# 7) Bell (\a): Triggers the system bell.

text = "Alert!\a"
print(text)
# Output: Alert! (and you will hear a bell sound)


# 8) Backspace (\b): Inserts a backspace, deleting the previous character.

text = "Hello,\b World!"
print(text)
# Output: Hell, World!

# 9) Formfeed (\f): Inserts a form feed.

text = "Hello,\fWorld!"
print(text)
# Output: Hello,
#          World!

# 10) Octal Value (\ooo): Represents a character by its octal value.

text = "\101\102\103"
print(text)
# Output: ABC

# 11) Hexadecimal Value (\xhh): Represents a character by its hexadecimal value.

text = "\x48\x65\x6c\x6c\x6f"
print(text)
# Output: Hello

