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

# Calling a Function :- Once we have defined a function, we can call it from another function, program, or even the Python prompt. To call a function we simply type the function name with appropriate parameters.
# example :- 
def greet(name):
  print("Hello, " + name + ". Good morning!")

greet("XYZ")



# Returning results from function :- We can return the result or output from the function using the return statement in the body of the function.

# Example :- 
def square_value(num):
    """This function returns the square
value of the entered number"""
    return num**2
print(square_value(2))
print(square_value(-4))


# Returning multiple values :- A Python program to return multiple values from a method using tuple

# This function returns a tuple
def fun():
  str = "geeksforgeeks"
  x = 20
  #  return str, x; # Return tuple, can also be written (str, x)
  return (str,x)

# Driver code to test above method
# str, x = fun() # Assign returned tuple
# print(str,x)
demo = fun()
print(demo)



# A Python program to return multiple values from a method using list 
# This function returns a list
# def fun():
#   str = "geeksforgeeks"
#   x = 20
#   return [str, x]
# list = fun()
# print(list)


# Finding Average using function

# Function Definition
# def avg():
#    a = int(input("Enter your number :- "))
#    b = int(input("Enter your number :- "))
#    c = int(input("Enter your number :- "))

#    average = (a+b+c)/3
#    print(average)

# avg() # Function Call


# Quick Quiz :- 
# def greet():
#    name = input("Enter your name :-  ")
#    print("Good Day",name)

# greet()


# TYPES OF  FUNCTIONS IN  PYTHON  :- 
'''

There are two types of functions in python :-

• Built in functions (Already present in python) 
• User defined functions (Defined by the user)


'''

# Build In Functions :- 

# 1) print() :- Prints the given objects to the console or a file.

# Syntax :-  print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

# print('Hello, World!') # Output: Hello, World!



# 2) len() :- Returns the length (the number of items) of an object.

# Syntax :- len(s)
# print(len('hello')) # Output: 5



# 3) type() :- Returns the type of an object.

# Syntax :-  type(object)
# print(type(5))
# Output: <class 'int'>



# 4) int() :- Converts a number or string to an integer.

# Syntax :- int([x[, base]])
# print(int('10'))
# Output: 10



# 5) str() :- Returns a string version of an object.

# Syntax :- str(object='')
# print(str(123)) # Output: '123'



# 6) input() :- Reads a line from input.

# Syntax :- input([prompt])
# name = input('Enter your name: ')
# print(f'Hello, {name}') # Output: Input prompt and greeting



# 7) sum() :- Returns the sum of an iterable.

# Syntax :- sum(iterable, /, start=0)
# print(sum([1, 2, 3]))
# Output: 6



# 8) max() :- Returns the largest item in an iterable or the largest of two or more arguments.

# Syntax :- max(iterable, *[, key, default])
# print(max([1, 2, 3])) # Output: 3



# 9) min() :- Returns the smallest item in an iterable or the smallest of two or more arguments.

# Syntax :- min(iterable, *[, key, default])
# print(min([1, 2, 3])) # Output: 1



# 10) list() :- Creates a list.

# Syntax :- list([iterable])
# print(list)
# print(list('hello')) # Output: ['h', 'e', 'l', 'l', 'o']



# 11) dict() :- Creates a new dictionary.

# Syntax :- dict([mapping-or-iterable])
# print(dict(a=1, b=2)) # Output: {'a': 1, 'b': 2}



# 12) set() :- Returns a new set object.

# Syntax :- set([iterable])
# print(set([1, 2, 2, 3])) # Output: {1, 2, 3}



# 13) tuple() :- Returns a tuple.

# Syntax :- tuple([iterable])
# print(tuple([1, 2, 3])) # Output: (1, 2, 3)



# 14) range() :- Returns an immutable sequence of numbers.

# Syntax :- range([start,] stop[, step])
# print(list(range(1, 5))) # Output: [1, 2, 3, 4]



# 15) abs() :- Returns the absolute value of a number.

# Syntax :- abs(x)
# print(abs(-5)) # Output: 5



# 16) round() :- Rounds a number to a specified number of decimal places.

# Syntax :- round(number[, ndigits])
# print(round(5.678, 2)) # Output: 5.68



# 17) pow() :- Returns x to the power y.

# Syntax :- pow(x, y[, z])
# print(pow(2, 3)) # Output: 8



# 18) zip() :- Returns an iterator of tuples.

# Syntax :- zip(*iterables)
# print(list(zip([1, 2, 3], ['a', 'b', 'c']))) # Output: [(1, 'a'), (2, 'b'), (3, 'c')]



# 19) enumerate() :- Returns an enumerate object.

# Syntax :- enumerate(iterable[, start=0])
# for i, val in enumerate(['a', 'b', 'c']):
#     print(i, val) 
# Output:
# 0 a
# 1 b
# 2 c



