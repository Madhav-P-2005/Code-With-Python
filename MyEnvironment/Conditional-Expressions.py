# Syntax :-  if conditon:
             # Statements to execute if
             # condition is true


# If Statement :- 
a = 20
if a > 50 : 
    print("This is the if body")
print("This is outside the if Block"+"\n\n")
print()


# If - Else Statement :- 

# Syntax :-  if(condition):
             #Executes this block if 
             # condition is true
             #else:
             #Executes this block if
             # conditon is false

a = int(input("Enter your age :- "))
if(a>=18) :
    print("You are above the age of consent ")
    print("Good for you ")

else :
    print("You are below the age of consent")

print("End of the program")


# If elif else Ladder / statement :- 

# Syntax :-   if(condition):
#                 Statement
              #elif(condition):
                    # statement
              # :
              # :
              #else:
                  #Statement


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


# Nested - If Statement / Multiple - If Statement :- 

# Syntax :-  if(condition):
            # Executes if condition1 is true
                # if(condition2):
                   # Executes if condition2 is true
             # condition2 ends here
    # condition1 ends here


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