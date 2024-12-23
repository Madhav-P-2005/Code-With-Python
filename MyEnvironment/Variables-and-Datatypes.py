'''Python has 7 major categories of data types, including: Text, Numeric, Sequence, Mapping, Set, Boolean, and Binary types.
Within these categories, there are specific types like str, int, list, dict, etc.
The NoneType category is often considered separately since it represents the absence of value.
'''
# Major Categories and Types :-
# 1) Text Type :	str
# 2) Numeric Types :	int, float, complex
# 3) Sequence Types :	list, tuple, range
# 4) Mapping Type :	dict
# 5) Set Types :	set, frozenset
# 6) Boolean Type :	bool
# 7) Binary Types :	bytes, bytearray, memoryview
# 8) None Typev :	NoneType 

# 1. Text Type
# str: Used to represent text data.

text = "Hello, World!"
print(text)  # Output: Hello, World!

# 2. Numeric Types
# int: Represents integer numbers.

integer_number = 42
print(integer_number)  # Output: 42

# float: Represents floating-point numbers.

floating_number = 3.14
print(floating_number)  # Output: 3.14
# complex: Represents complex numbers.

complex_number = 1 + 2j
print(complex_number)  # Output: (1+2j)


# 3. Sequence Types
# list: Ordered, mutable collection of items.

fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# tuple: Ordered, immutable collection of items.

coordinates = (10, 20)
print(coordinates)  # Output: (10, 20)


'''

range: Represents a sequence of numbers. The range() function can take a maximum of three arguments:
syntax :- range(start, stop, step) . 
The start and step parameters in range() are optional.

'''

number_range = range(1, 5)
print(list(number_range))  # Output: [1, 2, 3, 4]



# 4. Mapping Type
# dict: Unordered collection of key-value pairs.

person = {"name": "Alice", "age": 30}
print(person)  # Output: {'name': 'Alice', 'age': 30}


# 5. Set Types
# set: Unordered collection of unique items.

unique_numbers = {1, 2, 3, 4}
print(unique_numbers)  # Output: {1, 2, 3, 4}

# frozenset: Immutable version of a set.
frozen_set = frozenset([1, 2, 3, 4])
print(frozen_set)  # Output: frozenset({1, 2, 3, 4})

# 6. Boolean Type
# bool: Represents Boolean values (True or False).

is_valid = True
print(is_valid)  # Output: True


# 7. Binary Types
# bytes: Represents binary data.

byte_data = b"hello"
print(byte_data)  # Output: b'hello'

# bytearray: Mutable version of bytes.

mutable_byte_data = bytearray(b"hello")
mutable_byte_data[0] = ord('H')
print(mutable_byte_data)  # Output: bytearray(b'Hello')

# memoryview: Allows read and write access to the internal data of an object that supports the buffer protocol.

byte_data = b"hello"
memory_view = memoryview(byte_data)
print(memory_view[1])  # Output: 101 (ASCII value of 'e')

# 8. None Type
# NoneType: Represents the absence of a value.

nothing = None
print(nothing)  # Output: None




