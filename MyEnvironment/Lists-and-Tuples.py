'''

>>> List is a collection of data . It can hold values of multiple data types . They are mutable(can be modified) in nature 


'''

# here 1 'st positon is 0 and last element = last number - 1

friends = ["Apple" , "Orange" , 5 ,345.06 ,False , "Aakash ", "Rohan"]

print(friends[0])           # Output :-  Apple

friends[0] = "Grapes"  # Unlike Strings Lists are Mutable . 

print(friends[0])           # Output :-  Grapes

print(friends)              # Output :-  ['Grapes', 'Orange', 5, 345.06, False, 'Aakash ', 'Rohan']

print()



# Creating List of Lists
marks = [["Harry" , 100 ],["Raghav" , 95],["Kiran" , 99 ]]

print("List of lists is :- ",marks)                # Output :-  List of lists is :-  [['Harry', 100], ['Raghav', 95], ['Kiran', 99]]

print()


# Slicing :-

print(friends[:4])        # Output :-   ['Apple', 'Orange', 5, 345.06]

print(friends[0:])        # Output :-   ['Apple', 'Orange', 5, 345.06, False, 'Aakash ', 'Rohan']

print(friends[1:4])       # Output :-   ['Orange', 5, 345.06]

print()



# Negative Slicing :- 

fruits = ["apple", "banana", "cherry", "date", "fig"]

# Access the last element

print(fruits[-1])             # Output :-  fig

# Access the second-to-last element

print(fruits[-2])             # Output :-  date

# Access the third-to-last element

print(fruits[-3])             # Output :-  cherry

print()



# Slice the last three elements

print(fruits[-3:])           # Output :-  ['cherry', 'date', 'fig']


# Slice all elements except the last two

print(fruits[:-2])           # Output :-  ['apple', 'banana', 'cherry']


# Slice the second-to-last to the last element
print(fruits[-2:])           # Output :-  ['date', 'fig']


'''

>>>  Using the :: Syntax for Slicing :- The slicing syntax in Python uses the start:stop:step format, and you can use negative steps to reverse the list or sequence :-

'''


# Original list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Slice the list with a positive step

print(numbers[1:8:2])       # Output :-  [2, 4, 6, 8]


# Slice the list with a negative step (reversing the list)

print(numbers[::-1])        # Output :-  [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


# Slice the list with a negative step from end to start

print(numbers[8:3:-1])      # Output :-  [9, 8, 7, 6, 5]


'''

Practical Examples
Reverse a List

'''

# Using the slicing syntax [::-1] to reverse a list :-

fruits = ["apple", "banana", "cherry", "date", "fig"]

reversed_fruits = fruits[::-1]

print(reversed_fruits)       # Output :-  ['fig', 'date', 'cherry', 'banana', 'apple']

# Extracting Every Second Element :-   Using slicing to extract every second element :-

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

every_second = numbers[::2]

print(every_second)         # Output :-  [1, 3, 5, 7, 9]

print()



# List Methods 
friends = ["Apple" , "Orange" , 5 ,345.06 ,False , "Aakash ", "Rohan"]

print(friends)             # Output :-   ['Apple', 'Orange', 5, 345.06, False, 'Aakash ', 'Rohan']


# 1) Append() Method :-

friends.append("Madhav")  

print(friends)             # Output :-  ['Apple', 'Orange', 5, 345.06, False, 'Aakash ', 'Rohan', 'Madhav']


# 2)  Sort Method :- 

l1 = [1,34,62,2,6,11]

l1.sort()

print(l1)                 # Output :-  [1, 2, 6, 11, 34, 62]


# 3) Reverse Method :- 

l1 = [1,34,62,2,6,11]

l1.reverse()

print(l1)                  # Output :-   [11, 6, 2, 62, 34, 1]


# 4) Insert Method :- 

l1 = [1,34,62,2,6,11]

