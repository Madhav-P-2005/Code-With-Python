# Functions :- A function is a block of organized, reusable code that is used to perform a single, related action. Functions provide better modularity for your application and a high degree of code reusing.

# Advantages of functions :- 
'''

1) Functions are important in programming because they are used to process
data, make calculations or perform any task which is required in the software
development.

2) Once a function is written, it can be reused as and when required. So functions
are also called reusable code.

3) When there is an error in software , the corresponding function can be
modified without disturbing the other functions in the software.

4) Will reduce the length of the program.


'''

# Difference between Function and Method :-
'''

●) Function contains a group of statements and performs a specific task.

●) A function can be written individually in a Python program.

●) A function is called using its name. When a function is written inside a class, it
becomes a 'method‘.

●) A method is called using one of the following ways :-
             objectname.methodname()
             classname.methodname()

●) Function and a method are same except their placement and the way they are called.


'''

# Defining a Function :- 
'''

Here are simple rules to define a function in Python.

●) Function blocks begin with the keyword def followed by the function name and
parentheses ( ( ) ).

●) Any input parameters or arguments should be placed within

these parentheses. Define parameters inside these parentheses.

●) The first statement of a function can be an optional statement - the documentation string of the function.

●) The code block within every function starts with a colon (:) and is indented.

●) The statement return [expression] exits a function, optionally passing back an expression to the caller. A return statement with no arguments returns nothing.

'''

# Syntax:- 
''' 
   def function_name(parameters):
          """docstring"""
        statement(s)

'''

# Example :- 
def greet(name):
    print("Hello, " + name + ". Good morning!")
'''

This function greets to
the person passed in as
a parameter

'''

