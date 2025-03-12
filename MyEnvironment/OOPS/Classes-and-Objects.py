'''

💡) Class :- A class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.


📃Syntax :- 

class ClassName:
    def __init__(self, parameters):
        # Initialize attributes
    def method(self):
        # Define method


Usage :-  Classes are used to model real-world entities and define their behavior.

How it works :-  When a class is defined, no memory is allocated until objects of the class are created.



💡) Object :- An object is an instance of a class. It contains data and methods defined in the class. 

Syntax :-  obj = ClassName(parameters)

Usage :-  Objects are used to interact with the class methods and attributes.

How it works :-  When an object is created, memory is allocated and the __init__ method is called to initialize the attributes.


'''



# Create a Class :- To create a class, use the keyword class :

# Example :- Create a class named MyClass, with a property named x :
class MyClass:
       x = 5



# Create Object :- Now we can use the class named MyClass to create objects :-

# Example :- Create an object named p1, and print the value of x :
p1 = MyClass()  
print(p1.x)      # Output :- 5




# Ellipse Object (...) :- 

'''

Ellipsis, represented by ... in Python, is a built-in object that is technically an instance of the EllipsisType. While it might seem obscure at first, it is a versatile tool used in various contexts, especially in type hinting, slicing, and placeholder scenarios.

'''


# Definition :- Ellipsis (...) is a singleton object in Python, which means there is only one instance of it throughout a program. It is represented by three consecutive dots (...), and it has the type <class 'ellipsis'>.


# Key Features :- 

'''

   >> It's a constant and immutable.
   >> Only one instance exists, so Ellipsis is ... is always True.

'''

#  Syntax :-  
...

if ... == Ellipsis:
    print("True")   # Output :- True 


# Working and Behavior :- 
print(...)    # Output :- Ellipsis



# Advantages of Ellipsis :- 

'''

   1) Readability :-  Makes code cleaner and easier to understand when used as a placeholder.

   2) Flexibility :-  Allows for abstracting away details, especially in slicing or type annotations.

   3) Prototyping :-  Helps during development for incomplete code.

'''


# Limitations :- 

'''

   1) It is not inherently functional—it does nothing by itself.

   2) Its use can confuse readers if overused or used in non-standard ways.

'''


'''

Key Details :- 

a) Symbol :-   `...`

b) Built-In Name :-  `Ellipsis`

c) Type :-  <class 'ellipsis'>

d) Singleton :-  Yes (only a single instance exists)

e) Availability :-  Always available in Python (introduced in early versions)

f) Use Cases :-  Commonly used in type hinting, slicing, as a placeholder, and as a marker in functions or loops.

g) Libraries :-  Frequently utilized in libraries such as NumPy, Pandas, and type hints for various operations.

This versatile symbol plays a crucial role in Python programming, particularly in advanced indexing,  abstract implementations, and annotations.

'''





# Class and Object Example :- 
class Employee:
       language = "Python"      # Class Attribute 
       salary = "1200000"       # Class Attribute 

Madhav = Employee()
Madhav.name = "Madhav"          # This is an instance  attribute 

print(Madhav.name,Madhav.language , Madhav.salary )         # Output :- Madhav Python 1200000


Harry = Employee()
Harry.name = "Harry bhai "      # This is an instance attribute 

print(Harry.name , Harry.salary , Harry.language)           # Output :- Harry bhai  1200000 Python

["Note :-  Here name is Object(instance) attribute and salary and language are class Attributes as they belong to the class . "]




# Instance Vs Class Attribute 
class Employee:
       language = "Py"           # This is a class Attribute 
       salary = 1200000

harry = Employee()
harry.language = "Javascript"          # This is an instance attribute

print(harry.language , harry.salary)         # Output :- Javascript 1200000





# Object Methods :- Objects can also contain methods. Methods in objects are functions that belong to the object. Let us create a method in the Person class :-

# Example 1 :- Insert a function that prints a greeting, and execute it on the p1 object :-

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def  myfunc(self):
       print("Hello my name is :- " + self.name)
       print("Age is :- ",self.age)
       print()


p1 = Person("John" , 36)
p1.age = 40
p1.myfunc()


'''

Output :- 

Hello my name is :- John
Age is :-  40

'''




# Modify Object Properties :-  You can modify properties on objects like this  :-

# Example :- Set the age of p1 to 40:
p1.age = 40
p1.myfunc()


# Delete Object Properties :- You can delete properties on objects by using the del keyword :-

# Example :-  Delete the age property from the p1 object :- 
del p1.age
p1.myfunc()               # Output :- AttributeError: 'Person' object has no attribute 'age'


# Delete Objects :- You can delete objects by using the del keyword :-

# Example :-  Delete the p1 object :-
del p1
p1.myfunc()               # Output :- NameError: name 'p1' is not defined





# ⭐) The self Parameter :- 

'''

●) The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

●) It does not have to be named self , you can call it whatever you like, but it has to be the
first parameter of any function in the class :-

'''

# Example :- 

class Employee:
       language = "Python"   # This is a classs Attribute 
       salary = 1200000

       def getInfo(self):   # Method 
              print(f"The language is {self.language} . The salary is {self.salary}") 

       def greet(self):
              print("Good Morning")


harry = Employee()
harry.language = "JavaScript"       # This is an instance attribute 

# Two ways :-  1) harry.getInfo()  and  2) Employee.getInfo(harry)


'''

when this happens :- 

      def getInfo():   # Method 
                 print(f"The language is {self.language} . The salary is {self.salary}") 

                 
harry.getInfo() will throw error . 

'''

harry.getInfo()      # Output :- TypeError:  Employee.getInfo() takes 0 positional arguments but 1 was given . As it contains Employee.getInfo(harry) so  it was passing in Employee class which were not accepting this harry object there in the Method getInfo() 

'''

💡) Understanding the Error in harry.getInfo()

>>> In Python, when calling an instance method using object.method(), Python implicitly passes the instance (self) as the first argument to the method.


harry.getInfo()  

Initially, this call resulted in the following error :-   TypeError: Employee.getInfo() takes 0 positional arguments but 1 was given


⭐) This happened because Python implicitly passes self (which is harry here) to getInfo(), but if the method is not defined with self as a parameter, it does not accept any arguments.

'''


Employee.getInfo(harry)   # Output :- The language is JavaScript . The salary is 1200000

Employee.greet(harry)     # Output :- Good Morning

harry.getInfo()           # Output :- The language is JavaScript . The salary is 1200000

harry.greet()             # Output :- Good Morning





# String Representation :- 

'''

1) __str__(self): Informal string representation (str(self))

2) __repr__(self): Formal string representation (repr(self))


'''




# Object Creation and Deletion :- 

'''

1)  __new__(cls, *args, **kwargs) :-  Creation of a new instance

2)  __init__(self, *args, **kwargs) :-  Initialization of an instance

3)  __del__(self) :-  Destructor (called when an object is about to be destroyed)


'''





# Custom Context Manager :- 

'''

1) __enter__(self) :-  Enter the runtime context

2) __exit__(self, exc_type, exc_value, traceback) :- Exit the runtime context


'''

# Example: Custom Context Manager :-  

'''

Here's an example of using __enter__ and __exit__ to create a custom context manager :-

'''
class MyResource:
    def __enter__(self):
        print("Resource acquired")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Resource released")

# Usage
with MyResource() as resource:
    print("Using resource")
print()