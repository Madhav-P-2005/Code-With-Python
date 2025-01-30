# Exception Handling 


# When Released ? 
'''
  >> Exception handling was introduced in Python 2.0 (released in October 2000). However, the features were refined in Python 3.x versions.

'''

# Evolution of Exception Handling in Python :- 

'''

   a) Python 2.x :-  Introduced basic exception handling with the try and except blocks.
   
'''

# Example :- 
'''

try:
    # Code that might throw an exception
except SomeException:
    # Handle the exception

'''




'''

    b) Python 3.x: The exception handling was further refined, and else and finally blocks were added. Additionally, the as keyword was introduced for better exception management.
    
'''

# Example (in Python 3) :- 
'''

try:
    # Code that might throw an exception
except SomeException as e:
    # Handle the exception with 'e' containing the exception details
else:
    # Code that runs if no exception occurred
finally:
    # Code that always runs

'''



# Definition :- 

'''

    >> Exception handling in Python is a mechanism that allows you to deal with runtime errors (or exceptions) in a controlled way, preventing the program from crashing unexpectedly. Instead of allowing the program to terminate when an error occurs, exceptions allow the programmer to handle the error and continue with the program execution.


>> Some Important points to remember :- 
 	
	1)  If the programmer cannot do anything in case of an error, then it is called an 'error' and not an exception.

	2) All exceptions are represented as classes in Python.

	3) The exceptions which are already available in Python are called 'built-in' exceptions.

	4) The base class for all built-in exceptions is 'BaseException' class.

	5) From BaseException class, the sub class ' Exception' is derived. From Exception class, the sub classes 'StandardError'  and 'Warning' are derived.

	6) All errors (or exceptions) are defined as sub classes of 'StandardError' .

	7) An error should be compulsorily handled otherwise the program will not execute.

	8) Similarly, all warnings are derived as sub classes from 'Warning' class. A warning represents a caution and even though it is not handled, the program will execute. So, warnings can be neglected but errors cannot be neglected.

'''


# When to use Exception Handling ? 

'''

    1) Graceful Error Handling :-  You can manage errors without stopping the program unexpectedly.

    2) Code Flow Control :-  Handle various types of errors based on specific exceptions.

    3) Cleaner Code :-  Instead of using multiple checks for errors, exceptions allow you to focus on the primary logic and handle errors separately.

    4) Separation of Concerns :-  Keeping error-handling code distinct from normal program logic.

'''




# Types of Errors :- 


'''

• Errors in a Python Program In general, we can classify errors in a program into one of
these three types:

       • Compile-time errors
       • Runtime errors
       • Logical errors


'''
# Compile-Time Errors :- 
'''

    • These are syntactical errors found in the code, due to which a program fails to compile.

    • For example, forgetting a colon in the statements like if, while, for, def, etc. will result in compile-time error.

    • Such errors are detected by Python compiler and the line number along with error
    description is displayed by the Python compiler.
     
'''


# Runtime Errors :- 
'''

    • When Python Virtual Machine cannot execute the byte code, it flags runtime error.

    • For example, insufficient memory to store something or inability of the PVM to execute some statement come under runtime errors.

    • Runtime errors are not detected by the Python compiler. They are detected by the PVM, only at runtime.
    
'''



# Logical Errors :- 
'''

    • These errors depict flaws in the logic of the program.

    • The programmer might be using a wrong formula or the design of the program itself is wrong.

    • Logical errors are not detected either by Python compiler or PVM. The programme is
    solely responsible for them.


'''


# Components of Exception Handling :- 

'''

1)  try block :-  Code that might cause an exception is placed inside the try block.

2) except block :- 

    1) If an exception occurs in the try block, the code in the except block runs.

    2) The exception is specified in the except clause, e.g., except ZeroDivisionError.

3) else block (optional) :-

    1) If no exception occurs in the try block, the else block executes.

    2) This block is optional and used when you want to execute code only when the try block is successful.

4) finally block (optional) ;-

    1) This block will always run, regardless of whether an exception occurred or not.

    2) It is used to perform clean-up actions, such as closing files or releasing resources
      
'''




