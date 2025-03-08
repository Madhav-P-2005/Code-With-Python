# ✨ Magic (Dunder) Methods  in Python ✨  ?


# 📌 What are Magic (Dunder) Methods ?

'''

⭐) Magic methods (also called dunder methods, short for "Double UNDERscore") are special methods in Python that start and end with double underscores (__).

💡) They are automatically invoked by Python for specific operations on objects, such as :-

✅ Object creation

✅ Operator overloading

✅ Attribute access

✅ Function invocation

✅ Object representation


Example :-  __init__(), __str__(), __len__(), etc.

'''



# 🏆 How Do Magic Methods Work ?

'''

⭐) Magic methods work by automatically handling built-in operations in Python.

For example :-

🔹 When you call len(obj), Python internally calls obj.__len__()

🔹 When you add a + b, Python calls a.__add__(b)

🔹 When you print an object print(obj), Python calls obj.__str__()

'''



# 🚀 Types of Magic Methods in Python ? 

# ⭐) Magic methods are categorized into six major types :-

'''

1️⃣ Object Construction & Initialization (__new__, __init__, __del__)

2️⃣ String Representation (__str__, __repr__)

3️⃣ Operator Overloading (__add__, __sub__, __mul__, etc.)

4️⃣ Comparison & Rich Comparisons (__eq__, __lt__, __gt__, etc.)

5️⃣ Attribute Access (__getattr__, __setattr__, __delattr__, etc.)

6️⃣ Function-Like Behavior (__call__, __len__, __getitem__, etc.)

'''



#  1️⃣)  Object Construction & Initialization  :-   These methods are called when an object is created or destroyed.




# a)  __new__(cls, *args, **kwargs) :-    Creates a new instance (rarely used)

class Test:
    def __new__(cls):
        print("Creating instance...")
        return super().__new__(cls)

    def __init__(self):
        print("Initializing instance...")

obj = Test()  


'''
# Output : Creating instance...
           Initializing instance...

'''



# b)  __init__(self, *args, **kwargs) :-  Initializes the object

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("John", 25)
print(p.name)         # Output :-  John




# c)  __del__(self) :-  Destructor (called when an object is about to be destroyed) :- 

class Example:
    def __del__(self):
        print("Object is being deleted!")

obj = Example()
del obj            # Output :-  Object is being deleted!




# 2️⃣) String Representation :-   These methods define how an object looks when printed or converted to a string.


#  a) __str__() :-  Used by print() (User-Friendly Representation)

class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book Title: {self.title}"

b = Book("Python Essentials")
print(b)       # Output :-   Book Title: Python Essentials




# b) __repr__() :-  Official Representation (Used for Debugging)


class Book:
    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return f'Book("{self.title}")'

b = Book("Python Essentials")
print(repr(b))     # Output :-  Book("Python Essentials")




# 3️⃣) Operator Overloading  :-  These methods allow customizing built-in operators (+, -, *, /, etc.).


# a) __add__() :-  Overloads + operator :- 

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

a = Number(5)
b = Number(10)
c = a + b     # Calls a.__add__(b)
print(c.value)    # Output:-  15




# b) __mul__() :-  Overloads * operator


class Number:
    def __init__(self, value):
        self.value = value

    def __mul__(self, other):
        return Number(self.value * other.value)

a = Number(3)
b = Number(4)
c = a * b      # Calls a.__mul__(b)
print(c.value)  # Output :-  12




# 4️⃣) Comparison & Rich Comparisons :- These methods define custom comparison behavior (==, <, >, etc.).


# a) __eq__() :-  Overloads ==

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

p1 = Person("Alice", 30)
p2 = Person("Bob", 30)
print(p1 == p2)  # Output :-  True




# b)  __lt__() :-  Overloads < (Less than)   :- 


class Number:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

a = Number(5)
b = Number(10)
print(a < b)  # Output: True





# 5️⃣)  Attribute Access  :- These methods control how attributes are accessed, set, or deleted.


# a) __getattr__() :-  Called when an attribute doesn't exist


class Example:
    def __getattr__(self, name):
        return f"{name} does not exist!"

obj = Example()
print(obj.unknown)    # Output :- unknown does not exist!



# b)  __setattr__() :-  Called when setting an attribute

class Example:
    def __setattr__(self, name, value):
        print(f"Setting {name} to {value}")
        super().__setattr__(name, value)

obj = Example()
obj.name = "Alice"   # Output :-  Setting name to Alice





# 6️⃣) Function-Like Behavior :-   These methods allow objects to behave like functions.


# a) __call__() :-  Allows an object to be called like a function

class Greeting:
    def __call__(self, name):
        print(f"Hello, {name}!")

greet = Greeting()
greet("Alice")   # Output :-  Hello, Alice!




# b)  __len__() :-  Allows len(obj) to work.


class Team:
    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)

team = Team(["Alice", "Bob", "Charlie"])
print(len(team))     # Output :-  3






# 🎯 Key Takeaways

'''

✅ Magic Methods are built-in Python methods that allow customizing object behavior.

✅ They are automatically called in specific scenarios (e.g., +, ==, print(obj)).

✅ Used for object creation, string representation, operator overloading, attribute access, and more.

✅ They help in writing clean, reusable, and readable code.

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



print(n + m)        # Output :- unsupported operand type(s) for +: 'Number' and 'Number'
result = n + m 
print(result.n)     # Output: 3


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