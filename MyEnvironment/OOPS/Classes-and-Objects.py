'''

💡) Class :- A class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.


Syntax :- 

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
# p1.myfunc()   # Output :- AttributeError: 'Person' object has no attribute 'age'


# Delete Objects :- You can delete objects by using the del keyword :-

# Example :-  Delete the p1 object :-
del p1
# p1.myfunc()   # Output :- NameError: name 'p1' is not defined



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
       def __init__(self , name , language , salary):   # dunder method(constructor) which is automatically called 
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
print('\n')


# Class Method() :- 

'''

 A class method is a method that is bound to the class and not the instance of the class. It can modify class state that applies across all instances of the class. Class methods take a cls parameter that points to the class—and not the instance—when the method is called.

 '''

# Syntax :- 
class MyClass:
    class_attribute = "I am a class attribute"

    @classmethod
    def class_method(cls):
        print(f"Class method called: {cls.class_attribute}")

# Usage
MyClass.class_method()


# How it Works:

'''

1) Decorator :-  The @classmethod decorator is used to define a method as a class method.

2) Parameter cls :- The first parameter cls points to the class, not the object instance.

3) Accessing Class Attributes :- Inside the class method, you can access or modify class attributes using cls.

'''

# Usage :- 

'''

1) Factory Methods :-  Class methods are often used to create factory methods, which can create an instance of the class using alternative constructors.

2) Access/Modify Class State :-  They can be used to access or modify the class state that applies to all instances.

'''

# Example :- 

class Employee:
      a = 1   # Class Attribute 
      def show(self):
            print(f"The class value of a is {self.a}")
    
E = Employee()
E.a = 45  # output :- prints instance(object) value  =  45 

E.show()   # Output :- The class value of a is 45


# To overcome this we use @classmethod 
class Employee:
      a = 1   # Class Attribute 

      @classmethod
      def show(self):   # self or cls or something ...  anything will work.
            print(f"The class value of a is {self.a}")
    
E = Employee()
E.a = 45  # output :- Takes  class Attribute value  = 1 Because of @classmethod 

E.show()   # Output :- The class value of a is 1



# Property Decorators :-

''' 

Property decorators in Python are used to define methods in a class that can be accessed like attributes. They allow you to define getter, setter, and deleter methods, providing a way to manage the internal state of a class in an organized manner.

'''

# How it Works :-
 
'''

Property decorators work by transforming methods into read-only or read-write properties of the class. When you use the @property decorator, it turns the method into a getter for a managed attribute. If you also provide methods decorated with @<property_name>.setter and @<property_name>.deleter, you can control setting and deleting the attribute.

'''

# Usage :- 

'''

1) Getter :-  Define a method that retrieves the value of an attribute and decorate it with @property.

2) Setter :-  Define a method that sets the value of an attribute and decorate it with @<property_name>.setter.

3) Deleter :- Define a method that deletes an attribute and decorate it with @<property_name>.deleter.

'''

# Example :- 
class Employee:
      
      a = 1   # Class Attribute 

      @classmethod
      def show(self):   # self or cls or something ...  anything will work.
            print(f"The class value of a is {self.a}")
       

      @property
      def name(self):
            return f"{self.fname} {self.lname}"
      
      # This is only called Abstraction and Encapsulation. Abstraction:- Here the implementation details are made hidden from the users and Encapsulation :- we have made all the working components into a particular unit and is packed . which in case here is class . 
      @name.setter
      def name(self , value):
            self.fname = value.split(" ")[0]
            self.lname = value.split(" ")[1]

E = Employee()
E.a = 45  # output :- Takes  class Attribute value  = 1 Because of @classmethod 

E.name = "Harry Bhai ❤️"
print(E.fname , E.lname)
E.show()   # Output :- The class value of a is 1



# Without Property Decorators :- 
class Rectangle:
    def __init__(self, width, height):
        self._width = width   # Attribute
        self._height = height  # Attribute

    def get_width(self):  # Method (Getter)
        return self._width

    def set_width(self, value):  # Method (Setter)
        if value > 0:
            self._width = value
        else:
            raise ValueError("Width must be a positive value.")

    def get_height(self):  # Method (Getter)
        return self._height

    def set_height(self, value):  # Method (Setter)
        if value > 0:
            self._height = value
        else:
            raise ValueError("Height must be a positive value.")

    def area(self):  # Method
        return self._width * self._height

# Usage
rect = Rectangle(5, 10)
print(rect.get_width())  # Output: 5
print(rect.get_height())  # Output: 10
print(rect.area())  # Output: 50

rect.set_width(20)
print(rect.area())  # Output: 200




# Using Property Decorators :-
class Rectangle:
    def __init__(self, width, height):
        self._width = width  # Attribute
        self._height = height  # Attribute

    @property
    def width(self):  # Property (Getter)
        return self._width

    @width.setter
    def width(self, value):  # Property (Setter)
        if value > 0:
            self._width = value
        else:
            raise ValueError("Width must be a positive value.")

    @property
    def height(self):  # Property (Getter)
        return self._height

    @height.setter
    def height(self, value):  # Property (Setter)
        if value > 0:
            self._height = value
        else:
            raise ValueError("Height must be a positive value.")

    @property
    def area(self):  # Property (Computed attribute)
        return self._width * self._height

# Usage
rect = Rectangle(5, 10)
print(rect.width)  # Output: 5
print(rect.height)  # Output: 10
print(rect.area)  # Output: 50
rect.width = 20
print(rect.area)  # Output: 200




# Key Differences :- 

'''

