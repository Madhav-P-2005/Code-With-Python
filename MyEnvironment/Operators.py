# Operators 

# Arithmetic Operators
a = 7
b =4 
c = a + b
print(c)

# Assignment Operators 
a = 4-2
print(a)

b = 6
b += 3 # Increment the value of b by 3 and then assign it to b 
b -= 3  # Decrement the value of b by 3 and then assign it to b 
print(b)


# Comparison Operators 
d = 5 < 4 
print(d)

d = 5 <= 4 
print(d)

d = 5 >= 4 
print(d)


d = 5!=5 
print(d)

d = 5==5 
print(d)


# Logical Operators 
e = True or False
print(e)
i = True and False
print(i)

# Truth table of 'or
print("True or False is ",True or False)
print("True or True is ",True or False)
print("False or True is ",False or True)
print("False or False is ",False or False)

# Truth table of 'and'
print("True and False is ",True and False)
print("True and True is ",True and False)
print("False and True is ",False and True)
print("False and False is ",False and False)

print(not(False))
print(not(True))


# Type() Function
a = 31.2
t = type(a) # class <int>
print(t)

# Type Casting 
a = 32.9
b = complex(a)
print(b)
print(type(b))


# Input Function
a = input("Enter number 1 :- ") # 1 
b = input("Enter number 2 :- ") # 2
print("Number 2 is :- " ,b)
print("Number a is :-  " ,a)
print("Sum is ", a +b) # output 12 as it takes string it concatinates 


a = int(input("Enter number 1 :- ")) # 1 
b = int(input("Enter number 2 :- ")) # 2
print("Number 2 is :- " ,b)
print("Number a is :- " ,a)
print("Sum is ", a +b) # output 3 

# Identity Operators :- Identity operators in Python are used to compare the memory locations of two objects. They determine whether two variables point to the same object in memory. There are two identity operators :-

# is: Returns True if both variables point to the same object.

a = [1, 2, 3]
b = [1 ,2 ,3]
print(a is b)  # Output :- False
print()
b = a
print(a is b)  # Output :- True 
print()
c = [1, 2, 3]
print(a is b)  # Output: True (both a and b refer to the same object in memory)
print(a is c)  # Output: False (a and c refer to different objects with the same content)

# Immutable Types: For small integers and short strings, Python may reuse memory addresses.
# For example :- 
a = 256
b = 256
print(a is b)  # Output: True

print()

# Mutable Types: Lists, dictionaries, and other mutable types will have different memory addresses unless explicitly assigned:-
# For example :- 
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 is list2)  # Output: False



print()

# is not: Returns True if both variables do not point to the same object.
a1 = [1,2,3]
b1 = [1,2,3]
print(a1 is not b1)

print()

x = 42
y = 42
z = 43

print(x is not y)  # Output: False (both x and y refer to the same object in memory for small integers)
print(x is not z)  # Output: True (x and z refer to different objects)


# Membership operators :- Membership Operators in Python are used to test whether a value is found within a sequence (such as a string, list, tuple, set, or dictionary). There are two membership operators:

# Use Cases :- 

'''

Strings :-  Checking if a substring exists within a string.

Lists :-  Determining if an element is present in a list.

Tuples :- Identifying if an item exists in a tuple.

Sets :- Verifying membership in a set.

Dictionaries :- Checking if a key exists in a dictionary. 

'''


# in :- Returns True if the specified value is found in the sequence.

# Example with a list
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)  # Output: True

# Example with a string
text = "Hello, World!"
print("World" in text)  # Output: True

# Example with a tuple
numbers = (1, 2, 3, 4, 5)
print(3 in numbers)  # Output: True

# Example with a set
unique_numbers = {1, 2, 3, 4, 5}
print(5 in unique_numbers)  # Output: True

# Example with a dictionary (checks keys by default)
person = {"name": "Alice", "age": 30}
print("name" in person)  # Output: True
print("Alice" in person)  # Output: False
print()

# not in:- Returns True if the specified value is not found in the sequence.


# Example with a list
fruits = ["apple", "banana", "cherry"]
print("grape" not in fruits)  # Output: True

# Example with a string
text = "Hello, World!"
print("Python" not in text)  # Output: True

# Example with a tuple
numbers = (1, 2, 3, 4, 5)
print(6 not in numbers)  # Output: True

# Example with a set
unique_numbers = {1, 2, 3, 4, 5}
print(0 not in unique_numbers)  # Output: True

# Example with a dictionary (checks keys by default)
person = {"name": "Alice", "age": 30}
print("address" not in person)  # Output: True
print("Alice" not in person)  # Output: True