l1.insert(3,33333)  # Insert 33333 such that its index in the list is 3

print(l1)                 # Output :-  [1, 34, 62, 33333, 2, 6, 11]


# 5) Pop Method :-

l1 = [1,34,62,2,6,11]

value = l1.pop(2) 

print(value)               # Output :-  62


# 6) Remove Method :-

l1 = [1, 34, 62, 2, 6, 11]

value = l1.remove(2)    # Removes '2' from the list, but does NOT return it

print(value)              # Output :-   None

print(l1)                 # Output :-  [1, 34, 62, 6, 11]



# 7) extend() :- Adds all elements of an iterable to the end of the list.

list1 = [1, 2, 3]

list2 = [4, 5, 6]

list1.extend(list2)

print(list1)                # Output :-  [1, 2, 3, 4, 5, 6]



# 8) clear() :-  Description -->  Removes all elements from the list.

fruits = ["apple", "banana", "cherry"]

fruits.clear()

print(fruits)              # Output :-  []



# 9) index() :-  Returns the index of the first occurrence of a specified value.

fruits = ["apple", "banana", "cherry"]

index = fruits.index("banana")

print(index)              # Output :-  1



# 10) count() :- Returns the number of occurrences of a specified value.

numbers = [1, 2, 2, 3, 4, 2]

count = numbers.count(2)

print(count)              # Output :-  3



# 11) copy() :-  Returns a shallow copy of the list.

fruits = ["apple", "banana", "cherry"]

fruits_copy = fruits.copy()

print(fruits_copy)        # Output :-  ['apple', 'banana', 'cherry']



# 12) len() :-   Returns the number of items in a list.

fruits = ["apple", "banana", "cherry"]

length = len(fruits)

print(length)             # Output :-  3



# 13) max() :-  Returns the largest item in a list.

numbers = [1, 2, 3, 4, 5]

maximum = max(numbers)

print(maximum)            # Output :-  5



# 14) min() :-  Returns the smallest item in a list.

numbers = [1, 2, 3, 4, 5]

minimum = min(numbers)

print(minimum)            # Output :-  1



# 15) sum() :- Returns the sum of all items in a list.

numbers = [1, 2, 3, 4, 5]

total = sum(numbers)

print(total)              # Output :-  15



# 16) enumerate() :-   Description  -->  Returns an enumerate object. It contains the index and value for each item.

fruits = ["apple", "banana", "cherry"]

for index, value in enumerate(fruits):

    print(index, value)

'''

Output :- 

0 apple
1 banana
2 cherry

'''


# 17) any() :-  Returns True if any element of the iterable is True. If the iterable is empty, returns False.

numbers = [0, 1, 2, 3]

result = any(numbers)

print(result)             # Output :-  True



# 18) all() :-   Returns True if all elements of the iterable are True. If the iterable is empty, returns True.

numbers = [1, 2, 3, 4]

result = all(numbers)

print(result)             # Output :-  True



# 19) zip() :- Returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator is paired together, and so on.

list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
zipped = zip(list1, list2)
print(list(zipped))       # Output :-  [(1, 'a'), (2, 'b'), (3, 'c')]




'''

1)  Write a python program to read 10 elements in the list and print them one
by one.

a) Print the list in last in first out mode
b) Find how many elements are positive and how many are negative
c) Search for a specific element in the list
d) Sort the elements in the list
e) Find the largest and smallest elements in the list
f) Find the sum of all positive elements leaving zero’s
g) Find how many positive numbers are there in the first half of the
list and in second half of the list.

'''


# a) Print the list in last in first out mode :- 
lst=[]
print("Enter the size of the list :-  ")
n=int(input())
for i in range(n):
    value=int(input(f"Enter the element {i} :- "))
    lst.append(value)
for i in range(1,n+1):
    print(lst[-i] , end=' ')
print()


