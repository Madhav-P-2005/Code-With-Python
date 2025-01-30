# Definition 

'''

>> The format() method in Python is used to format strings dynamically by inserting variables, expressions, or other values into placeholders {}. It provides a flexible and powerful way to create customized and readable strings.

'''



# Syntax :-    "string with placeholders {}".format(values)



# Key Points :- 

'''

1) Placeholders :-  Represented by {} in the string.

2) Arguments :-  Values provided inside .format() replace the placeholders.

3) Positional or Named Arguments :-  Placeholders can use positional indexes or named keywords.

'''




# How Does It Work ?
 
'''

1) The string contains placeholders {} where dynamic values will be inserted.

2) The format() method takes arguments and maps them to these placeholders.

3) The method supports various formatting options like alignment, padding, and precision.

'''


# Example 1 :- 

a = "{} is a good {}".format("harry", "boy")


print(a)    # Output :-  harry is a good boy




# Example 2 :-  Using Indexes for Positional Arguments:

a = "{1} is a good {0}".format("harry", "boy")


print(a)    # Output :-  boy is a good harry




# Example 3 :-  Basic Formatting with Positional Arguments

name = "Alice"
age = 25
message = "My name is {} and I am {} years old.".format(name, age)


print(message)    # Output: My name is Alice and I am 25 years old.




# Example 4 :-  Named Arguments

message = "My name is {name} and I live in {city}.".format(name="Alice", city="Paris")


print(message)       # Output: My name is Alice and I live in Paris.



# Example 5 :-   Mixing Positional and Keyword Arguments

message = "I scored {0} in Math and {science} in Science.".format(95, science=98)


print(message)        # Output: I scored 95 in Math and 98 in Science.




# Example 6 :-  Formatting Numbers (Precision)

pi = 3.14159
message = "The value of pi is {:.2f}".format(pi)


print(message)       # Output: The value of pi is 3.14


# Example 6 :-  Formatting Numbers (Precision)

pi = 3.14159
message = "The value of pi is {:.2f}".format(pi)


print(message)       # Output: The value of pi is 3.14


# Example 6 :-  Formatting Numbers (Precision)

pi = 3.14159
message = "The value of pi is {:.2f}".format(pi)


print(message)       # Output: The value of pi is 3.14





# Advantages of format() :- 

'''

1) Flexibility: Supports positional, named, and mixed arguments.

2) Readability: Makes complex string formatting easy to understand.

3) Powerful: Offers advanced formatting options like alignment, padding, and type-specific formats.

'''




# Comparison with F-Strings (Python 3.6+) :-

'''

>> While format() is powerful, f-strings (f"{variable}") are more concise and often preferred in modern Python code. 

'''



