# Dictionary is an unordered collection of data stored as a pair of key and value
# The order in which the elements are placed are not in an order .  They are mutable in nature 

# variable_name=(key1 : value1,key2 :value2....) .


# Creating an empty Dictionary 
d1={}
print(d1)
print(type(d1))


marks = {
    "Harry" : 100,
    "Shubam" : 56,
    "Rohan" : 23
}
print(marks, type(marks))

# print(marks[0]) # error 

print(marks["Harry"])

# Dictionary Methods 

# 1) Keys() Method :- Returns a view object that displays a list of all the keys in the dictionary.

print("Keys are :- ",marks.keys())

# 2) Values() Method :- Returns a view object that displays a list of all the values in the dictionary.

print("Values are :- ",marks.values())

# 3) Update() Method :- Updates the dictionary with elements from another dictionary or from an iterable of key-value pairs.

marks.update({"Harry" : 99 , "Renuka" : 100})
print(marks)

# 4) get() Method :- Returns the value for the specified key if the key is in the dictionary. Otherwise, it returns a default value.

my_dict = {"name": "Alice", "age": 30}
age = my_dict.get("age", "Not Found")
print(age)  # Output: 30
gender = my_dict.get("gender", "Not Found")
print(gender)  # Output: Not Found


print(marks.get("Harry"))  # Prints None
print(marks["Harry"])  # Returns Error 


# 5) clear() Method :- Removes all elements from the dictionary.

my_dict = {"name": "Alice", "age": 30, "city": "New York"}
my_dict.clear()
print(my_dict)  # Output: {}


# 6) copy() Method :- Returns a shallow copy of the dictionary.

my_dict = {"name": "Alice", "age": 30, "city": "New York"}
new_dict = my_dict.copy()
print(new_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}


# 7) fromkeys() Method :- Creates a new dictionary with keys from an iterable and values set to a specified value.

keys = ["name", "age", "city"]
default_value = None
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)  # Output: {'name': None, 'age': None, 'city': None}


# 8) items() Method :- Returns a view object that displays a list of dictionary's key-value tuple pairs.

my_dict = {"name": "Alice", "age": 30}
items = my_dict.items()
print(items)  # Output: dict_items([('name', 'Alice'), ('age', 30)])


# 9) pop() Method :-  Removes the element with the specified key and returns its value. If the key is not found, it raises a KeyError.

my_dict = {"name": "Alice", "age": 30}
age = my_dict.pop("age")
print(age)  # Output: 30
print(my_dict)  # Output: {'name': 'Alice'}


# 10) popitem() Method :- popitem() :- Removes and returns the last inserted key-value pair as a tuple. If the dictionary is empty, it raises a KeyError.

my_dict = {"name": "Alice", "age": 30}
item = my_dict.popitem()
print(item)  # Output: ('age', 30)
print(my_dict)  # Output: {'name': 'Alice'}

# 11) setdefault() :- Returns the value of a specified key. If the key does not exist, it inserts the key with the specified value.

my_dict = {"name": "Alice"}
age = my_dict.setdefault("age", 30)
print(age)  # Output: 30
print(my_dict)  # Output: {'name': 'Alice', 'age': 30}


# Nested Dictionary :-  Dictionary Within a Dictionary
d6={"name":{"first":"sam","last":"Crew"},"age":22,"profession":"student"}
print(d6)


# Add elements to the Dictionary
d={}
d[0] = "Welcome"
print(d)

d[1] = ("How","are","you")
print(d)


# Strings can also be the keys in Dictionary
d["name"]="Sam"
print(d)


# You can a dictionary as an element  in a already Exsisting Dictionary   # Here we are updating the key element 
d["name"]={"first":"Sam","last":"Crew"}
print(d)

# Retrieve the Value form the dictionary
print(d["name"])


# Want to Access the element just key first within the key name
print(d["name"]["first"])


# Write a Python program to store and retrieve player names and their run scores using a dictionary. Ensure to prompt for the player's name and runs ?
dict = {}
print("How many players ? ",end=" ")
n = int(input())
for i in range(n):
    print("Enter Player Name " , end = "")
    p = input()
    print("Enter the runs ",end = " ")
    r = int(input())
    dict.update({p:r})

print("\nPlayers in this Match :- ")
for pname in dict.keys():
    print(pname)

print("Enter the player name :-  ",end= " ")
name=input()
runs=dict.get(name,-1)
if runs==-1:
    print(f"{name} Player Not Found ")
else:
    print('{} made {} '.format(name,runs))


# Slicing Dictionaries :- No, slicing is not possible with dictionaries. Slicing is a feature available for sequences like lists, tuples, and strings. Dictionaries are unordered collections of key-value pairs, so they do not support indexing or slicing.




