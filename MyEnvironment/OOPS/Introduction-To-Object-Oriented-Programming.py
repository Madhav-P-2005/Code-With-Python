# DRY Principle :- Do not Repeat Yourself . 

# Problems in Procedure Oriented Approach :-

'''

1) Procedural programming mainly focuses on procedures or functions. Less attention is
given to the data.

2) The data and functions are separate from each other.

3) Global data is freely moving and is shared among various functions. Thus, it becomes
difficult for programmers to identify and fix issues in a program that originate due to
incorrect data handling.

4) Changes in data types need to be carried out manually all over the program and in the
functions using the same data type.

5) Limited and difficult code reusability.

6) It does not model real-world entities (e.g., car, table, bank account, loan) very well where
we as a human being, perceive everything as an object.

7) The procedural programming approach does not work well for large and complex
systems.


'''

# Python Classes and Objects :-

"""

1) Python is an object-oriented programming language.

2) Almost everything in Python is an object, with its properties and methods.

3) A Class is like an object constructor, or a "blueprint" for creating objects.

"""

# Features Of Object-Oriented Programming (OOP) ?

'''

1) Class :- A class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.

Syntax :- 
class ClassName:
    def __init__(self, parameters):
        # Initialize attributes
    def method(self):
        # Define method


Usage :-  Classes are used to model real-world entities and define their behavior.

How it works :-  When a class is defined, no memory is allocated until objects of the class are created.



2) Object :- An object is an instance of a class. It contains data and methods defined in the class. 

Syntax :-  obj = ClassName(parameters)

Usage :-  Objects are used to interact with the class methods and attributes.

How it works :-  When an object is created, memory is allocated and the __init__ method is called to initialize the attributes.



3) Encapsulation :-  Encapsulation is the bundling of data (attributes) and methods that operate on the data into a single unit (class), and restricting access to some of the object's components.


Syntax :- 

class MyClass:
    def __init__(self, value):
        self.__private_attribute = value


Usage :-  Encapsulation is used to protect the internal state of an object and only expose the necessary parts.


How it works :-  By defining private attributes (prefixed with __), access to these attributes is restricted outside the class.



4) Abstraction :-  Abstraction is the concept of hiding the complex implementation details and showing only the necessary features.


Syntax :- 

from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

        
Usage :-  Abstraction is used to focus on essential qualities rather than specific characteristics.


How it works :-  Abstract classes and methods provide a way to define common interfaces for different implementations.



5) Polymorphism :- Polymorphism allows methods to do different things based on the object it is acting upon.


Syntax :- 

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

        
Usage :-  Polymorphism is used to allow different classes to be treated as instances of the same class through a common interface.


How it works :-  Methods in different classes can have the same name and provide different functionalities.



6) Inheritance :- Inheritance allows a class (child class) to inherit properties and behavior from another class (parent class).

Syntax :- 

class ParentClass:
    def method(self):
        pass

class ChildClass(ParentClass):
    def another_method(self):
        pass


Usage :-  Inheritance is used to create a hierarchical classification and promote code reuse.


How it works :-  The child class inherits methods and attributes from the parent class and can also have additional methods and attributes.



7) Dynamic Binding :-  Dynamic binding refers to the process of linking a method call to the method body at runtime.

Syntax :- 

class Base:
    def method(self):
        pass

class Derived(Base):
    def method(self):
        pass

obj = Derived()
obj.method()  # Calls the method in Derived class


Usage :-  Dynamic binding is used to achieve polymorphism and allow method overriding.


How it works :- The method to be called is determined at runtime based on the object type.



8. Message Passing :- Message passing is the process by which an object sends data to another object or asks for data from another object.


Syntax :- obj.method(parameters)


Usage :-  Message passing is used to enable objects to interact with each other.


How it works :-  Objects communicate with each other by calling methods and passing data as parameters.

'''


# Create a Class :- To create a class, use the keyword class :

# Example :- Create a class named MyClass, with a property named x :
class MyClass:
       x = 5



# Create Object :- Now we can use the class named MyClass to create objects :-

# Example :- Create an object named p1, and print the value of x :
p1 = MyClass()  
print(p1.x)


# Class and Object Example :- 
class Employee:
       language = "Python"  # Class Attribute 
       salary = "1200000"   # Class Attribute 

Madhav = Employee()
Madhav.name = "Madhav"  # This is an instance  attribute 
print(Madhav.name,Madhav.language , Madhav.salary )   # Output :- Madhav Python 1200000