1) Access Syntax :- a) Methods: You need to use method calls like get_width() and set_width(value). 
                    b) Properties: You access them like attributes, e.g., rect.width and rect.width = value.

2) Readability and Clean Code :-   a) Methods: The code can become cluttered with method calls.
                                   b) Properties: The code looks cleaner and more natural, like regular attribute access.

3) Encapsulation :-    a) Methods: The logic to get and set values is separated into methods.
                       b) Properties: The logic to get, set, and compute values is encapsulated within properties, promoting better abstraction.

4) Consistency :-      a) Methods: Every access and modification must go through the method, ensuring validation but can be cumbersome.
                       b) Properties: Automatic validation when setting values, ensuring consistency and ease of use.

5) Advanced Features :-  Properties can have computed values (like area) and can include deleters, providing more flexibility without changing the interface.

'''



# Operator Overloading :- 

'''

Operator overloading in Python allows you to define custom behavior for built-in operators (like +, -, *, etc.) when they are used with objects of a user-defined class. This makes it possible to use operators with your class objects just like you would with built-in types.

'''

# Syntax :- 

'''
To overload an operator, you define a special method in your class. These special methods are also called magic methods or dunder methods (double underscore methods), because they have double underscores at the beginning and end of their names.

'''

# Working :- 

'''

1) Define a class with special methods that correspond to the operators you want to overload.

2) Create objects of this class.

3) Use the overloaded operators with these objects.

'''


# Example :- 
class Number:
     def __init__(self , n ):
          self.n = n

     # Overload the + operator
     def __add__(self , num):
          return self.n + num.n   # Return a new Number instance

n = Number(1)
m = Number(2)



print(n + m)   # Output :- unsupported operand type(s) for +: 'Number' and 'Number'
result = n + m 
print(result.n) # Output: 3

# Explanation :- 

'''

1) Class Definition :-  The __init__ method initializes the n attribute.

2) Overloaded __add__ Method :- a) This method takes another Number instance (num) as an argument.
                                b) It returns a new Number instance with the sum of self.n and num.n.

3) Creating Instances :-   n = Number(1) and m = Number(2) create two instances of Number.

4) Using the + Operator :-  n + m uses the overloaded __add__ method.
                           a) This adds the n values of both instances (1 + 2 = 3).
                           b) A new Number instance is returned with this sum.

5) Accessing the Result :-  result.n accesses the n attribute of the result, which is 3.


'''


# Arithmetic Operators :- 

'''

1) __add__(self, other): Addition (+)

2) __sub__(self, other): Subtraction (-)

3) __mul__(self, other): Multiplication (*)

4) __truediv__(self, other): True Division (/)

5) __mod__(self, other): Modulus (%)

6) __pow__(self, other): Exponentiation (**)

'''

# Unary Operators :- 

'''

1)  __neg__(self): Negation (-self)

2)  __pos__(self): Unary plus (+self)

3)  __abs__(self): Absolute value (abs(self))

'''

# Comparison Operators :- 

'''

1) __eq__(self, other): Equality (==)

2) __ne__(self, other): Inequality (!=)

3) __lt__(self, other): Less than (<)

4) __le__(self, other): Less than or equal to (<=)

5) __gt__(self, other): Greater than (>)

6) __ge__(self, other): Greater than or equal to (>=)


'''

# Bitwise Operators  :- 

'''

1)  __and__(self, other) :-  Bitwise AND (&)

2)  __or__(self, other) :-  Bitwise OR (|)

3)  __xor__(self, other) :- Bitwise XOR (^)

4)  __invert__(self) :- Bitwise NOT (~)

5)  __lshift__(self, other) :-  Left shift (<<)

6)  __rshift__(self, other) :-  Right shift (>>)


'''



# Assignment Operators :- 

'''

1) __iadd__(self, other) :- In-place addition (+=)

2) __isub__(self, other) :- In-place subtraction (-=)

3) __imul__(self, other) :-  In-place multiplication (*=)

4) __itruediv__(self, other) :-  In-place true division (/=)

5) __ifloordiv__(self, other) :-  In-place floor division (//=)

6) __imod__(self, other) :-  In-place modulus (%=)

7) __ipow__(self, other) :-  In-place exponentiation (**=)


'''



# Container Emulation :- 

'''

1) __len__(self): Length (len(self))

2) __getitem__(self, key): Getting item (self[key])

3) __setitem__(self, key, value): Setting item (self[key] = value)

4) __delitem__(self, key): Deleting item (del self[key])

5) __contains__(self, item): Membership test (item in self)


'''



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