'''

Output :- 

Enter the size of the list :-  
5
Enter the element 0 :- 
1
Enter the element 1 :- 
2
Enter the element 2 :- 
3
Enter the element 3 :- 
4
Enter the element 4 :- 
5

5 4 3 2 1

'''



# b) Find how many elements (counts) are positive and how many are negative
lst=[]
print("Enter the size of the list :-  ")
n=int(input())
for i in range(n):
    value=int(input(f"Enter the element {i} :- "))
    lst.append(value)

count_positive=0
count_negative=0
for j in lst:
    if j>0:
        count_positive+=1
    else:
        count_negative+=1

print(f"No of Positive Numbers in list are :- ",count_positive)
print(f"No of Negative Numbers in list are :- ",count_negative)


'''

Output :- 

Enter the size of the list :-  
5
Enter the element 0 :- 
100
Enter the element 1 :- 
5654
Enter the element 2 :- 
-67
Enter the element 3 :- 
-30
Enter the element 4 :- 
-0

No of Positive Numbers in list are :-  2
No of Negative Numbers in list are :-  3

'''



# c) Search for a specific element in the list
lst=[]
print("Enter the size of the list :-  ")
n=int(input())
for i in range(n):
    value=int(input(f"Enter the element {i} :- "))
    lst.append(value)

flag=False
key=int(input("Enter the element you want to search :-  "))
for i in range(n):
    if key==lst[i]:
        print(f"{key} is present in location {i}")
        flag=True

if flag==False:
    print(f"{key} Not Found ! in the list ")


'''

Output :- 

Enter the size of the list :-  
5
Enter the element 0 :- 100
Enter the element 1 :- 23
Enter the element 2 :- 0
Enter the element 3 :- 1
Enter the element 4 :- -100

Enter the element you want to search :-  1

1 is present in location 3



'''



# d)  Sort the elements in the list
# 1) Ascending Order :- 
lst=[]
print("Enter the size of the list :-  ")
n=int(input())
for i in range(n):
    value=int(input(f"Enter the element {i} :- "))
    lst.append(value)

print("Elements before Sorting :-  \n")
for i in range(n):
    print(lst[i])

flag=False
print("Elements after Sorting :- \n")
for i in range(n-1):
    for j in range(n-i-1):
        if lst[j] > lst[j+1]:
            flag=True
            temp = lst[j]
            lst[j] = lst[j+1]
            lst[j+1] = temp
    
if flag==False:
    print("It is in descending order ")
else:
   print(f"Sorted Elements are (ascending order: small to big): {lst}")

print()


'''

Output :- 

Enter the size of the list :-  
5
Enter the element 0 :- 12
Enter the element 1 :- 100
Enter the element 2 :- 99
Enter the element 3 :- 45
Enter the element 4 :- 66
Elements before Sorting :-  

12
100
99
45
66
Elements after Sorting :- 

Sorted Elements are (ascending order: small to big): [12, 45, 66, 99, 100]


'''




# 2) Descending Order :- 
lst=[]
print("Enter the size of the list :-  ")
n=int(input())
for i in range(n):
    value=int(input(f"Enter the element {i} :- "))
    lst.append(value)

print("Elements before Sorting :-  \n")
for i in range(n):
    print(lst[i])

flag=False
print("Elements after Sorting :- \n")
for i in range(n-1):
    for j in range(n-i-1):
        if lst[j] < lst[j+1]:
            flag=True
            temp = lst[j]
            lst[j] = lst[j+1]
            lst[j+1] = temp
    
if flag==False:
    print("It is in descending order ")
else:
   print(f"Sorted Elements are (ascending order: big to small): {lst}")


'''

Output :- 

Enter the size of the list :-  
5
Enter the element 0 :- 12
Enter the element 1 :- 1
Enter the element 2 :- 100
Enter the element 3 :- 99
Enter the element 4 :- -67
Elements before Sorting :-  

12
1
100
99
-67
Elements after Sorting :- 

Sorted Elements are (ascending order: small to big): [100, 99, 12, 1, -67]


'''



