# ⭐) General Decorators in Python  ?

'''

1️⃣) A decorator is a function that takes another function as an argument and returns a new function that modifies the behavior of the original function. The new function is often referred to as a "decorated" function. 


2️⃣) Decorators in Python are functions that modify the behavior of other functions or methods without changing their code.


3️⃣) They are typically used for logging, authentication, caching, etc.

'''


# 📃) The basic syntax for using a decorator is the following :- 


# @decorator_function
def my_function():
    pass





# 💡) Types of General Decorators ? 


# 1️⃣) Function Decorators  :-    Applied to regular functions to modify their behavior.


# 📃) Syntax :-   @my_decorator



# Example :- 

def greet(fx, gx):             # Decorator function accepting two functions
    def mfx(num1, num2):       # Wrapper function with two arguments
        print("Good Morning")  
        fx()                              # Call first function (hello)
        print(gx(num1, num2))             # Call second function (add) with arguments
        print("Thanks for using this function ")  
    return mfx         # Return the new function (mfx)

# Define functions normally
def hello():
    print("Hello World")

def add(x, y):
    return x + y

# Manually decorate
decorated_function = greet(hello, add)

# Call decorated function
decorated_function(4, 5)


'''

Output :- 

Good Morning
Hello World
9
Thanks for using this function 


'''



# 2️⃣) Function Decorators  :- 




# 3️⃣) Built-in General Decorators :-   Python provides several built-in general decorators


#  a) Static Method (@staticmethod) :- 


# 📃) Syntax :- 

class Example:
    @staticmethod
    def greet():
        return "Hello!"



# Example :- 

class Employee:
       language = "Python"   # This is a class Attribute 
       salary = 1200000

       def getInfo(self):   # Method 
              print(f"The language is {self.language} . The salary is {self.salary}") 


# ⭐) @staticmethod :- It is a decorator used why you dont want to pass (self) as  an object to a method . 

       @staticmethod     # If you dont need to put Object here then use 
       def greet():
              print("Good Morning")


harry = Employee()
harry.greet()

harry.getInfo()


# ✅ Usage :-  Used for utility methods that don’t depend on instance attributes.



'''

Output :- 

Good Morning
The language is Python . The salary is 1200000

'''




# b) Class Method (@classmethod) :- 

'''

 A class method is a method that is bound to the class and not the instance of the class. It can modify class state that applies across all instances of the class. Class methods take a cls parameter that points to the class—and not the instance—when the method is called.

 '''

# Syntax :- 
class MyClass:
    class_attribute = "I am a class attribute"

    @classmethod
    def class_method(cls):
        cls.class_attribute = "Modified statement "
        print(f"Class method called: {cls.class_attribute}")

# Usage
MyClass.class_method()      # Output :- Class method called :-  I am a class attribute



# How it Works :- 

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


# Example 2:- 

class Employee:
      a = 1            # Class Attribute 
      def show(self):
            print(f"The class value of a is {self.a}")
    
E = Employee()
E.a = 45              # output :- prints instance(object) value  =  45 

E.show()              # Output :- The class value of a is 45



# To overcome this we use @classmethod 
class Employee:
      a = 1   # Class Attribute 

      @classmethod
      def show(self):       # self or cls or something ...  anything will work.
            print(f"The class value of a is {self.a}")
    
E = Employee()
E.a = 45                   # output :- Takes  class Attribute value  = 1 Because of @classmethod 

E.show()              # Output :- The class value of a is 1



# 💡)  Class Methods as Alternative Constructors  ?


'''

1) In object-oriented programming, the term "constructor" refers to a special type of method that is automatically executed when an object is created from a class. The purpose of a constructor is to initialize the object's attributes, allowing the object to be fully functional and ready to use.

2) However, there are times when you may want to create an object in a different way, or with different initial values, than what is provided by the default constructor. This is where class methods can be used as alternative constructors.

3) A class method belongs to the class rather than to an instance of the class. One common use case for class methods as alternative constructors is when you want to create an object from data that is stored in a different format, such as a string or a dictionary. For example, consider a class named "Person" that has two attributes: "name" and "age". The default constructor for the class might look like this:

'''

# Example :- 

class Employee:
     def __init__(self , name,salary):
          self.name = name 
          self.salary = salary
 

     @classmethod
     def fromStr(cls  , string):
          return cls(string.split('-')[0] , string.split("-")[1])
     


