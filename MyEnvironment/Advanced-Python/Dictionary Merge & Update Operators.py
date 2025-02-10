# Dictionary Merge & Update Operators :- In Python 3.9 and later, the merge (|) and update (|=) operators were introduced for dictionaries, making it easier and more concise to combine and update dictionaries. Here's everything you need to know about them:

# When Were These Operators Released ?

'''

   a) Introduced in Python 3.9 as part of PEP 584.

   b) They provide a cleaner and more readable way to merge and update dictionaries compared to traditional methods like .update() or dictionary unpacking.  

'''



# What Are They  ? 

# (a) Dictionary Merge (|) :- 

'''

   1) The | operator creates a new dictionary that combines the key-value pairs from two or more dictionaries.

   2) If there are duplicate keys, the values from the right-hand operand take precedence.

'''


# Syntax  :-  new_dict =  dict1 | dict2



# Example :- 
dict1 = {"a" : 1, "b" : 2}     # The b key is overwritten with the value from dict2 (3).

dict2 = {"b" : 3, "c" : 4}

merged_dict = dict1 | dict2
print(merged_dict)    # Output :- {'a': 1, 'b': 3, 'c': 4}



# (b) Dictionary Update (|=) :- 

'''

   1) The |= operator updates the dictionary in place with the key-value pairs from another dictionary.

   2) Like the | operator, values from the right-hand operand override existing keys.

'''

# Syntax :-  dict1 |= dict2


# Example :- 
dict3 = {"a" : 1 , "b" : 2 , "c" : 100 ,  "d" : 4}     # dict1 is updated in place with the values from dict2.

dict4 = {"b" : 3 , "c" : 4}

dict3 |= dict4
print(dict3)   # Output :- {'a': 1, 'b': 3, 'c': 4, 'd': 4}




#  Handling Nested Dictionaries :- 

dict5 = {"a" : {"x" : 1} , "b" : 2}     # The a key is overwritten, not merged deeply.

dict6 = {"a" : {"y" : 2} , "c" : 3}

merged_dict = dict5 | dict6
print(merged_dict)         # Output :- {'a': {'y': 2}, 'b': 2, 'c': 3}
 




#  Advantages :- 

'''

1) Cleaner Syntax :- 

      >> The | and |= operators make the code more concise and easier to read.

      Compare :- 

      # Before Python 3.9
      # Merge Using Dictionary Unpacking :- 
      merged_dict = {**dict1, **dict2}
      dict1.update(dict2)

      
      # Python 3.9+
      merged_dict = dict1 | dict2
      dict1 |= dict2


       
2) Immutable and Mutable Options :- 

     1) Use | for creating new dictionaries (immutable behavior).

     2) Use |= for modifying dictionaries in place (mutable behavior).


3) Chaining :-  The | operator supports chaining, allowing you to merge multiple dictionaries in a single statement.


'''

# Limitations :- 

'''

1) Not Compatible with Older Python Versions :- 

    a) The | and |= operators are only available in Python 3.9+.

    b) For older versions, you'll need to use methods like .update() or dictionary unpacking.

    
2) Shallow Merge :-  

     a) These operators only merge top-level keys and do not perform a deep merge for nested dictionaries.

'''


