# ⭐)  dir(), __dict__ and help() methods  ? 

'''

⭐) We must look into dir(), __dict__() and help() attribute/methods in python. They make it easy for us to understand how classes resolve various functions and executes code. In Python, there are three built-in functions that are commonly used to get information about objects: dir(), dict, and help(). Let's take a look at each of them:

'''


# The dir() method :- 

# 1) dir() :-  The dir() function returns a list of all the attributes and methods (including dunder methods) available for an object. It is a useful tool for discovering what you can do with an object.


# Example :- 

x = [1,2,4]

print(dir(x))

print(x.__add__)   # <method-wrapper '__add__' of list object at 0x7a2134978b40>

'''

['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

<method-wrapper '__add__' of list object at 0x7a2134978b40>

'''






# 2) __dict__ () :- The __dict__ attribute returns a dictionary representation of an object's attributes. It is a useful tool for introspection.


#  Example :- 

class Person:
    def __init__(self , name , age):
        self.name = name 
        self.age = age 
        self.version = 1
        
        
        
p = Person("John" , 30)
print(p.__dict__)          #  The self values / we will get the attributes from this object as a dictionary      

''' 

Output :- {'name': 'John', 'age': 30, 'version': 1}

'''




# 3) help() :-  The help() function is used to get help documentation for an object, including a description of its attributes and methods. 



# Example :- 


class Person:
    def __init__(self , name , age):
        self.name = name 
        self.age = age 
        self.version = 1
        
        
        
p = Person("John" , 30)


print(help([]))



'''

Output :- 


Help on list object:

class list(object)
 |  list(iterable=(), /)
 |
 |  Built-in mutable sequence.
 |
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |
 |  Methods defined here:
 |
 |  __add__(self, value, /)
 |      Return self+value.
 |
 |  __contains__(self, key, /)
 |      Return bool(key in self).
 |
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |
 |  __eq__(self, value, /)
 |      Return self==value.
--More--


'''



'''

>>> In conclusion, dir(), dict, and help() are useful built-in functions in Python that can be used to get information about objects. They are valuable tools for introspection and discovery.


'''