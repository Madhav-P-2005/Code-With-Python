# Definition 

'''

1) Lambda functions in Python are anonymous functions (functions without a name). They are used to define small, one-liner functions in a concise and readable manner, especially for short-lived use cases.

2)  Lambda functions are often used as arguments to higher-order functions, or to create simple inline functions without the overhead of defining a full function using the def keyword.


'''



# Syntax :-    lambda arguments: expression




# Components :- 

'''

1) lambda :-  The keyword that defines a lambda function.

2) arguments :-  A comma-separated list of parameters (just like regular function arguments).

3) expression :-  A single expression that the function evaluates and returns. Note: Lambda functions can’t include statements or multiple expressions.

'''




# How It Works :-  

'''

Declaration :-   A lambda function is declared using the lambda keyword, followed by arguments and the expression.

Evaluation :-  When called, the function evaluates the expression and returns the result.

Anonymous Nature :-  Unlike functions created with def, lambda functions don’t have a name unless explicitly assigned to a variable.

'''


# Example :-  Without Lambda Function

def square(n):
    return n*n


print(square(5))




# Example 2 :- With Lambda Function 
square = lambda x : x*x
print(square(9))



# Example 2.0 
sum_of_three_Numbers = lambda a , b , c : a+b+c
print("Sum is ",sum_of_three_Numbers(1,2,3))