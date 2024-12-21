# An array is an object that stores a group of elements (or values) of same data type. The main advantage of array is to store and process a group of elements easily.

# Key Points :- 1) Arrays can store only one type of data.
#               2) Arrays can increase or decrease their size dynamically.


# Advantages of Arrays :- 
''' 1) Arrays are similar to lists. The main difference is that arrays can store only one type
of elements; whereas, lists can store different types of elements. When dealing with a
huge number of elements, arrays use less memory than lists and they offer faster
execution than lists.'''

''' 2) The size of the array is not fixed in Python. Hence, we need not specify how many
elements we are going to store into an array in the beginning.'''


''' 3) Arrays can grow or shrink in memory dynamically (during runtime).'''


''' 4) Arrays are useful to handle a collection of elements like a group of numbers or
characters.'''

''' 5) Methods that are useful to process the elements of any array are available in 'array'
module '''

# Creating an Array :- Arrays can hold data of same type. The type should be specified by using a type code at the time of creating the array object as: - 

# Syntax :- arrayname = array(type code, [elements])

# Example :- a = array('i', [4, 6, 2, 9])

'''
The type code 'i', represents integer type array where we can store integer numbers. If
the type code is 'f' then it represents float type array where we can store numbers with
decimal point. Refer :- Python_Type_codes .png for more insights about this . 

'''


#  Import the Array Module of Python :- There are three ways to import the array module into our program. The first way is to import the entire array module using import statement as,
# I) :- 
#  1)  import array 

# When we import the array module, we are able to get the 'array' class of that module that helps us to create an array.
#  2) Examples: a = array.array('i',[4,6,2,9])

# Here, the first 'array' represents the module name and the next 'array' represents the class name for which the object is created.

# II) :- 
# The second way of importing the array module is to give it an alias name, as:
# 2) import array as ar
# Example: a = ar.array('i', [4,6,2,9])

# III) :- 
# The third way of importing the array module is to write:
# 3) from array import *

# Observe the '*' symbol that represents 'all'. The meaning of this statement is this:
'''
import all (classes, objects, variables etc) from the array module into our program.
• That means we are specifically importing the 'array' class (because of * symbol) of
'array' module. So, there is no need to mention the module name before our array
name while creating it. We can create the array as:
a =array('i',[4,6,2,9])

'''

# An index represents the position number of an element in an array.
# Examples: x = array('i', [10, 20, 30, 40, 50])

# To find out the number of elements in an array we can use the len() function as:
# Example :-  n = len(x)
# • The len(x) function returns the number of elements in the array 'x' into 'n'.


# Slicing :-  
'''

1) A slice represents a piece of the array. When we perform 'slicing' operations
on any array, we can retrieve a piece of the array that contains a group of
elements. Whereas indexing is useful to retrieve element by element from the array,
slicing is useful to retrieve a range of elements.

2) Python supports the slicing of arrays. It is the creation of a new sub-array from the
given array on the basis of the user-defined starting and ending indices.

3) The general format of a slice is:- 

 Syntax :- arrayname[start:stop:stride]

 
4)  We can eliminate any one or any two in the items: 'start', 'stop' or 'stride' from the
above syntax.

5) Again, Python also provides a function named slice() which returns a slice object
containing the indices to be sliced.

# The syntax for using this method is given below.
# slice(start, stop[, step])

i) Start is the starting index from which we need to slice the array arr. By
default set to 0.

ii) stop is the ending index, before which the slicing operation would end. By
default equal to the length of the array.

iii) step is the steps the slicing process would take from start to stop. By default
set to 1.

1) With one parameter :- 
>> Default values for start, stop and step are equal to 0, length of the array, and 1
respectively. Hence, specifying either one of the start or stop, we can slice an
array.

2) Array Slicing in Python with two parameters 
>> Example :- 
import array
array_arr= array. array('i',[1,2,3,4,5])
print("Sliced array: ", array_arr[2:5])

3) With the step parameter
>> Example :- 
import array
array_arr= array.array('i',[1,2,3,4,5,6,7,8,9,10])
print("Sliced array: ", array_arr[1:8])
print("Sliced array: ", array_arr[1:8:2])


'''


from array import * 
# Array Methods :- 

# 1) append(x) :- Adds an element x to the end of the list.
arr = array('d' , [10.9, 55.5 , 77.7 , 45.67 , 99.98 , 100.14])
arr.append(120.98)
print(arr)           # output :- array('d', [10.9, 55.5, 77.7, 45.67, 99.98, 100.14, 120.98])   
print(arr.tolist())  # output :- [10.9, 55.5, 77.7, 45.67, 99.98, 100.14, 120.98]

# 2) buffer_info() :- Returns a tuple containing the memory address and the length of the array. The buffer_info() method returns useful information about the memory management of the array in the form of a tuple
arr = array('i' , [1,2,3])
info = arr.buffer_info()
print(info) # Output: (memory_address, 3) - memory_address will vary

# 3) byteswap() :- The byteswap() method in the Python array module is used to swap the byte order of each element in the array. This is especially useful when dealing with binary data from different systems with different endianness (the order in which bytes are stored).
arr = array('h', [1, 256, 512])
arr.byteswap()
print(arr)  # Output: array('h', [256, 1, 2048])