# 20) sorted() :- Returns a new sorted list from the items in an iterable.

# Syntax :- sorted(iterable, *, key=None, reverse=False)
# print(sorted([3, 1, 2])) # Output: [1, 2, 3]



# 21) filter() :- Constructs an iterator from those elements of the iterable for which the function returns true.

# Syntax :- filter(function, iterable)
# print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))) # Output: [2, 4]



# 22) all() :- Returns True if all elements of the iterable are true (or if the iterable is empty).

# Syntax :- all(iterable)
# print(all([True, True, False])) # Output: False



# 23) any() :- Returns True if any element of the iterable is true. If the iterable is empty, returns False.

# Syntax :- any(iterable)
# print(any([False, False, True])) # Output: True



# 24) bool() :- Converts a value to a Boolean, True or False.

# Syntax :- bool(x)
# print(bool(1))
# Output: True
# print(bool(0))
# Output: False



# 25) float() :- Converts a value to a floating-point number.

# Syntax :- float([x])
# print(float(5))
# Output: 5.0



# 26) format(value[, format_spec]) :- Formats a value as a string

# Syntax :- format(value[, format_spec])
# print(format(1234.5678, '.2f'))  # Output: 1234.57



# 27) id(object) :- Returns the identity of an object.

# Syntax :- id(object)
# print(id(5))  # Output: Unique ID for the integer 5



# 28) getattr(object, name[, default]) :- Returns the value of the named attribute of an object.
 
# Syntax :- getattr(object, name[, default])
# class MyClass:
#     attr = 'value'
# obj = MyClass()
# print(getattr(obj, 'attr'))  #



# 29) map(function, iterable, ...) :- Applies a function to every item of an iterable and returns a list of the results.

# Syntax :- map(function, iterable, ...)
# print(list(map(lambda x: x * 2, [1, 2, 3])))  # Output: [2, 4, 6]



# 30) eval(expression[, globals[, locals]]) :- Evaluates the specified expression if it's a valid Python expression.

# Syntax :-  eval(expression[, globals[, locals]])
# print(eval('1 + 2'))  # Output: 3



# Function with Arguments :- 
'''

1) Here, add_numbers(2, 3) specifies that parameters a and b will get values 2 and 3
respectively.

2) When a function is defined, it may have some parameters. These parameters are
useful to receive values from outside of the function. They are called 'formal
arguments'.

3) When we call the function, we should pass data or values to the function. These
values are called 'actual arguments'.

'''

def sum(a, b): # a, b are formal arguments
      c = a+b
      print(c)

# call the function
x=10; y=15
sum(x, y) # x, y are actual arguments



# Return a Value
# def goodDay(name, ending):
#    print("Good Day, " + name)
#    print(ending)
#   #  return "done"
#    return 7

  
# a = goodDay("Harry" , "Thank you")
# # print(a) # output :- done
# print(a) # output :- 7


# The actual arguments used in a function call are of 4 types:
'''
    1) Positional arguments
    2) Keyword arguments
    3) Default arguments
    4) Variable length arguments

'''

# 1) Positional arguments :-  

#  ● An argument is a variable, value or object passed to a function or method as input. Positional arguments are arguments that need to be included in the proper position or order.
#  ● The first positional argument always needs to be listed first when the function is called. The second positional argument needs to be listed second and the third positional argument listed third, etc.

'''

When calling print_line(errors, encoding, line), the arguments are passed in this order :-

a) The first argument errors (value 3) is assigned to encoding.

b) The second argument encoding (value 2) is assigned to errors.

c) The third argument line (value 1) is assigned to line.

'''
# Example :-  
def print_line( encoding  , errors , line ):
    print(line , errors  ,encoding )  # Output: 1 2 3


line = 1
encoding = 2
errors = 3
print_line(errors , encoding , line)


# 2) Keyword arguments :- 

# ● Keyword arguments are related to the function calls.
# ● Using keyword arguments in a function call, the caller identifies the arguments by the parameter name.
# ● Allows to skip arguments or place them out of order, the Python interpreter use the
# ● keywords provided to match the values with parameters.

# Example :- 
def function1(date , year):
    print("date : " , date)  # 20
    print("year : " , year)  # 1975
    return

function1(year=1975 , date=20)



# 3) Default arguments :- 

# ●  Default Argument :- argument that assumes a default value if a value is not provided in the function call for that argument.
# ●  = operator to provide default values.

# Example:
# def add_numbers(a = 7, b = 8):  # here a and b has default values 
#     sum = a + b
#     print('Sum:', sum)


# function call with two arguments
# add_numbers(2, 3)  # Output :- Sum: 5
# # function call with one argument
# add_numbers(a = 2) # Output :- Sum: 10
# # function call with no arguments
# add_numbers()  # Output :- 15



