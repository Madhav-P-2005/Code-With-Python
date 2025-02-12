# ‘global’ keyword is used to modify the variable outside of the current scope.


# Key Rules of the global Keyword :- 

'''

   1) Without global, a variable inside a function is treated as local.

   2) A global declaration is required only when modifying a global variable inside a function. Reading a global variable does not require global.

'''


# Syntax :-  
global variable_name

# variable_name :-  The name of the variable you want to declare as global.




# Example 1 :- 
def Global_Example():
    a1  = 10     # Local variable 
    print(a1)     # Output  :-  10



a1 = 100
print(a1)   # 100
Global_Example()


'''

Output :-  100
           10

'''




# Example 2 :-

a2 = 100       # Global Variable 

def Global_Example2():
    a2  = 10     # Local Variable 
    print(a2)     # Output  :-  10



Global_Example2()
print(a2)   # Output :-  100



'''
Output :-   10
            100

'''



print()



# Example 3 :- Using Global Keyword 

a3 = 100       # Global Variable 

def Global_Example2():
    global a3
    a3  = 10      # Local Variable 
    print(a3)     # Output  :-  10



Global_Example2()
print(a3)   # Output :-  10



'''
Output :-   10
            10

'''

