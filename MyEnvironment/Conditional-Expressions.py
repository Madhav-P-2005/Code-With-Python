# Control Statements :- Control statements are statements which control or change the flow of execution. The following are the control statements available in Python :- 

'''

● if statement
● if... else statement
● if... elif... else statement
● while loop
● for loop
● else suite
● break statement
● continue statement
● pass statement
● assert statement
● return statement

'''




# If Statement :-   The if statement in Python is used for decision-making. It allows your program to execute a block of code only if a specified condition is True.


'''

Syntax :-  if conditon:
             Statements to execute if
             condition is true
             
'''


a = 20
if a > 50 : 
    print("This is the if body")
print("This is outside the if Block"+"\n\n")
print()

'''

Output :-   This is outside the if Block

'''




# If - Else Statement :-   The if-else statement allows you to execute one block of code when a condition is True and another block when it is False.


'''

Syntax :-  if(condition):
             Executes this block if 
             condition is true
             else:
             Executes this block if
             conditon is false
             
'''


a = int(input("Enter your age :- "))
if(a>=18) :
    print("You are above the age of consent ")
    print("Good for you ")

else :
    print("You are below the age of consent")

print("End of the program")


'''

Output :- 

Enter your age :- 
23
You are above the age of consent 
Good for you 
End of the program


'''




# If elif else Ladder / statement :-   The if-elif-else statement is used when multiple conditions need to be checked one by one. It works like a decision-making ladder, where only one condition executes.


'''

Syntax :- if condition1:
                   # Executes if condition1 is True

          elif condition2:
                   # Executes if condition2 is True

          elif condition3:
                   # Executes if condition3 is True

          else:
               # Executes if none of the conditions are True


'''


a = int(input("Enter your age :- "))
if(a>=18) :
    print("You are above the age of consent ")
    print("Good for you ")

elif(a<0):
    print("You are entering an invalid negative age")

elif(a==0):
    print("You are entering 0 which is not a valid age ")

else :
    print("You are below the age of consent")

print("End of the program")


'''

Output :- 

Enter your age :- 
12
You are below the age of consent
End of the program

'''




# Nested - If Statement / Multiple - If Statement :- 

'''

Syntax :-  if(condition):
            Executes if condition1 is true
                if(condition2):
                   Executes if condition2 is true
             condition2 ends here
    condition1 ends here

'''


a = int(input("Enter your age :- "))

if(a%2 == 0):
    print("a is even")

if(a>=18) :
    print("You are above the age of consent ")
    print("Good for you ")

elif(a<0):
    print("You are entering an invalid negative age")

else :
    print("You are below the age of consent")

print("End of the program")



'''

Output :- 

Enter your age :- 
100
a is even
You are above the age of consent 
Good for you 
End of the program

'''




# Ternary Conditional Operator :- The ternary conditional operator, also known as the conditional expression, is a compact way to execute conditional statements in Python. It's useful for writing concise and readable code.

# Syntax :- <value_if_true> if <condition> else <value_if_false>

x = 10
result = "x is greater than 5" if x > 5 else "x is not greater than 5"

# Ternary Operator in List Comprehensions :- 
numbers = [1,2,3,4,5]

even_odd = ["even" if num % 2 == 0 else "odd" for num in numbers]

print(even_odd)              # Output: ['odd', 'even', 'odd', 'even', 'odd']