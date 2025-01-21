'''

💡) Inheritance :- Inheritance allows a class (called a child class or subclass) to inherit attributes and methods from another class (called a parent class or superclass). It promotes code reusability and can lead to a more efficient codebase.


Syntax :- 

class ParentClass:
    def method(self):
        pass

class ChildClass(ParentClass):
    def another_method(self):
        pass


Usage :-  Inheritance is used to create a hierarchical classification and promote code reuse.


How it works :-  The child class inherits methods and attributes from the parent class and can also have additional methods and attributes.


'''


# Example :-

class Employee:
    company = "ITC"
    def show(self ):
        print(f"The name is {self.name} and the salary is {self.salary}")

class Programmer:
    company = "ITC Infotech"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

    def showLanguage(self):
         print(f"The name is {self.name} and he is good with {self.language} language")


# Inheritance Demo :- 

class Programmer(Employee):
    company = "ITC InfoTech"
    def showLanguage(self):
            print(f"The name is {self.name} and he is good with {self.language} language")


a = Employee()
b = Programmer()
print(a.company , b.company)


# Types of Inheritance :- 

# 1) Single Inheritance :-  A child class inherits from one parent class.

class Parent:
     def method1(self):
          print("Parent method")
     
class Child(Parent):
     def method2(self):
          print("Child Method")

obj = Child()
obj.method1() # Output: Parent method
obj.method2() # Output: Child method



# 2) Multiple Inheritance: A child class inherits from more than one parent class.

class Parent1:
     def method1(self):
          print("Parent1 Method")

class Parent2:
     def method2(self):
          print("Parent2 Method")

class Child1(Parent1, Parent2):
     def method3(self):
          print("Child1 Method")


obj = Child1()
obj.method1()  # Output: Parent1 method
obj.method2()  # Output: Parent2 method
obj.method3()  # Output: Child method



# 3) Multilevel Inheritance :-  A child class inherits from a parent class, which in turn inherits from another parent class.


class Grandparent:
    def method1(self):
        print("Grandparent method")

class Parent(Grandparent):
    def method2(self):
        print("Parent method")

class Child(Parent):
    def method3(self):
        print("Child method")

obj = Child()
obj.method1()  # Output: Grandparent method
obj.method2()  # Output: Parent method
obj.method3()  # Output: Child method



# 4) Hierarchical Inheritance :- Multiple child classes inherit from one parent class.

class Parent:
    def method1(self):
        print("Parent method")

class Child1(Parent):
    def method2(self):
        print("Child1 method")

class Child2(Parent):
    def method3(self):
        print("Child2 method")

obj1 = Child1()
obj2 = Child2()
obj1.method1()  # Output: Parent method
obj1.method2()  # Output: Child1 method
obj2.method1()  # Output: Parent method
obj2.method3()  # Output: Child2 method



# 5) Hybrid Inheritance :-   Is a blend of two or more types of inheritance. It usually occurs when a class is derived from multiple classes that follow different inheritance patterns, like combining single, multiple, multilevel, and/or hierarchical inheritance.


class Parent:
    def method1(self):
        print("Parent method")

class Child1(Parent):  # Single Inheritance
    def method2(self):
        print("Child1 method")

class Child2(Parent):  # Hierarchical Inheritance
    def method3(self):
        print("Child2 method")

class Grandchild(Child1, Child2):  # Multiple Inheritance combining Single & Hierarchical Inheritance
    def method4(self):
        print("Grandchild method")

obj = Grandchild()
obj.method1()  # Output: Parent method
obj.method2()  # Output: Child1 method
obj.method3()  # Output: Child2 method
obj.method4()  # Output: Grandchild method
print()



# Super Method() :-

''' 

The super() method in Python is a built-in function used to call methods from a parent class. It's particularly useful in inheritance to ensure that the child class can access and override the parent class's methods. The super() function returns a temporary object of the superclass that allows you to call its methods.

'''


# Syntax :- 

'''

1) Calling Parent Methods :-  Use super().method_name() to call a method from the parent class inside the child class method.

2) Calling Parent Constructor :-  Use super().__init__() in the child class constructor to call the parent class constructor.

'''

# Uses :-

# 1) The super() function is used to call constructors of parent classes as well. When you use super() in the constructor of a child class, it allows you to initialize attributes from the parent class within the child class.

# 2) Access Parent Class Methods: You can use super() to call a method defined in a parent class from a method with the same name in a child class.

# 3) Avoid Duplicate Code: If a method in a child class needs to extend the functionality of a parent class's method, super() can be used to avoid duplicating code.

# 4) Multiple Inheritance :-  In a multiple inheritance scenario, super() ensures that methods are resolved in a consistent manner (using the Method Resolution Order).


class Employee:
    def __init__(self): # Constructor 
       print("Constructor of Employee")

    a = 1  # Class Attribute 

class Programmer(Employee):
    def __init__(self): # Constructor 
       print("Constructor of Programmer")

    b = 2


class Manager(Programmer):
    def __init__(self): # Constructor 
       super().__init__() # Calls the Parent Constructor
       print("Constructor of Manager")
    c = 3

E = Employee()  # Output :-  Constructor of Employee
print(E.a)  # Prints the class a Attribute 


P = Programmer()  # Output :- Constructor of Employee
print(P.a , P.b)  # Prints the class  a & b Attribute 


M = Manager()  # Output :- Constructor of Employee
print(M.a , M.b , M.c)  # Prints the class a , b & c Attribute 

M = Manager()
print(M.a , M.b , M.c)


def factorial(N):
    f=1
    for i in range(1,N+1):
        f=f*i
    return f
    # Your code goes here

N=int(input("enter the value :- "))
c=factorial(N)
print(c)