Harry = Employee()
Harry.name = "Harry bhai "   # This is an instance attribute 
print(Harry.name , Harry.salary , Harry.language)   # Output :- Harry bhai  1200000 Python

# Here name is Object(instance) attribute and salary and language are class Attributes as they belong to the class . 


# Instance Vs Class Attribute 
class Employee:
       language = "Py"  # This is a class Attribute 
       salary = 1200000

harry = Employee()
harry.language = "Javascript"   # This is an instance attribute
print(harry.language , harry.salary) # Output :- Javascript 1200000



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
# p1.age = 40
p1.myfunc()



# Modify Object Properties :-  You can modify properties on objects like this  :-

# Example :- Set the age of p1 to 40:
p1.age = 40
p1.myfunc()


# Delete Object Properties :- You can delete properties on objects by using the del keyword :-

# Example :-  Delete the age property from the p1 object :- 
del p1.age
p1.myfunc()   # Output :- AttributeError: 'Person' object has no attribute 'age'


# Delete Objects :- You can delete objects by using the del keyword :-

# Example :-  Delete the p1 object :-
del p1
p1.myfunc()   # Output :- NameError: name 'p1' is not defined



# The self Parameter :- 

'''

●) The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

●) It does not have to be named self , you can call it whatever you like, but it has to be the
first parameter of any function in the class :-

'''

# Example 
class Employee:
       language = "Python"   # This is a classs Attribute 
       salary = 1200000

       def getInfo(self):   # Method 
              print(f"The language is {self.language} . The salary is {self.salary}") 

       def greet(self):
              print("Good Morning")


harry = Employee()
harry.language = "JavaScript"   # This is an instance attribute 

# Two ways :-  1) harry.getInfo()  and  2) Employee.getInfo(harry)

harry.getInfo()  # Output :- TypeError: Employee.getInfo() takes 0 positional arguments but 1 was given . As it contains Employee.getInfo(harry) so  it was passing in Employee class which were not accepting this harry object there in the Method getInfo() 

Employee.getInfo(harry)   # Output :- The language is JavaScript . The salary is 1200000
Employee.greet(harry)   # Output :- Good Morning
harry.getInfo()  # Output :- The language is JavaScript . The salary is 1200000
harry.greet()    # Output :- Good Morning



# Static Method :- 
class Employee:
       language = "Python"   # This is a classs Attribute 
       salary = 1200000

       def getInfo(self):   # Method 
              print(f"The language is {self.language} . The salary is {self.salary}") 

# @staticmethod :- It is a decorator used why you dont want to pass (self) as  an object to a method . 

       @staticmethod     # If you dont need to put Object here then use @staticmethod
       def greet():
              print("Good Morning")


harry = Employee()
harry.greet()
harry.getInfo()



# The __init__() Function :- The __init__() function in Python is a special method, often referred to as a "constructor" in object-oriented programming. It's a type of dunder (double underscore) method that gets called automatically when an instance (object) of a class is created.

'''

●  The examples above are classes and objects in their simplest form, and are not really
useful in real life applications.

● It is a special method which is called dunder method . In python the methods which starts with and underscore __ is called as dunder method .

●  To understand the meaning of classes we have to understand the built-in __init__() function.

●  All classes have a function called __init__(), which is always executed when the class is being initiated.

●  Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created.


# Key Points About __init__() :- 

1) Constructor Method :-  While it's technically a method, its primary purpose is to initialize an object's attributes, making it similar to what other programming languages call a constructor.

2) Automatic Execution :-  When you create an instance of a class, Python calls the __init__() method automatically to set up the object.

3) Initialization of Attributes :-  It is used to assign values to object properties or perform other initialization tasks that are necessary when the object is being created.


'''


class Employee:
       language = "Python"   # This is a classs Attribute 
       salary = 1200000

       # Instead of giving  harry.name = "Harry" use __init__ Function :-
       def __init__(self , name , language , salary):   # dunder method which is automatically called 
              self.name = name
              self.language = language
              self.salary = salary
              print("I am creating an Object")


       def getInfo(self):   # Method 
              print(f"The language is {self.language} . The salary is {self.salary}") 



       @staticmethod     
       def greet():
              print("Good Morning")


# harry = Employee() # # Output :- I am creating an Object
harry = Employee("Harry" , 1300000 , "JavaScript")
harry.name = "Harry"
print(harry.name , harry.language ,harry.salary)  # Output :- Harry Python 1200000
# rohan = Employee() # Output :- I am creating an Object