# Try Block :-

''' 
   >> The try block contains the code that might raise an exception. Python will attempt to execute this code, and if an error occurs, it will look for an except block to handle it.

'''


# Syntax :- 

'''
try: 
    statements

'''



# Except Block :-

''' 

   >> The 'except' block is useful to catch an exception that is raised in the try block. When there is an exception in the try block, then only the except block is executed. It is written in various formats :- 

   1) To catch the exception which is raised in the try block, we can write except block with
   the Exceptionclass name as :- 

   except Exceptionclass:


   2) We can catch the exception as an object that contains some description about the exception.

   except Exception as obj:

   
   3) To catch multiple exceptions, we can write multiple catch blocks. The other way is to use a single except block and write all the exceptions as a tuple inside parentheses as :- 

   except (Exceptionclass1,Exceptionclass2,...): 


   4) To catch any type of exception where we are not bothered about which type of
   exception it is, we can write except block without mentioning any Exceptionclass
   name as :-

   except:


'''


# Syntax :- 

'''
except Exceptionname: 
              statements

'''




# Finally Block :-

''' 

   The finally block is always executed, regardless of whether an exception occurred or not. It is typically used for cleanup operations, like closing files or releasing resources.

   ⭐) Note :- See Finally means it will always be executed . But in functions it works differently , if the function returns then it means that the after code(succeeding code) of this function will not work but here the finally overrides it . 

'''


# Syntax :- 

'''
try: 
    statements

'''


# Example 
def main():
      try:
            a = int(input("Hey , Enter a number : "))
            print(a)
            return
      except Exception as e:
            print(e)
            return 
      
      finally:
            print("You have entered the finally block")

    #   print("Without finally") 

main()


'''
Output :- 

Hey , Enter a number : 556
556
You have entered the finally block

'''
# The following points are noteworthy :- 

'''

A single try block can be followed by several except blocks.

  • Multiple except blocks can be used to handle multiple exceptions. 
  • We cannot write except blocks without a try block.
  • We can write a try block without any except blocks.
  • Else block and finally blocks are not compulsory.
  • When there is no exception, else block is executed after try block.

Finally block is always executed.

'''




# Try with Else Clause :- In Python, you can also use the else clause on the try-except block which must be present after all the except clauses. The code enters the else block only if the try clause does not raise an exception.


# Syntax :- 

'''

try:
    statements
except Exception1:
    handler1
except Exception2:
    handler2
else:
    statements
finally:
    statements

'''

# Example 1 :-   for Divide by zero 
# try:
#     a = int(input("Enter the numerator :- "))
#     b = int(input("Enter the numerator :- "))
#     # b = input("Enter the denominator :- ")
#     divide = a/b
#     print("Divison value is :- ",divide)
    
    
# except ZeroDivisionError as z:
#           print("Error :- ",z)
# except TypeError:
#         print("Typing error occured")
# except RuntimeError:
#         print("Excecution Error ")
# else:
#     print("No error")
# finally:
#     print("Program ended . bye")


'''
Output :- 

Enter the numerator :- 12
Enter the numerator :- 3
Divison value is :-  4.0
No error
Program ended . bye

'''


# Example 2 :- Division by Zero 
# a = int(input("Enter a number :- "))
# b = int(input("Enter a number :- "))

# if(b==0):
#       raise ZeroDivisionError("Hey our program is not meant to divide numbers by zero ")
# else:
#       print(f"The division a/b is {a/b}")




# Python Exception Classes :- There are several exceptions available as part of Python language that are called built-in exceptions. In the same way, the programmer can also create his own exceptions called user-defined exceptions.



