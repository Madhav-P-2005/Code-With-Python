# NEWLY ADDED FEATURES IN PYTHON 

# Using Walrus Operator :-   The walrus operator (:=), introduced in Python 3.8, is an assignment expression operator that allows you to assign a value to a variable as part of an expression. It is named the "walrus operator" because of its resemblance to the eyes and tusks of a walrus (:=).  is officially called the "assignment expression .


'''

⭐) The walrus operator enables inline assignment, which means you can assign a value to a variable and use that value in the same expression. This can make your code more concise and potentially more readable in some cases.



Syntax :-  variable := expression  .    Here, variable is assigned the result of the expression.


Usage :-  The walrus operator is useful when :-

                   1)  Reducing redundancy in code.
                   2) Avoiding multiple evaluations of the same expression.
                   3) Writing concise and readable loops, comprehensions, or conditions.


Key Scenarios :- 
        1)  Loops
        2)  Conditional expressions
        3)  List comprehensions
        4)  Reducing function calls

        

Working :- 

    a) The walrus operator evaluates the expression on the right-hand side and assigns its value to the variable on the left-hand side.

    b) It can only be used within an expression, not at the top level of a script or block (e.g., not as a standalone statement like x := 5).

    
Important Notes :- 

     a) Readability :-  While it can make code more concise, overusing it may make your code less readable.

     b) Scope :-  The variable assigned using the walrus operator follows Python's scoping rules.

     c) Python Version: It is only available in Python 3.8 and later.

Common Mistakes :- 

     a) Using = instead of := for assignment within expressions. This will result in a SyntaxError.

     b) Overusing the walrus operator in places where clarity is more important than brevity.

     
 >>  The walrus operator is a powerful addition to Python that can simplify and streamline your code when used appropriately. However, it’s best to balance its use with readability!


'''

# Example :- 
if(n := len([1, 2, 3 ,4 ,5])) > 3:
            print(f"List is too Long ({n} elements , expected < = 3) ")  # Output :- List is too Long (5 elements , expected < = 3) 


            
# a) In a While Loop :-  Without the use of Walrus Operator 
data = input("Enter a value ( or 'stop' to quit) :-  ")

while data != 'stop':
        print(f" You entered : {data}")
        data = input("Enter a value (or 'stop' or quit :-  )")

'''

Output :-  


Enter a value ( or 'stop' to quit) :-  5
 You entered : 5

Enter a value (or 'stop' or quit :-  ) stop
 You entered :  stop

Enter a value (or 'stop' or quit) :- ....

...


'''


# With the walrus Operator :- 
while (data := input("Enter a value (or 'stop' to quit) :- ")) != 'stop':
        print(f"You entered :- {data}")



'''

Output :- 

   Enter a value (or 'stop' to quit) :- 5
   You entered :- 5
   Enter a value (or 'stop' to quit) :- stop
   
'''

# Here, data is assigned and checked in the same line, avoiding redundancy.



#  In an If Condition :-  Without the walrus operator . 

value = len(input("Enter you string :- "))
if value > 5:
        print(f"You string is more than {value}")
elif value==5:
        print(f"Your string is equal to {value}")
else:
        print(f"Your string is less than {value}")


'''

Output :- 

Enter you string :- Billu
Your string is equal to 5

'''


# With the walrus operator :-

if (value := len(input("Enter you string :- "))) >5 :print(f"Your string is more than {value}")
elif value==5:print(f"Your string is equal to {value}")
else: print(f"Your string is less than {value}")

'''

Output :- 

Enter you string :- Madhav
You string is more than 6
Enter you string :- Karan  
Your string is equal to 5

'''

# In List Comprehensions :- 

# Without the walrus Operator :-  
results = []
for x in range(10):
        squared = x**2
        if squared>10:
                results.append(squared)

print("Result is :- ",results)    # Output :-  Result is :-  [16, 25, 36, 49, 64, 81]



# With the walrus operator :- 
results = [squared for x in range(10) if(squared := x**2) > 10]
print(results)     # Ouput :- [16, 25, 36, 49, 64, 81]
