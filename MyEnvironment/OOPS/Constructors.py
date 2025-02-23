# ⭐) Types of Constructors in Python  ? 


# 1) Parameterized Constructor in Python :- 

'''

a) When the constructor accepts arguments along with self, it is known as parameterized constructor.

b) These arguments can be used inside the class to assign the values to the data members.

'''


# Example :- 
class Details:

    def __init__(self, animal, group):
        self.animal = animal
        self.group = group

obj1 = Details("Crab", "Crustaceans")

print(obj1.animal, "belongs to the", obj1.group, "group.")      # Output :- Crab belongs to the Crustaceans group.




# 2) Default Constructor in Python  :- 

'''

a) When the constructor doesn't accept any arguments from the object and has only one argument, self, in the constructor, it is known as a Default constructor.

'''

# Example :- 
class Details:
  def __init__(self):
    print("animal Crab belongs to Crustaceans group")

obj1=Details()        # Output :-   animal Crab belongs to Crustaceans group




# ⭐)  The __init__() Function :-  The __init__() function in Python is a special method, often referred to as a "constructor" in object-oriented programming. It's a type of dunder (double underscore) method that gets called automatically when an instance (object) of a class is created.


'''

●  The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

●  It is a special method which is called dunder method . In python the methods which starts with and underscore __ is called as dunder method .

●  To understand the meaning of classes we have to understand the built-in __init__() function.

●  All classes have a function called __init__(), which is always executed when the class is being initiated.

●  Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created.


# 💡) Key Points About __init__() :- 

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
              self.language = "Java"      # Will not modify use class method if you want to modify. 
              print(f"The language is {self.language} . The salary is {self.salary}") 



       @staticmethod     
       def greet():
              print("Good Morning")


# harry = Employee()               #  Output :- I am creating an Object
harry = Employee("Harry" , 1300000 , "JavaScript")

harry.name = "Madhav"

print(harry.name , harry.language ,harry.salary)            # Output :- Harry Python 1200000

rohan = Employee()                                       # Output :- I am creating an Object

rohan.getInfo()


'''

TypeError :-  Employee.__init__() missing 3 required positional arguments: 'name', 'language', and 'salary

'''

print('\n')