'''
                            
Exception Class                |                            Description                                                                                                 |
Name                           |                                                                                                                                        |
                               |                                                                                                                                        |
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Exception                                 Represents any type of exception. All exceptions are sub classes of this class.

ArithmeticError                           Represents the base class for arithmetic errors like OverflowError, ZeroDivisionError, FloatingPointError.

AssertionError                            Raised when an assert statement gives error.

AttributeError                            Raised when an attribute reference or assignment fails.

EOFError                                  Raised when input() function reaches end of file condition without reading any data.

FloatingPointError                        Raised when a floating point operation fails.

IOError                                   Raised when an input or output operation failed. It raises when the file opened is not found or when writing data disk is full.

ImportError                               Raised when an import statement fails to find the module being imported.

IndexError                                Raised when a sequence index or subscript is out of range.

KeyError                                  Raised when a mapping (dictionary) key is not found in the set of existing keys.

KeyboardInterrupt                         Raised when the user hits the interrupt key(normally control-C or Delete).

NameError                                 Raised when an identifier is not found locally or globally.

NotImplementedError                       Derived from 'RuntimeError' . In user defined base classes,abstract methods should raise this exception when they     
                                          require derived classes to override the method.

OverflowError                             Raised when the result of an arithmetic operation is to large too be represented. This cannot occur for long integers (which 
                                          would rather raise'MemoryError').

RuntimeError                              Raised when an error is detected that doesn't fall in any of the other categories.

StopIteration                             Raised by an iterator's next() method to signal that there are no more elements.

SyntaxError                               Raised when the compiler encounters a syntax error.Import or exec statements and input() and eval() functions may raise this 
                                          exception.

IndentationError                          Raised when indentation is not specified properly.

SystemExit                                Raised by the sys.exit() function. When it is not handled, the Python interpreter exits.

ValueError                                Raised when a built-in operation or function receives an argument that has right datatype but wrong value.

ZeroDivisionError                         Raised when the denominator is zero in adivision or modulus operation.

'''




# A Python program to handle IOError produced by open() function ?

# try:
#       name = input("Enter filename : ")
#       f = open(name , 'r')

# except IOError:
#       print("File not Found ",name)

# else:
#       n = len(f.readlines())
#       print(name , 'has', n ,'lines')
#       f.close


'''

Output :- 

Enter filename : Raj.txt
File not Found  Raj.txt

'''



# User Defined Exceptions :-  User-defined exceptions are custom exceptions created by developers to handle specific error scenarios that are not covered by built-in Python exceptions. These exceptions can provide better clarity and control over application logic by signaling issues specific to your code or domain.


# How to Create User-Defined Exceptions :-   You can create a user-defined exception by :-

'''

1) Subclassing the built-in Exception class or its derived classes (e.g., ValueError, RuntimeError).

2)  Optionally defining custom attributes and methods to enhance the exception.

'''




# Syntax :- 
class CustomException(Exception):
    """Custom exception class with a meaningful docstring."""
    pass




# You can then raise this exception using the raise keyword :

# raise CustomException("This is a custom error message.")


# Example 
class CustomError(Exception):
      def __init__(self, message):
            self.message = message

try:
      raise CustomError("This is a Custom Error ")

except CustomError as e:
      print(e.message)



'''

Output :-  This is a Custom Error

'''



# Best Practices for User-Defined Exceptions

'''

1) Inherit from Exception :- 

            a) Always subclass the built-in Exception class to create a custom exception.

2) Use meaningful names :- 

            a) The class name should clearly convey the type of error.

3) Add docstrings :- 

            a) Include a brief description of the exception's purpose.

4) Provide additional attributes (optional) :-

            a) Add context-specific attributes, like error codes or detailed messages.

5) Handle them gracefully :- 

            a) Use try-except blocks to catch and manage custom exceptions.'''




# Advantages of User-Defined Exceptions 

'''

   1) Provides clarity by signaling specific application-level errors.

   2) Makes the code more maintainable and easier to debug.

   3) Enables developers to define custom error handling for their unique use cases.

'''