''' 
Explanation of Correct Output:- 

Original Element 1 (0x0001): Bytes swapped to 0x0100 = 256

Original Element 256 (0x0100): Bytes swapped to 0x0001 = 1

Original Element 512 (0x0200): Bytes swapped to 0x0002 = 2

'''

# 4) count(x) :- Returns the number of occurrences of x in the array
arr = array('i', [1, 2, 2, 3])
count = arr.count(2)
print(count)  # Output: 2

# 5) extend(iterable) :- Extends the array by appending elements from the iterable.
arr = array('i', [1, 2, 3])
arr.extend([4, 5, 6])
print(arr)  # Output: array('i', [1, 2, 3, 4, 5, 6])

# 6) frombytes(b) :- Appends items from the string buffer b.
arr = array('i', [1, 2, 3])
arr.frombytes(b'\x04\x00\x00\x00\x05\x00\x00\x00')
print(arr)  # Output: array('i', [1, 2, 3, 4, 5])

# 7). fromfile(f, n) :- Reads n items from the file object f and appends them to the array. Write the array to a file first
arr = array('i', [1, 2, 3])
with open('array_data.bin', 'wb') as f:
    arr.tofile(f)

# Read the array from the file
arr2 = array('i')
with open('array_data.bin', 'rb') as f:
    arr2.fromfile(f, 3)
print(arr2)  # Output: array('i', [1, 2, 3])

# 8). fromlist(lst) :- Appends items from the list lst
arr = array('i', [1, 2, 3])
arr.fromlist([4, 5, 6])
print(arr)  # Output: array('i', [1, 2, 3, 4, 5, 6])

# 9) fromstring(s) :- (This method is deprecated in Python 3, use frombytes instead)

# 10) fromunicode(u) :- Extends the array with data from the unicode string u.
arr = array('u', 'hello')
arr.fromunicode('world')
print(arr)  # Output: array('u', 'helloworld')
print()


# 11) index(x) :- Returns the index of the first occurrence of x.
arr = array('i', [1, 2, 3, 2])
index = arr.index(2)
print(index)  # Output: 1
print()


# 12) insert(i, x) :- Inserts a new item x into the array before position i.
arr = array('i' , [1,2,3,4,5])
arr.insert(3 , 100)
print("Insert :- ",arr) # Output :- Insert :-  array('i', [1, 2, 3, 100, 4, 5])
print()


# 13) pop([i]) :- Removes and returns the item at position i (or the last item if i is not specified).
arr = array('i', [1, 2, 3])
popped_element = arr.pop(1)
print(arr)  # Output: array('i', [1, 3])
print(popped_element)  # Output: 2

# 14) remove(x) :- Removes the first occurrence of x from the array.
arr = array('i', [1, 2, 3, 2])
arr.remove(2)
print(arr)  # Output: array('i', [1, 3, 2])
print()


# 15) reverse() :- Reverses the elements of the array in place.
arr = array('i', [1, 2, 3])
arr.reverse()
print(arr)  # Output: array('i', [3, 2, 1])
print()


# 16) tobytes() :- Converts the array to a bytes object.
arr = array('i', [1, 2, 3])
b = arr.tobytes()
print(b)  # Output: b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00'


# 17) tofile(f) :- Writes the array to a file.
arr = array('i', [1, 2, 3])
with open('array_data.bin', 'wb') as f:
    arr.tofile(f)
# No direct output, but the array is written to 'array_data.bin'


# 18) tolist() :- Converts the array to a list.
arr = array('i', [1, 2, 3])
lst = arr.tolist()
print(lst)  # Output: [1, 2, 3]

# 19) tounicode() :- Converts the array to a unicode string.
arr = array('u', 'hello')   # DeprecationWarning: The 'u' type code is deprecated and will be removed in Python 3.16
u = arr.tounicode()
print(u)  # Output: 'hello'




# Write a Python program to demonstrate indexing and Slicing of an array ? 
from array import * 
x = array('i' , [10 , 20 , 30, 40 , 50])
n = len(x) 
print("Length of array : - ", n)
print("Last element of the array is  : - ", x[-1])

# Displaying Array elements Using indexing 
for i in range(n):
    print (x[i] ,end= ' ') 


# Use of Slicing 
y = x[1:4]
print(y)
print()
y = x[0:1]
print(y)
print()
y = x[-3:]
print(y)
print()
y = x[-4:-1]
print(y)
print()
y = x[:3]
print(y)



# Write a Python Program to perform Searching and Sorting ? 
from array import *
arr = array('i' , [ ])

size = int(input("Enter the size of the array : - "))

for i in range(size) :
    print("Array Value := ", i)
    arr.append(int(input()))

flag=False

for i in range(size - 1):
    for j in range(size - i - 1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            flag = True
        if flag==False:
            break
        else:
            flag=False
print("Sorted array : ", arr)


s=int(input("Enter the element to be searched :- "))
temp=False
for i in range(len(arr)):
    if s==arr[i]:
        print("found the position" , i)
        temp=True
        break
if temp==False:
        print("\n not found in the array ")
            
