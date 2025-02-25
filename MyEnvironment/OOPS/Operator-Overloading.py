'''

⭐) Operator Overloading allows you to define custom behaviors for Python's built-in operators (like +, -, *, etc.) when applied to user-defined objects. This is achieved by defining magic methods (also called dunder methods) in your class.

'''


# 📌 Key Points

'''

1️⃣) Built-in Operators :-  Operators like +, -, *, ==, and others work with built-in types.

2️⃣) Custom Behavior :-  You can redefine these operators for your custom classes using magic methods such as __add__, __sub__, __eq__, etc.
    
3️⃣) Magic Methods :-  These are special methods in Python surrounded by double underscores (e.g., __add__ for +).

'''



# 📃 Syntax :- 

class MyClass:
    def __add__(self, other):
        # Custom behavior for '+'
        return self.some_value + other.some_value



# Example 
class Vector:
    def __init__(self , i , j , k):
        self.i  = i
        self.j = j
        self.k = k

    
    def __str__(self):
        return f"{self.i}i  + {self.j}j  + {self.k}k"
    
    def __add__(self , x):
        return f"{self.i  + x.i}i +  {self.j + x.j}j + {self.k + x.k}k"
        
    # To convert string out to  Vector     
    def __add__(self , x):
        return Vector(self.i  + x.i ,  self.j + x.j ,  self.k + x.k)


v1 = Vector(3 ,  5, 6)
print(v1)                  # Output :-  3i  + 5j  + 6k

v2 = Vector(1 ,  2, 9)
print(v2)                  # Output :-  1i  + 2j  + 9k


print(v1 + v2)             # Output :-  4i +  7j + 15k

print(type (v1 + v2))      # Output :-  <class 'str'>

print(type (v1 + v2))      # Output :-  <class '__main__.Vector'>



# 🎯 Types of Magic Methods for Overloading

# Here are some common operators and their corresponding magic methods :-

'''

1) Addition (+) :-

    Magic Method :-  __add__(self, other)
    Example :-  obj1 + obj2

2) Subtraction (-) :-

    Magic Method :-  __sub__(self, other)
    Example :-  obj1 - obj2

3) Multiplication (*) :- 

    Magic Method :-  __mul__(self, other)
    Example :-  obj1 * obj2

4) Division (/) :-

    Magic Method :-  __truediv__(self, other)
    Example :-  obj1 / obj2

5) Equality (==) :-

    Magic Method :-  __eq__(self, other)
    Example :-  obj1 == obj2

6) Less Than (<) :-

    Magic Method :-  __lt__(self, other)
    Example :-  obj1 < obj2

7) Greater Than (>) :-

    Magic Method :-  __gt__(self, other)
    Example :-  obj1 > obj2

8) Indexing ([]) :-

    Magic Method :-  __getitem__(self, key)
    Example :-  obj[key]

'''

