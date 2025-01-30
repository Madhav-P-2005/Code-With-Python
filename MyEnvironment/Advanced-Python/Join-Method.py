# Release Info :- 

'''

The join() method was introduced in Python 1.6, released in September 2000, as part of the string class enhancements.

'''




# Definition 

'''
>> The join() method in Python is a string method used to concatenate the elements of an iterable (like a list, tuple, or set) into a single string, with a specified separator placed between each element. Join() method works for only list 

'''



# Syntax :-    separator.join(iterable)




# How Does It Work ? 

'''

  1) The join() method takes an iterable as its argument.

  2) Each element in the iterable is joined together into a single string.

  3) The specified separator is placed between consecutive elements during concatenation.

  4) The result is returned as a new string.

'''



# Example 1 :- Joining a List of Strings:

List = ["Marathas", "chhatrapati shivaji maharaj" , "Saibai Bhonsale "]

Result =  "-".join(List)


print(Result)             # Output :- Marathas-chhatrapati shivaji maharaj-Saibai Bhonsale


Result = "::".join(List)     


print(Result)            # Output :-  Marathas::chhatrapati shivaji maharaj::Saibai Bhonsale 





# Example 2 :- Joining a Tuple of Strings:

Tuple = ["Marathas", "chhatrapati shivaji maharaj" , "Saibai Bhonsale "]

Result = ",".join(Tuple)    

print(Result)            # Output :-   Marathas,chhatrapati shivaji maharaj,Saibai Bhonsale





# Example 3 :-  Using an Empty Separator

chars = ["H", "e", "l", "l", "o"]
result = "".join(chars)


print(result)           # Output: Hello




# Example 4  :-   Joining Characters in a String:

word = "WORLD"
result = ".".join(word)


print(result)          # Output: W.O.R.L.D




# Common Use Cases :- 
# 1) Creating CSV Strings :- 

fields = ["Name", "Age", "Location"]
csv = ",".join(fields)


print(csv)             # Output: Name,Age,Location



# 2) Building File Paths :- 

path_parts = ["home", "user", "documents", "file.txt"]
path = "/".join(path_parts)


print(path)            # Output: home/user/documents/file.txt



# 3) Flattening Nested Data :- 

nested = [["a", "b"], ["c", "d"]]
flat = "-".join([item for sublist in nested for item in sublist])


print(flat)            # Output: a-b-c-d




# 4) Formatting Strings Dynamically :- 

names = ["John", "Doe"]
sentence = " and ".join(names) + " are working together."



print(sentence)       # Output: John and Doe are working together.




# Example 5 :-    Joining Dictionary Values

data = {"name": "Alice", "age": "25", "city": "Paris"}
result = ", ".join(data.values())



print(result)         # Output: Alice, 25, Paris




# Joining Key-Value Pairs :-   You can explicitly format key-value pairs as strings and then join them.

data = {"name": "Alice", "age": "25", "city": "Paris"}
result = ", ".join(f"{key}: {value}" for key, value in data.items())



print(result)         # Output: name: Alice, age: 25, city: Paris





# Important Notes :- 


# 1) All Elements Must Be Strings: The elements in the iterable must be strings, or a TypeError will occur.

# nums = [1, 2, 3]
# print(",".join(nums))   # Raises: TypeError: sequence item 0: expected str instance, int found


# Solution: Convert elements to strings :- 

nums = [1, 2, 3]
result = ",".join(map(str, nums))


print(result)              # Output: 1,2,3



# 2) Works Only on Iterables: The argument to join() must be an iterable (e.g., list, tuple). Non-iterable arguments will raise an error.

# 3) Order Matters: The separator string is specified first, followed by the iterable.




# Limitations :-  

'''

The join() method can only handle iterables of strings. It does not directly support other data types like numbers or dictionaries.

'''





# Best Practices :-  

'''

1) Always ensure that all elements in the iterable are strings before using join().


2) Use meaningful separators to make the output more readable.

'''