# 4) Variable-length arguments :-  ● In Python, we can pass a variable number of arguments to a function using special symbols. There are two special symbols:

# 1) *args (Non-Keyword Arguments) :-  In Python, *args is used to pass a variable number of arguments to a function. It is used to pass a variable-length, non-keyworded argument list. These arguments are collected into a tuple within the function and allow us to work with them.

# Example 1 :- 
# Python program to illustrate *args for variable number of arguments
def myFun(*argv):
   for arg in argv: 
      print(arg)


myFun('Hello', 'Welcome', 'to', 'Hubli')


# Example2:
# program to find sum of multiple numbers
def find_sum(*numbers):
      result = 0
      for num in numbers:
        result = result + num
        print("Sum = ", result)


# function call with 3 arguments
find_sum(1, 2, 3)
# function call with 2 arguments
find_sum(4, 9)



# 2) **kwargs (Keyword Arguments) :- In Python, **kwargs is used to pass a keyworded, variable-length argument list. We call kwargs with a double star. The reason for this is that the double star allows us to pass over keyword arguments (in any order). Arguments are collected into a dictionary within the function that allow us to access them by their keys.

# Example:
# Python program to illustrate
# *kwargs for variable number of keyword arguments
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

# Driver code
myFun(first='hello', mid='welcome to', last='Hubli')


# Local and Global Variables :-

'''

● When we declare a variable inside a function it become a local variable
● A Local variable is a variable whose scope is only limited to that function Where it is
created.
● In the Following example the variable a is declared inside myfunction() and hence it
is available inside that function
● Once we come out of function the variable a is removed from memory.

'''

# Example :-
def myfunction():
    a=1 # this is local variable
    a=a+1
    print(a)


myfunction()
# print(a)  # Output :- NameError: name 'a' is not defined



# Global variables :-
'''
These are those which are defined outside any function and which are accessible throughout the program, i.e., inside and outside of every function.

'''

# Example :-
a=1 #this is global variable
def myfunction():
       b=2
       print('a=', a) # display global variable
       print('b=',b) #  display local variable

myfunction()
# print(a)
# print(b)  # Output :- NameError : name 'b' is not defined 



# Global keyword :- 

'''

● Sometimes the global and local variable may have same name in that case the
function by default refers to the local variable and ignores the global variable.
● When the programmer wants to use the global variable inside a function he can use
the keyword global before the variable in the beginning of the function.

'''

# Example :- 
a=1 #this is global variable
def myfunction():
     global a
     a=2
     print('Inside myfunction a = ', a) # display global variable

myfunction()
print('Outside myfunction  a = ', a)   # Output :- a = 2



# Lambda/Anonymous function :- 

'''

● A function without a name is called 'anonymous function'.

● So far, the functions we wrote were defined using the keyword 'def'. But anonymous
functions are not defined using 'def'. They are defined using the keyword lambda and
hence they are also called 'Lambda functions'.

● These functions are called anonymous because they are not declared in the standard
manner by using the def keyword. You can use the lambda keyword to create small
anonymous functions.

● Lambda forms can take any number of arguments but return just one value in the form of
an expression. They cannot contain commands or multiple expressions.

● An anonymous function cannot be a direct call to print because lambda requires an
expression.

● Lambda functions have their own local namespace and cannot access variables other than
those in their parameter list and those in the global namespace.

● We use the lambda keyword instead of def to create a lambda function. 

     Syntax :-   lambda argument(s) : expression


Here,
      ○ argument(s) - any value passed to the lambda function
      ○ expression  - expression is executed and returned


'''

# Example :- 
# lambda that accepts one argument 
greet_user = lambda name : print("Hey there " , name)

# lambda call
greet_user("Madhav P")




# Recursion :- 

'''

   ● Function can call other functions. It is even possible for the function to call itself.These types of construct are termed as recursive functions.

   ● A function that calls itself is known as recursive function.

   ● Every recursive function must have a base condition that stops the recursion or
   else the function calls itself infinitely.

   ● The Python interpreter limits the depths of recursion to help avoid infinite
   recursions, resulting in stack overflows.

   ● By default, the maximum depth of recursion is 1000. If the limit is crossed, it
   results in RecursionError.

   
'''
# Syntax :- 
def recurse():
    ...
    recurse()
    ...

recurse() 




# Factorial of a Given Number :- 
def fact(n):
     if n==0:return 1
     if n==1:return 1
     else:
         return n * fact(n-1)


def factorial():
    print("Enter any number :- ")
    n = int(input())
    print(f" Factorial of {n} is :- ",fact(n))


factorial()




# Sum of N Natural numbers 
def Add(limit):
    sum = 0
    return sum + sum + (limit-1)



def SUM():
    print("Enter the limit :- ")
    limit = int(input())
    print(f" Sum  of {limit} Natural numbers is :- ",Add(limit))
 

SUM()
