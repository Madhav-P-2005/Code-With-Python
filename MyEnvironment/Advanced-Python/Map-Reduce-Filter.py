'''

  >> These three functions—map(), filter(), and reduce()—are functional programming tools in Python. They operate on iterables, applying a function to their elements to process or transform data.

1) map() :-  Transforms each element of an iterable using a function.
 
2) filter() :-  Filters elements of an iterable based on a condition.

3) reduce() :-  Aggregates or reduces elements of an iterable into a single cumulative value.

'''


# 1)  map() :-   The map() function applies a specified function to every item in an iterable and returns a map object (which is iterable).


# Syntax :-   map(function, iterable, ...)



# How It Works :- 

'''

    1) The function is applied to each element of the iterable.

    2) If multiple iterables are provided, the function should accept that many arguments.


'''




# Example 1 :-  Without Map function :- 


List = [1 ,2 ,3 ,4 ,5]

square  = lambda x : x * x 


for num in List:
       print(square(num), end=" ")     # Output :- 1 4 9 16 25


print() 



# Example 2 :- With Map function 

sqlist = map(square , List)

print(list(sqlist))        # Output :-   [1, 4, 9, 16, 25]





# 2) filter() :-   The filter() function filters elements from an iterable based on whether they meet a specified condition.



# Syntax :-    filter(function, iterable)



# How It Works :-  

'''

   1) The function should return True for elements that you want to keep and False for elements to discard.

   2) Returns a filter object (an iterable).

'''


# Example 3 :-  With Filter 
def even(n):
       if(n%2==0):
              return True
       return False 

onlyEven = filter(even, List)

print(list(onlyEven))     # Output :-  [2, 4]





# 3) reduce() :- The reduce() function performs a cumulative operation on the elements of an iterable, reducing them to a single value.



# Syntax :-  from functools import reduce

'''  reduce(function, iterable, initializer)  '''




# How It Works :-  
  
'''

>>  The function is applied cumulatively to the elements of the iterable.
An optional initializer can be provided as the starting value.

'''



# Example 4 :- With Reduce() Method 
from functools import reduce     # To use Reduce you need to import from functools module 

 

def sum(a , b):
       return a + b

print(reduce(sum, List))     # Output :-  15



# Example 5 :- With Reduce() Method 

multiply = lambda x,y : x * y

print(reduce(multiply , List))    # Output :-   120






# Key Differences  ? 

'''

Function	             Purpose            	                              Input	                                                        Output
------------------------------------------------------------------------------------------------------------------------------------------------------------
map()	       Transforms each element in an iterable.	                  Function + Iterable(s)	                                      Iterable (transformed).
filter()	Filters elements based on a condition.	          Function (returns True/False) + Iterable	                          Iterable (filtered).
reduce()	Aggregates elements into a single value.	     Function (binary operation) + Iterable (+ optional initializer)	                 Single Value.


'''