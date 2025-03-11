'''

⭐) Access Modifiers in Python define the scope and visibility of variables and methods within a class. They determine how attributes and methods can be accessed from inside and outside a class.

⭐) Python does not have strict access control like other languages (Java, C++), but it follows a naming convention to indicate the intended level of access.

'''


# Types of access specifiers  ? 


'''

1️⃣) Public (public) → Accessible from anywhere.

2️⃣) Protected (_protected) → Intended to be used within the class and subclasses.

3️⃣) Private (__private) → Accessible only within the class (Name Mangling applies).

'''


# ⚡ How Access Modifiers Work in Python?

'''
Python does not enforce strict access control like Java or C++. Instead, it follows a naming convention :- 


⭐) Public :-   Accessible anywhere.

⭐) Protected :-  Accessible inside the class and subclasses (but not enforced).

⭐) Private :-  Not directly accessible, but can be accessed using name mangling (_ClassName__privateVar).

'''


# 1️⃣) Public Access Specifier  ? 


# ✅ Definition :- 

'''

a) Attributes and methods declared without an underscore (_) are public by default.

b) They can be accessed inside and outside the class.

c) All the variables and methods (member functions) in python are by default public. Any instance variable in a class followed by the ‘self’ keyword ie. self.var_name are public accessed.

'''

# 📌 Usage :-    Used for attributes and methods that should be accessible from anywhere.


# Example :- 
class Student:

    # constructor is defined
    def __init__(self, age, name):
        self.age = age               # public variable

        self.name = name             # public variable


obj = Student(21,"Harry")
print(obj.age)                    

print(obj.name)


'''

Output :- 

21
Harry

'''




# 2️⃣) Protected Access Modifier :- 

'''

✅ Definition :- 

   a) Attributes and methods prefixed with a single underscore (_) are considered protected.

   b) By convention, protected members should be used only within the class and subclasses, but Python does not enforce this restriction.

   c) Can still be accessed outside the class (not truly private).

   d) In object-oriented programming (OOP), the term "protected" is used to describe a member (i.e., a method or attribute) of a class that is intended to be accessed only by the class itself and its subclasses. In Python, the convention for indicating that a member is protected is to prefix its name with a single underscore (_). For example, if a class has a method called _my_method, it is indicating that the method should only be accessed by the class itself and its subclasses.

   e) It's important to note that the single underscore is just a naming convention, and does not actually provide any protection or restrict access to the member. The syntax we follow to make any variable protected is to write variable name followed by a single underscore (_) ie. _varName.

'''


# Example :- 

class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()

# calling by object of Student class

print(obj._name)      

print(obj._funName())     

# calling by object of Subject class

print(obj1._name)    

print(obj1._funName())


'''

Output :- 

Harry
CodeWithHarry
Harry
CodeWithHarry

'''



'''

📌) Usage :- 

a) Used when a variable or method should not be modified directly but can be accessed in child classes.

b) Mostly used in inheritance.

'''





# 3️⃣)  Private Access Modifier  :- 

'''

✅ Definition :- 

a) Attributes and methods prefixed with double underscores (__) are considered private.

b) They can only be accessed inside the class.

c) Python performs name mangling, which changes __privateVar to _ClassName__privateVar.

d) By definition, Private members of a class (variables or methods) are those members which are only accessible inside the class. We cannot use private members outside of class.

e) In Python, there is no strict concept of "private" access modifiers like in some other programming languages. However, a convention has been established to indicate that a variable or method should be considered private by prefixing its name with a double underscore (__). This is known as a "weak internal use indicator" and it is a convention only, not a strict rule. Code outside the class can still access these "private" variables and methods, but it is generally understood that they should not be accessed or modified.

'''


# Example :- 
class Employee:
      def __init__(self):
           self.__name = "Shyam"


obj = Employee()

print(obj.__name)     # Cannot be accessed directly 



# Name mangling :- 

'''

⭐) Name mangling in Python is a technique used to protect class-private and superclass-private attributes from being accidentally overwritten by subclasses. Names of class-private and superclass-private attributes are transformed by the addition of a single leading underscore and a double leading underscore respectively.

'''

print(obj._Employee__name)    # Output :- Harry    name mangling


print(obj.__dir__())    # Shows all the methods 


'''

['_Employee__name', '__module__', '__init__', '__dict__', '__weakref__', '__doc__', '__new__', '__repr__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__reduce_ex__', '__reduce__', '__getstate__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']

'''

        


'''

📌) Usage :- 

    a) Used when an attribute or method should not be accessed outside the class.

    b) Typically used in sensitive data like passwords, balance, etc.

    c) If needed, provide getter (get_) and setter (set_) methods to control access.

'''





# ✅ When to Use Access Modifiers?

'''

🔹 Use public when the attribute/method should be available everywhere.

🔹 Use protected when it should be accessible only inside the class and subclasses.

🔹 Use private when it should be strictly restricted to the class.


💡 Example Use Case :- 

      a) Public → General attributes (name, age).

      b) Protected → Internal logic that subclasses may use (_config).

      c) Private → Sensitive data (__password, __balance).

'''