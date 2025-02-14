# TYPES  DEFINITIONS  IN  PYTHON  :-

''' 

  Type hints in Python allow you to annotate variables, function arguments, and return values with expected data types. They help developers understand the type of data expected by a function or variable, making code easier to read, debug, and maintain.

  Type hints are not enforced at runtime (Python is still dynamically typed) but are used for static analysis by tools like mypy or IDE linters to detect type-related issues.
 
'''

# When Were Type Hints Introduced ? 


'''

Introduced : -  In Python 3.5 (2015) via PEP 484.
Why Introduced :- 

  ● Improve code readability.
  ● Make it easier to debug and test code by specifying the expected types.
  ● Support for type checking tools like mypy.
  ● Encourage better coding practices in large and complex codebases.
  
'''


'''

 >> Why Use Type Hints?

     1) Improved Code Readability :-  Type hints make it clear what types are expected.

     2) Static Analysis :- Tools like mypy can catch type-related errors without running the code.

     3) Documentation :-  Type hints serve as built-in documentation for developers.

     4) Better IDE Support :-  Modern IDEs (e.g., PyCharm, VSCode) provide better autocompletion and linting for type-annotated code.

'''

# Syntax of Type Hints :- 

'''

 Type hints use the colon (:) syntax for annotating variable types and function parameters. The arrow (->) is used to annotate return types.
 
'''

# Basic Syntax :- For Varibles :- 
x : int = 10       # x is an integer 
y : str = "hello"  # y is a  string  
print(x,y)   # Output :- 10 hello


# For Functions :- 
def add(x: int , y: int) -> int:
        return x+y

print(add(5 , 10))   # Output :- 15


# For Classes :- 
class Point:
        x : float
        y : float


p = Point()
p.x= 15   # If printed output comes 15 even if float specified 
print(p.x)   # Output :- 1.5



# Why Doesn’t Python Enforce Type Hints ? 

'''

Python is a dynamically typed language, which means :0 

   ●) Variables can hold values of any type, and their types can change during execution.

   ●) Type hints are not constraints; they are annotations for tools and developers.

If Python were to enforce type hints at runtime, it would no longer be dynamically typed and would introduce additional overhead during execution.

'''

#  How Type Hints Work

'''

Runtime Behavior

    1) Type hints are ignored by Python at runtime. Python treats them as annotations and stores them in the __annotations__ attribute.

    2) They are primarily used by static type checkers, IDEs, and documentation generators.

'''

# Example :- 
x : int = 42
print(x.__annotations__)


# Why x.__annotations__ Doesn't Work : -

'''

>> When you define x : int = 42 at the module level, Python treats x as a regular variable. It does not attach the type hint (int) to the variable itself. Instead:

    ●) The type hint is stored in the __annotations__ attribute of the module.

You cannot access it directly from the variable x because Python does not associate runtime metadata with individual variables.

'''


# However, we can manually inspect the type hints :- 
def greet(name : str)  -> str:
        return f"hello , {name}!"

print(greet.__annotations__)    # {'name': <class 'str'>, 'return': <class 'str'>}




# Advanced Typing modules :- The typing module in Python provides many built-in types for more complex scenarios 

'''

Basic Types :- 

  a) List[int] :- A list of integers.
  b) Tuple[str, int] :- A tuple with a string and an integer. 
  c) Dict[str, int] :- A dictionary with string keys and integer values.
  d) Set[float] :-   A set of floats.


Optional Types :- 

   e) Optional[int] :-  An integer or None.
   
'''

# Example 

from typing import List,Tuple,Dict,Set,Union

# List of intergers :- 
List_numbers : List[int] = [1 ,2 , 3, 4 ,5]
print(List_numbers)   # Output :- [1 ,2 , 3, 4 ,5]


# # Tuple of Items :- 
Tuple_items : Tuple[str , float] = "hello ji " , 4.5
print(Tuple_items)   # Output :- ('hello ji ', 4.5)




# Dictionary  of key - value pairs :- 

'''

>> Dict type from the typing module only accepts two generic type arguments :-

   1) The type of the keys.
   2) The type of the values.

'''
# ' any '  allows any type for the values .

couples_data : Dict[str , any] = {"Raj" : "Simran" , "Prem" : "Paro" }
print(couples_data)   # Output :-  {'Raj': 'Simran', 'Prem': 'Paro'}



# # Set data of Student :- 
Set_data :  Set[str] = {"Madhav" , 19}
print(Set_data)     # Output :-   {'Madhav', 19}


# # Union Data :-  Union type of variables that can hold multiple types 
identifier : Union[int , str] = "ID292383895485"
print(identifier)   # Output :- ID292383895485