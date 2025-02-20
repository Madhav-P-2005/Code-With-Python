# 🔥 Method Overloading in Python  ?

'''

⭐) Method overriding is a powerful feature in object-oriented programming that allows you to redefine a method in a derived class. The method in the derived class is said to override the method in the base class. When you create an instance of the derived class and call the overridden method, the version of the method in the derived class is executed, rather than the version in the base class.

⭐) In Python, method overriding is a way to customize the behavior of a class based on its specific needs. For example, consider the following base class:

'''



# Syntax :- 

class Parent:
    def show(self):
        print("This is the parent class method")

class Child(Parent):
    def show(self):  # Overriding the parent method
        print("This is the child class method")

# Creating objects
p = Parent()
c = Child()

p.show()  # Calls Parent's method
c.show()  # Calls Child's method (Overriding)



'''

Output :- 

This is the parent class method
This is the child class method


'''




# Example :- 

class Shape:
    def __init__(self, x , y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y
    


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius , radius)          # 25

    def area(self):
        return 3.14 * super().area()


rec = Shape(3 , 5)

print(rec.area())
  
cir = Circle(5)

print(cir.area())



'''

Output :- 

15 
78.5

'''




# 🔥 Real-World Example: Method Overriding in Banking System  ?

class BankAccount:
    def interest_rate(self):
        return "Interest rate is 5%"

class SavingsAccount(BankAccount):
    def interest_rate(self):
        return "Interest rate for savings account is 6%"

class FixedDepositAccount(BankAccount):
    def interest_rate(self):
        return "Interest rate for fixed deposit is 7.5%"

# Creating objects
savings = SavingsAccount()
fd = FixedDepositAccount()

print(savings.interest_rate())  # Overridden method in SavingsAccount
print(fd.interest_rate())  # Overridden method in FixedDepositAccount



'''

Output :- 

Interest rate for savings account is 6%
Interest rate for fixed deposit is 7.5%


'''




# 🔍 How Method Overriding Works? 

'''

1️⃣ Inheritance :-  The child class 
inherits from the parent class.

2️⃣ Same Method Name :-  The child class defines a method with the same name as the parent class.

3️⃣ Overriding :-  When the method is called on the child class object, Python executes the child class method instead of the parent class method.

'''




# 🎯 Usage of Method Overriding  

'''

✔ Polymorphism :-  It allows different behaviors for the same method in 
different classes.

✔ Extending Functionality :-  The child class can modify the behavior of an inherited method.

✔ Accessing Parent Methods :-  With super(), we can call the parent method before or after overriding.

'''




# ✅ How Does It Work in Python?

'''

Since Python does not allow multiple methods with the same name, we can simulate method overloading using :- 

1️⃣ Default Parameters

2️⃣ Variable-length Arguments (*args, **kwargs)

3️⃣ Function Overloading with @singledispatch (from functools)

'''