# Match Case :- 

# 1. When Was It Released ?

'''

>> Introduced :-  Python 3.10 (Released on October 4, 2021).
>> Part of PEP 634 :-  Specification for Structural Pattern Matching.

'''


# What Is match Statement ?

'''

-> The match statement allows you to compare a value against a series of patterns and execute code based on which pattern matches. It’s similar to switch-case in other languages but is far more versatile, as it supports :- 


  1) Matching on literals, types, or structures (like tuples, lists, dictionaries, etc.).

  2) Capturing values.

  3) Nested patterns.


'''

# Syntax of match :- 

'''

match <expression>:
     case <pattern1>:
          # Code block for pattern1
     case <pattern2>:
          # Code block for pattern2
     case _:
          # Default case (if no other patterns match)

'''


# Key Components : - 

'''

  1) <expression> :-  The value being matched (e.g., a variable or function result).

  2) <pattern> :-  The conditions to check against the value.

  3)  _ :-   The wildcard pattern (matches anything, similar to a default case in switch).

'''


# Using Wildcards (_) :- ' _ '  is a wildcard pattern that matches anything. It is equivalent to the default case in other languages.



# Basic Example :- 
def http_status(status):
        match status:
                case 200:
                        return "Ok"
                case 404:
                        return "Not Found"
                case 500:
                        return "Internal Server Error"
                case _:
                        return "Unknown Status"

print(http_status(200))   # Output :- Ok
print(http_status(404))   # Output :- Not Found
print(http_status(500))   # Output :- Internal Server Error
print(http_status(346436))   # Output :- Unknown Status



# Matching Literals :-

x = 10

match x:
        case 1: 
                print("It's one.")
        case 10:
                print("It's ten.")
        case _:
                print("It's something else. ")

'''

Output :-  Its 's  ten .

'''

# Matching Data Structures :- You can match tuples , list , or dictionaries 

# a) Matching Tuples :- 

point = (1 , 2)


match point:
          case (0,0):
                print("Origin")
          case (x , y):
                print(f"Point at x is {x} , y is {y}")


'''

Output :-  Point at x is 1 , y is 2

'''




# b) Matching Lists :-

items = [1,2,3,4,5]

match items:
        case [1,2,3]:
                print("Exact numbers ")   
        case [1,*_]:
                print("starts with 1 . ")
        case _:
                print("No match")


'''

Output :- Exact numbers

'''


items = [1,...]

match items:
        case [1,2,3]:
                print("Exact numbers ")   
        case [1,_]:
                print("starts with 1 . ")
        case _:
                print("No match")


'''

Output :-  starts with 1 .

'''

# [1, _] vs. [1, *_] :- 

# Case 1: [1, _] :-  This pattern matches a list with exactly two elements, where the first element is 1, and the second element can be any single value.

# Case 2: [1, *_] :- This pattern matches a list with one or more elements, where the first element is 1, and the rest of the list (0 or more elements) is captured by the wildcard *_.


# c) Matching Dictionaries :- 

person = {"name" : "Madhav" , "age" : 25}

match person:
        case {"name" : "Alice", "age" : age}:
                print(f" Alice is {age} years old")
        case {"name" : name}:
                print(f"Found someone named {name}")
        case _:
                print("No match")


'''

Output :-  Found someone named Madhav

'''




# d)  Matching with Type Guards :- You can match patterns based on types.

value = 34.88

match value:
        case int():
                print("Its an integer . ")
        case float():
                print("Its's a float")
        case _:
                print("Its something else.")

'''

Output :- Its's a float

'''


# How Does It Work ? :- 

'''

1) The match expression evaluates the provided value (the subject).

2) It tries to match the value against each case pattern sequentially.

3) If a pattern matches :- 
    >> The corresponding block of code is executed.
    >> The matching process stops (no further patterns are checked).

4) If no patterns match :- 
    >>  _ case (if present) is executed.
    >>  If _ is not present, no action is taken.'''


# Why Use match? (Advantages) :- 

'''

1) Clean Code :-  Makes complex conditional logic (e.g., nested if-elif-else) easier to read.

2) Expressiveness :-  Supports pattern matching for literals, types, and structures like lists, tuples, and dictionaries.

3) Extensibility :-  Makes it easier to handle complex data-driven logic (e.g., parsing, deconstructing nested data).

4) Error-Prone Conditions :-  Eliminates repetitive checks like if var == value1.

'''

# Limitations of match :-  

'''

  1) Only available in Python 3.10 and later.

  2) Does not work with non-exhaustive patterns (if none of the patterns match and there's no _, no action occurs).

  3) Not as performant for very simple conditions compared to if-elif.

'''