e = Employee("Harry" , 12000)
print(e.name)                # Output :-  Harry
print(e.salary)              # Output :- 12000



# Suppose the data provided is in string format !
string  = "John-12000"

# e = Employee(string.split("-")[0] , string.split("-")[1])           # Repetative so use class Methods 
print(e.name)                # Output :- Harry
print(e.salary)              # Output :- 12000

e2 = Employee.fromStr(string)
print(e2.name)               # Output :- John
print(e2.salary)             # Output :- 12000




# c) functools.lru_cache (@lru_cache(maxsize=3) :-   The @lru_cache decorator is used to cache the results of function calls so that the function doesn’t have to re-compute the same result again.


# 💡) Why use caching ?

'''

   a) Imagine you have a function that takes a long time to compute (e.g., fetching data from a server, running complex calculations).

   b) Instead of computing the result every time, Python stores (caches) the result, so if the same input appears again, it just returns the stored value instantly. 

'''


# Example 
from functools import lru_cache

@lru_cache(maxsize=3)  # Cache up to 3 results
def expensive_function(n):
    print("Computing...")  # Prints only when computing
    return n * n

expensive_function(5)      # First call:- Computes and stores result


# ⭐) What Happens Here ?

'''

First Call :- 

        a) You call expensive_function(5).

        b) Python checks the cache → 🟥 Not found → Computes 5 * 5 = 25.

        c) Stores the result in the cache.


Output :-   Computing...


'''

# Understanding maxsize=3  ? 

'''

   a) maxsize=3 → The cache will store only the last 3 unique results.

   b) If a new value is computed beyond 3 values, the oldest cached result gets removed.

'''


expensive_function(5)  
expensive_function(10)  
expensive_function(15)  
expensive_function(5)   # Cached, won't compute again
expensive_function(20)  # Oldest (10) will be removed to store 20
expensive_function(10)  # 10 was removed earlier, so it will compute again



# 💡) Step-by-Step Execution  ? 

'''

Step-by-step execution of the function calls:  

1️⃣) First call :-  expensive_function(5)  

      a) Not in cache  

      b) Computes (5 * 5) = 25  

      c) Stores result in cache  

      d) Output: "Computing..."  


2️⃣  Second call :-  expensive_function(10)  

      a) Not in cache  

      b) Computes (10 * 10) = 100  

      c) Stores result in cache  

      d) Output: "Computing..."  


3️⃣  Third call :-  expensive_function(15)  

      a) Not in cache  

      b) Computes (15 * 15) = 225  

      c) Stores result in cache  

      d) Output: "Computing..."  


4️⃣  Fourth call :-  expensive_function(5)  

      a) Found in cache  

      b) Returns cached result (25)  

      c) No computation needed, so no output  


5️⃣  Fifth call  :-  expensive_function(20)  

      a) Not in cache

      b) Computes (20 * 20) = 400  

      c) Stores result in cache  

      d) Since maxsize=3, the oldest cached value (10) is removed  

      e) Output :-  "Computing..."  


6️⃣   Sixth call :-  expensive_function(10)  

      a) Not in cache (was removed earlier)  

      b) Computes (10 * 10) = 100 again  

      c) Stores result in cache  

      d) Output :-  "Computing..."  

'''

# ✅ Usage :-  Used for memoization in performance-critical applications.






# 💡) Key Differences Between General and Property Decorators in Python ? 

''''

1️⃣ Purpose :- 

        a) General decorators (@decorator_name) are used to modify the behavior of functions or methods, such as adding logging, authentication, or caching mechanisms.


        b) Property decorators (@property, @property.setter, @property.deleter) are specifically designed to encapsulate attribute access in classes, making instance variables behave like properties.


2️⃣ Usage :- 

        a) General decorators are applied to functions and methods, allowing modification of their execution without altering their code.

        b) Property decorators are used with class attributes, providing a controlled way to get, set, or delete attribute values.


3️⃣ Common Use Cases :- 

        a) General decorators are widely used for logging, authentication, caching, and performance monitoring.

        b) Property decorators are primarily used to define getter, setter, and deleter methods, ensuring controlled access to private attributes while maintaining clean syntax.

4️⃣ Examples :- 

        a) General decorators include @staticmethod, @classmethod, and custom decorators like @my_decorator for modifying function execution.


        b) Property decorators consist of @property, @property.setter, and @property.deleter, which facilitate attribute management in object-oriented programming.

'''