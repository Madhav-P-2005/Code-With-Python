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

