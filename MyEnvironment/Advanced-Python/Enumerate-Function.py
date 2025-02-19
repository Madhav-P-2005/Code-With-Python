#  Enumerate Function 

''' 

    1) The enumerate() function is a built-in Python function that adds a counter to an iterable (like a list, tuple, or string) and returns it as an enumerate object. This object can then be converted into a list of tuples or iterated over directly.

    2) Each tuple consists of an index and the corresponding item from the iterable.

'''


# Syntax :-   enumerate(iterable, start=0)


# Parameters :- 

'''

1) iterable :-  Any iterable object (e.g., list, tuple, string, dictionary, etc.).


2) start (optional): The starting index of the counter. Default is 0.

Returns :- 
     An enumerate object, which is an iterator that produces tuples (index, value).

'''


# How It Works :- 

'''

1) enumerate() takes an iterable and a starting index as input.

2) It iterates through the items of the iterable, keeping track of the index of each item.

3) It pairs each index with the corresponding value as a tuple (index, value).

The output is lazy (generated on demand) and memory-efficient.

'''


# Example 

# Without Enumerate function 

l = [3, 513 , 53 , 535]

index = 0
for item in l:
    
    print(f"The item number at {index} is {item}")
    index+=1

# Note :- This can be simplified using enumerate function 



# With Enumerate Function 

for index,item in enumerate(l):
    print(f"The item numbeer at index {index} is {item}")

'''

Output :- 

The item number at 0 is 3
The item number at 1 is 513
The item number at 2 is 53
The item number at 3 is 535

The item numbeer at index 0 is 3
The item numbeer at index 1 is 513
The item numbeer at index 2 is 53
The item numbeer at index 3 is 535


'''


# Example 2 :- Using start ? 

marks = [1 ,2 ,3 ,4, 5, 6, 7,8,9,10]

for index , mark in enumerate(marks , start=1):
    print(mark)
    if index==5:
        print("Madhav has arrived !")



'''

Output :- 

1
2
3
4
5
Madhav has arrived !
6
7
8
9
10

'''

# Enumerate in tuples , dictionaries , ....many more .. to be done .  # Pending work 