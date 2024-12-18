# List is a collection of data . It can hold values of multiple data types . They are mutable(can be modified) in nature 


# here 1 'st positon is 0 and last element = last number - 1

friends = ["Apple" , "Orange" , 5 ,345.06 ,False , "Aakash ", "Rohan"]

print(friends[0])
friends[0] = "Grapes"  # Unlike Strings Lists are Mutable . 
print(friends[0])
print(friends)
print()


# Creating List of Lists
marks = [["Harry" , 100 ],["Raghav" , 95],["Kiran" , 99 ]]
print("List of lists is :- ",marks)
print()


# Slicing :-

print(friends[:4])
print(friends[0:])
print(friends[1:4])
print()

# Negative Slicing :- 
fruits = ["apple", "banana", "cherry", "date", "fig"]

# Access the last element
print(fruits[-1])  # Output: fig

# Access the second-to-last element
print(fruits[-2])  # Output: date

# Access the third-to-last element
print(fruits[-3])  # Output: cherry

print()

# Slice the last three elements
print(fruits[-3:])  # Output: ['cherry', 'date', 'fig']

# Slice all elements except the last two
print(fruits[:-2])  # Output: ['apple', 'banana', 'cherry']

# Slice the second-to-last to the last element
print(fruits[-2:])  # Output: ['date', 'fig']


# Using the :: Syntax for Slicing :- The slicing syntax in Python uses the start:stop:step format, and you can use negative steps to reverse the list or sequence :-

# Original list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Slice the list with a positive step
print(numbers[1:8:2])  # Output: [2, 4, 6, 8]

# Slice the list with a negative step (reversing the list)
print(numbers[::-1])  # Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Slice the list with a negative step from end to start
print(numbers[8:3:-1])  # Output: [9, 8, 7, 6, 5]

# Practical Examples
# Reverse a List
# Using the slicing syntax [::-1] to reverse a list :-

fruits = ["apple", "banana", "cherry", "date", "fig"]
reversed_fruits = fruits[::-1]
print(reversed_fruits)  # Output: ['fig', 'date', 'cherry', 'banana', 'apple']

# Extracting Every Second Element :-   Using slicing to extract every second element :-


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
every_second = numbers[::2]
print(every_second)  # Output: [1, 3, 5, 7, 9]

print()

# List Methods 
friends = ["Apple" , "Orange" , 5 ,345.06 ,False , "Aakash ", "Rohan"]
print(friends)

# 1) Append() Method :-

friends.append("Madhav")  
print(friends)

# 2)  Sort Method :- 
l1 = [1,34,62,2,6,11]
l1.sort()
print(l1)


# 3) Reverse Method :- 
l1 = [1,34,62,2,6,11]
l1.reverse()
print(l1)


# 4) Insert Method :- 
l1 = [1,34,62,2,6,11]
l1.insert(3,33333)  # Insert 33333 such that its index in the list is 3
print(l1)

# 5) Pop Method :-
l1 = [1,34,62,2,6,11]
value = l1.pop(2) 
print(value)

# 6) Remove Method :-
l1 = [1,34,62,2,6,11]
value = l1.remove(2) 
print(value)
print(l1)

# 7) extend() :- Adds all elements of an iterable to the end of the list.

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)  # Output: [1, 2, 3, 4, 5, 6]


# 8) clear() :- Description: Removes all elements from the list.

fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)  # Output: []

# 9) index() :- Returns the index of the first occurrence of a specified value.

fruits = ["apple", "banana", "cherry"]
index = fruits.index("banana")
print(index)  # Output: 1


# 10) count() :- Returns the number of occurrences of a specified value.

numbers = [1, 2, 2, 3, 4, 2]
count = numbers.count(2)
print(count)  # Output: 3


# 11) copy() :- Returns a shallow copy of the list.

fruits = ["apple", "banana", "cherry"]
fruits_copy = fruits.copy()
print(fruits_copy)  # Output: ['apple', 'banana', 'cherry']

# 12) len() :- Returns the number of items in a list.

fruits = ["apple", "banana", "cherry"]
length = len(fruits)
print(length)  # Output: 3

# 13) max() :- Returns the largest item in a list.

numbers = [1, 2, 3, 4, 5]
maximum = max(numbers)
print(maximum)  # Output: 5

# 14) min() :- Returns the smallest item in a list.