# e) Find the largest and smallest elements in the list
lst=[]
print("Enter the size of the list :-  ")
n=int(input())
for i in range(n):
    value=int(input(f"Enter the element {i} :- "))
    lst.append(value)


print("Displaying the elements in the list :- ")
for i in range(n):
    print(lst[i])

large=lst[0]
for j in range(n):
    if large < lst[j]:
        large=lst[j]


print(f"Largest element in the list is ",large)

small=lst[0]
for j in range(n):
    if small > lst[j]:
        small=lst[j]

print(f"Smallest element in the list is ",small)


'''

Output :- 

Enter the size of the list :-  
5
Enter the element 0 :- 12
Enter the element 1 :- 33
Enter the element 2 :- 44
Enter the element 3 :- 5
Enter the element 4 :- 2

Displaying the elements in the list :- 
12
33
44
5
2

Largest element in the list is  44
Smallest element in the list is  2

'''


# or (simple way) :- 


lst=[]
print("Enter the size of the list :-  ")
n=int(input())
for i in range(n):
    value=int(input(f"Enter the element {i} :- "))
    lst.append(value)


print("Displaying the elements in the list :- ")
for i in range(n):
    print(lst[i])

large = max(lst)
small = min(lst)
print(f"Largest element in the list is ",large)
print(f"Smallest element in the list is ",small)



'''

Output :- 

Enter the size of the list :-  
5
Enter the element 0 :- 1
Enter the element 1 :- 100
Enter the element 2 :- -67
Enter the element 3 :- 3
Enter the element 4 :- 1
Displaying the elements in the list :- 
1
100
-67
3
1
Largest element in the list is  100
Smallest element in the list is  -67


'''


# f) Find the sum of all positive elements leaving zero’s
lst=[]
print("Enter the size of the list :-  ")
n=int(input())
for i in range(n):
    value=int(input(f"Enter the element {i} :- "))
    lst.append(value)


print("Displaying the elements in the list :- ")
for i in range(n):
    print(lst[i])

sum=0
flag=False
for j in lst:
    if j > 0:
        flag=True
        sum = sum+j
    else:
        continue

if flag==True:
    print(f"Sum of Positive elements in the list :- ",sum)


'''

Output :- 

Enter the size of the list :-  
5
Enter the element 0 :- 100
Enter the element 1 :- 9
Enter the element 2 :- 45
Enter the element 3 :- -27
Enter the element 4 :- 0
Displaying the elements in the list :- 
100
9
45
-27
0
Sum of Positive elements in the list :-  154

'''



# g) Positive numbers in first half and second half of the list 
List  = []
n = int(input("enter the size :- "))

for i in range(n):
    value = int(input(f"Enter value {i + 1} : "))
    List.append(value)

mid_point = len(List)//2
first_half = List[:mid_point]
second_half = List[mid_point:]
positive_in_firsthalf = sum(1 for num in first_half if num > 0)
positive_in_secondhalf = sum(1 for num in second_half if num > 0)

print(f"Number of positive numbers in first Half " , positive_in_firsthalf)
print(f"Number of positive numbers in second Half " , positive_in_secondhalf)


'''

Output :- 

enter the size :- 5
Enter value 1 : 12
Enter value 2 : -89
Enter value 3 : 100
Enter value 4 : 1
Enter value 5 : 0

Number of positive numbers in first Half  1
Number of positive numbers in second Half  2


'''



# Tuples :-  A Tuple is collection of immutable heterogeneous python objects

# Creating an empty Tuples
emp = ()
print(type(emp))           # Output :-  <class 'tuple'>


a = (1,)
print(type(a))             # Output :-  <class 'tuple'>


a = (1, 45,345 ,3424 , False, "Rohan " ,"Shivam")

print(a)                   # Output :-  (1, 45, 345, 3424, False, 'Rohan ', 'Shivam')


