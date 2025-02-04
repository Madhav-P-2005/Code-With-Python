# When Released ?

# List comprehensions were introduced in Python 2.0, released in 2000.


# Definition :- 

'''

  >> List comprehensions are a concise and elegant way to create lists in Python. They allow you to construct new lists by applying an expression to each element in an existing iterable (like a list, tuple, or range), optionally filtering elements based on a condition.


'''


# Syntax :-  new_list = [expression for item in iterable if condition]


# Components :- 

'''

   1) Expression :-  The operation or transformation applied to each element.

   2) for item in iterable :-  Iterates through the given iterable (e.g., a list, range, or string).

   3) if condition (optional) :-  Filters elements based on a condition.

'''



# How It Works :- 

'''

1) The comprehension loops through each item in the iterable.

2) For each item, it evaluates the expression.

3) If a condition is specified, only elements satisfying the condition are included.

4) The resulting elements are collected into a new list.

'''



# Example 1 :-  Without List Comprehensions 

myList = [1 ,2 ,9 , 5 , 3 , 5]

squaredList = []
for item in myList:
    squaredList.append(item*item)

print(squaredList)   # Output :-  [1, 4, 81, 25, 9, 25]



print()



# Example 2 :-   With List Comprehensions

squaredList  =  [i*i for i in myList]

print("List Comprehensions :- ",squaredList)       # Output :-  List Comprehensions :-  [1, 4, 81, 25, 9, 25]