numbers = [1, 2, 3, 4, 5]
minimum = min(numbers)
print(minimum)  # Output: 1

# 15) sum() :- Returns the sum of all items in a list.

numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(total)  # Output: 15

# 16) enumerate() :-Description: Returns an enumerate object. It contains the index and value for each item.

fruits = ["apple", "banana", "cherry"]
for index, value in enumerate(fruits):
    print(index, value)
# Output:
# 0 apple
# 1 banana
# 2 cherry


# 17) any() :-  Returns True if any element of the iterable is True. If the iterable is empty, returns False.

numbers = [0, 1, 2, 3]
result = any(numbers)
print(result)  # Output: True


# 18) all() :- Returns True if all elements of the iterable are True. If the iterable is empty, returns True.

numbers = [1, 2, 3, 4]
result = all(numbers)
print(result)  # Output: True


# 19) zip() :- Returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator is paired together, and so on.

list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
zipped = zip(list1, list2)
print(list(zipped))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]




# Tuples :-  
# A Tuple is collection of immutable heterogeneous python objects

# Creating an empty Tuples
emp = ()
print(type(emp))


a = (1,)
print(type(a))


a = (1, 45,345 ,3424 , False, "Rohan " ,"Shivam")
print(a)


# Slicing :- Return new Tuple
my_tuple = ("Madhav" , "Jyothi More" , "Sachin" , "Jyothi Patel")
print(my_tuple)
print(my_tuple[:2])
print(my_tuple[0:3])
print(my_tuple[0:])


# Negative Indexing / slicing :- Negative indexing and slicing work with tuples in the same way they do with lists. Here's a guide on how to use these techniques with tuples:

fruits = ("apple", "banana", "cherry", "date", "fig")

# Access the last element
print(fruits[-1])  # Output: fig

# Access the second-to-last element
print(fruits[-2])  # Output: date

# Access the third-to-last element
print(fruits[-3])  # Output: cherry


# Slicing with Negative Indices :-  You can also use negative indices with slicing to access a range of elements from the end of the tuple:

fruits = ("apple", "banana", "cherry", "date", "fig")

# Slice the last three elements
print(fruits[-3:])  # Output: ('cherry', 'date', 'fig')

# Slice all elements except the last two
print(fruits[:-2])  # Output: ('apple', 'banana', 'cherry')

# Slice the second-to-last to the last element
print(fruits[-2:])  # Output: ('date', 'fig')
print()


# Using the :: Syntax for Slicing :-  The slicing syntax in Python uses the start:stop:step format, and you can use negative steps to reverse the tuple or sequence :- 

# Original tuple
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Slice the tuple with a positive step
print(numbers[1:8:2])  # Output: (2, 4, 6, 8)

# Slice the tuple with a negative step (reversing the tuple)
print(numbers[::-1])  # Output: (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)

# Slice the tuple with a negative step from end to start

print(numbers[8:3:-1])  # Output: (9, 8, 7, 6, 5)
print()

# Slicing Breakdown:-

'''
Slice: numbers[8:3:-1]

Step 1: Start at index 8
Element at index 8: 9

Step 2: Move to the next element to the left (since step is -1)
Element at index 7: 8

Step 3: Continue moving left by one element each time
Element at index 6: 7
Element at index 5: 6
Element at index 4: 5

Step 4: Stop when you reach the element just before index 3
Element at index 3: 4 (this is not included) 

'''
print()

# Extracting Every Second Element :- Using slicing to extract every second element:

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
every_second = numbers[::2]
print(every_second)  # Output: (1, 3, 5, 7, 9)

# Tuple Methods :- 

# Count() Method :-

a = (1,45,345 ,3424 , False, 45,"Rohan " ,"Shivam")
no = a.count(45)
print(no)

# Index() Method :- 

i = a.index(345)
print(i)

# That’s all! Tuples don’t support mutating methods (like append, extend, or remove) because they are immutable. However, you can still use general functions like len(), min(), max(), etc., with tuples since they are sequence types.

# Length() Method :-

tuple = 1 , 3 , 4
print(tuple)
print("Length is :- ",len(tuple))
print()

# Max() Method :-
print("Max element is ",max(tuple))

# Min() Method :-
print("Min element is ",min(tuple))


# Unpacking :- Tuples can be unpacked into individual variables .

my_tuple = (1,2,3)
a , b , c = my_tuple
print(a , b ,c)