# Slicing :- Return new Tuple
my_tuple = ("Madhav" , "Jyothi More" , "Sachin" , "Jyothi Patel")

print(my_tuple)            # Output :-  ('Madhav', 'Jyothi More', 'Sachin', 'Jyothi Patel')

print(my_tuple[:2])        # Output :-  ('Madhav', 'Jyothi More')

print(my_tuple[0:3])       # Output :-  ('Madhav', 'Jyothi More', 'Sachin')

print(my_tuple[0:])        # Output :-  ('Madhav', 'Jyothi More', 'Sachin', 'Jyothi Patel')



'''

>>>  Negative Indexing / slicing :- Negative indexing and slicing work with tuples in the same way they do with lists. Here's a guide on how to use these techniques with tuples :- 

'''


fruits = ("apple", "banana", "cherry", "date", "fig")

# Access the last element

print(fruits[-1])               # Output :-  fig

# Access the second-to-last element

print(fruits[-2])               # Output :-  date

# Access the third-to-last element

print(fruits[-3])               # Output :-  cherry


# Slicing with Negative Indices :-  You can also use negative indices with slicing to access a range of elements from the end of the tuple:

fruits = ("apple", "banana", "cherry", "date", "fig")

# Slice the last three elements

print(fruits[-3:])              # Output :-  ('cherry', 'date', 'fig')


# Slice all elements except the last two

print(fruits[:-2])              # Output :-  ('apple', 'banana', 'cherry')


# Slice the second-to-last to the last element
print(fruits[-2:])             # Output :-  ('date', 'fig')

print()



'''

>>>  Using the :: Syntax for Slicing :-  The slicing syntax in Python uses the start:stop:step format, and you can use negative steps to reverse the tuple or sequence :- 

'''

# Original tuple
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


# Slice the tuple with a positive step

print(numbers[1:8:2])         # Output :-  (2, 4, 6, 8)


# Slice the tuple with a negative step (reversing the tuple)

print(numbers[::-1])          # Output :-  (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)


# Slice the tuple with a negative step from end to start

print(numbers[8:3:-1])        # Output :-  (9, 8, 7, 6, 5)
print()




# Slicing Breakdown:-

'''
Slice :  numbers[8:3:-1]

Step 1 :  Start at index 8
Element at index 8: 9

Step 2 :  Move to the next element to the left (since step is -1)
Element at index 7: 8

Step 3 :  Continue moving left by one element each time
Element at index 6: 7
Element at index 5: 6
Element at index 4: 5

Step 4 :  Stop when you reach the element just before index 3
Element at index 3: 4 (this is not included) 

'''
print()

# Extracting Every Second Element :- Using slicing to extract every second element:

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

every_second = numbers[::2]

print(every_second)         # Output :-  (1, 3, 5, 7, 9)

# Tuple Methods :- 

# 1) Count() Method :-

a = (1,45,345 ,3424 , False, 45,"Rohan " ,"Shivam")

no = a.count(45)           

print(no)                  # Output :- 2

# 2) Index() Method :- 

i = a.index(345)

print(i)                   # Output :- 2


'''

>>>  That’s all! Tuples don’t support mutating methods (like append, extend, or remove) because they are immutable. However, you can still use general functions like len(), min(), max(), etc., with tuples since they are sequence types.

'''

# Length() Method :-

tuple = 1 , 3 , 4

print(tuple)                # Output :-  (1, 3, 4)

print("Length is :- ",len(tuple))       # Output :-  Length is :-  3
 
print()


# Max() Method :-
print("Max element is ",max(tuple))     # Output :-  Max element is  4


# Min() Method :-
print("Min element is ",min(tuple))     # Output :-  Max element is  1


# Unpacking :- Tuples can be unpacked into individual variables .

my_tuple = (1,2,3)

a , b , c = my_tuple

print(a , b ,c)             # Output :-  1 2 3