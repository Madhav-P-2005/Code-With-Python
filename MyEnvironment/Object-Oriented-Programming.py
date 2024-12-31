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



# The self Parameter :- 

'''

●) The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

●) It does not have to be named self , you can call it whatever you like, but it has to be the
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
# harry.language = "JavaScript"   # This is an instance attribute 

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

       @staticmethod
       def greet(self):
              print("Good Morning")
