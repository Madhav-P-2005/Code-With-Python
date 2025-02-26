# ⭐) Property Decorators (@property)  :-

''' 

1️⃣) Property decorators in Python are used to define methods in a class that can be accessed like attributes. They allow you to define getter, setter, and deleter methods, providing a way to manage the internal state of a class in an organized manner.

2️⃣) Property decorators specifically deal with class attributes.


3️⃣) The built-in @property decorator makes a method behave like an attribute.

'''


# How it Works :-
 
'''

  a) Property decorators work by transforming methods into read-only or read-write properties of the class. When you use the @property decorator, it turns the method into a getter for a managed attribute.

  b) If you also provide methods decorated with @<property_name>.setter and @<property_name>.deleter, you can control setting and deleting the attribute.

'''




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




# Types of Property Decorators ?

'''

1) Getter :-  Define a method that retrieves the value of an attribute and decorate it with @property.

2) Setter :-  Define a method that sets the value of an attribute and decorate it with @<property_name>.setter.

3) Deleter :- Define a method that deletes an attribute and decorate it with @<property_name>.deleter.

'''



# Example :- 

# Without Property Decorators 
class Employee:
    def __init__(self , first , last):
        self.first = first         # Attribute

        self.last = last           # Attribute

        self.email = first + '.' + last + '@email.com'             # Attribute

    
    def fullname(self):                   # Method
        return '{} {}'.format(self.first , self.last)
    

employee1 = Employee('Shiv' , 'Shankar')

employee1.first = 'Manav'


print(employee1.first)

print(employee1.last)

# print(employee1.fullname)            # Output :-   <bound method Employee.fullname of <__main__.Employee object at 0x7172c9cb5af0>>


'''

  a) As here we can see employee1.fullname cannot be taken as attribute while others are attributes , it has to be accessed in a method format .
 
 
  b) So the issue here is that it will break the code for everyone currently using the class so they would have to go through and change every instance of the email attribute with an email method now . 

  c) Due to this we use Getters , Setters and Deleters . 

'''

print(employee1.fullname())           # Shiv Shankar  or Manav Shankar

print(employee1.email())


'''

Output :- 

Manav
Shankar
Manav Shankar
Shiv.Shankar@email.com

'''



# 1️⃣)  With @property Decorators (Getters)   :-   Converts a method into a read-only property, allowing attribute-like access.
class Employee:
      
      def __init__(self , first , last):
          self.first = first
          self.last = last 

      @property            # Getter
      def email(self):                   # Method
            return '{} {}@email.com.'.format(self.first , self.last)
      

      @property            # Getter 
      def fullname(self):
          return '{} {}'.format(self.first, self.last)
      

      @fullname.setter              # Setter
      def fullname(self, Name):
          first , last = Name.split(' ')
          self.first = first 
          self.last = last 


employee1 = Employee('Mothi' , 'lal')

# employee1.fullname = "shruti hasan"     # AttributeError: property 'fullname' of 'Employee' object has no setter


employee1.first = "Raj"

print(employee1.first)       # Raj

print(employee1.last)        # lal

print(employee1.email)       # Raj lal@email.com

print(employee1.fullname)    # Raj lal





# 2️⃣ and 3️⃣)  With @property Decorators , Setters and Deleters 
class Employee:
      
      def __init__(self , first , last):
          self.first = first
          self.last = last 

      @property
      def email(self):            # Method
            return '{} {}@email.com.'.format(self.first , self.last)
      
      @property                   # Getter 
      def fullname(self):
          return '{} {}'.format(self.first, self.last)
      

      @fullname.setter            # Setter 
      def fullname(self, Name):
          first , last = Name.split(' ')
          self.first = first 
          self.last = last 


      @fullname.deleter           # Deleter
      def fullname(self):
          print(f"{self.fullname} got Deleted ! ")
          self.first =  None
          self.last =   None



employee1 = Employee('Mothi' , 'lal')

employee1.fullname = "shruti hasan"    

print(employee1.first)         # shruti 

print(employee1.last)          # hasan

print(employee1.email)         # shruti hasan@email.com

print(employee1.fullname)      # shruti hasan


del employee1.fullname         # shruti hasan got Deleted ! 

print(employee1.fullname)             


'''

Output :- 

shruti
hasan
shruti hasan@email.com.
shruti hasan
shruti hasan got Deleted ! 
None None

'''