# Sets :- A set is an unordered collection of unique elements. Sets are mutable, meaning you can add or remove elements, but all the elements must be immutable (e.g., numbers, strings, tuples). Sets are particularly useful for operations that involve membership testing, removing duplicates, and mathematical operations like unions and intersections. Slicing is not possible in Sets 

# Key Characteristics of Sets :- 

# 1) Unordered: Elements in a set do not have a specific order.

# 2) Unique: Each element in a set must be unique.
s = {1,5,32,5.4,5,5,5,5 , "Madhav"}
print(s)  # Doesnot take care of order . If order required use lists not sets . 

# 3) Mutable: You can add or remove elements from a set.


# Creating Sets :- You can create a set using curly braces {} or the set() constructor:

# Using curly braces
my_set1 = {1, 2, 3, 4, 5}
print(type(my_set1))

# Empty Dictionary 
my_set2 = {}
print(type(my_set2))  # Output :- <class 'dict'>

# Creating a Empty Set 
s = set()
print(type(s))        # Output :- <class 'set'>
print()

# Using the set() constructor
another_set = set([1, 2, 3, 4, 5])
print(another_set)
print()

s1 =  {1 , 23 , 45}
s2 = {6 , 1,  3 ,34, 23, 54}
data = s1 - s2
print(data)   # Output :- {45}

# Set Methods :- 

# 1) Add() Method :- Adds an element to the set.
s1 = {1,5,32,54,5,5,5,"Harry"}
s1.add(566)
print(s1 , type(s1))
print()

# 2) clear() Method :- Removes all elements from the set.
my_set = {1, 2, 3}
my_set.clear()
print(my_set)  # Output: set()

# 3) Copy() Method :- Returns a shallow copy of the set.
my_set = {1, 2, 3}
new_set = my_set.copy()
print(new_set)  # Output: {1, 2, 3}

# 4) discard() Method :- Removes a specified element from the set if it is a member. If the element is not a member, do nothing.
my_set = {1, 2, 3}
my_set.discard(2)
print(my_set)  # Output: {1, 3}

# 5) pop() Method :- Removes and returns an arbitrary element from the set. Raises KeyError if the set is empty.
my_set = {1, 2, 3}
elem = my_set.pop()
print(elem)  # Output: 1 (or any other element)

# 6) remove() Method :- Removes the specified element from the set. Raises KeyError if the element is not found.
my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)  # Output: {1, 3}

# 7) update() Method :- Updates the set with the union of itself and another set.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.update(set2)
print(set1)  # Output: {1, 2, 3, 4, 5}


# 8) union() Method :- 
s1 = {1, 45 ,6 ,78}
s2 = {7, 8, 1, 78}
print("Union :- ", s1.union(s2))


# 9) intersection() Method :- 
s1 = {1, 45 ,6 ,78}
s2 = {7, 8, 1, 78}
print("Intersection :- ",s1.intersection(s2))
print()

# 10) intersection_update() :- Updates the set with the intersection of itself and another set.
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.intersection_update(set2)
print("Original set1 :- ",set1)  # Output: {2, 3} (only the common elements)
print()


# 11) difference() Method :- Returns the difference between two or more sets as a new set.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
diff_set = set1.difference(set2)
print("Difference :- ",diff_set)  # Output: {1, 2}
print("Original set1 :- ",set1) # Output: {1, 2, 3, 4} (original set remains unchanged)
print()

# 12) symmetric_difference() :- Returns the symmetric difference of two sets as a new set.
set1 = {1, 2, 3}
set2 = {2, 3, 4}
sym_diff_set = set1.symmetric_difference(set2)
print("Symmetric_difference :- ",sym_diff_set)  # Output: {1, 4}
print()


# 13) symmetric_difference_update() :- Updates the set with the symmetric difference of itself and another set.
set1 = {1, 2, 3}
set2 = {2, 3, 4}
new_set =set1.symmetric_difference_update(set2)
print("Symmetric_difference_update  :- ",new_set)
print("Original set1 symmetric_difference_update",set1)  # Output: {1, 4}
print()


# 14) difference_update() Method :- Removes the elements found in another set from the current set.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
diff_update = set1.difference_update(set2)
print("Difference Update :- " ,diff_update)  
print("Original set1 :- ",set1) # Output: {1, 2} (original set is modified)
print()


# 15) isdisjoint() Method :- Returns True if two sets have a null intersection.
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print("isdisjoint :- ",set1.isdisjoint(set2))  # Output: True
print()


# 16) issubset() Method :- Returns True if another set contains this set.
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
print("issubset :- ",set1.issubset(set2))  # Output: True
print()


# 17) issuperset() Method :- Returns True if this set contains another set.
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}
print("issuperset :- ",set1.issuperset(set2))  # Output: True



