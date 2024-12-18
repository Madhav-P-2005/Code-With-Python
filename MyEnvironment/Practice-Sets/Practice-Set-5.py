# Ans 1 :- 
dict = {"प्रेम" : input("Enter the corresponding word 'प्रेम' in English :- "), "जिम्मेदारी" : input("Enter the corresponding word 'जिम्मेदारी' in English :-") , "ईमानदारी" : input("Enter the corresponding word 'ईमानदारी' in English :-  "), "भरोसा" : input("Enter the corresponding word 'भरोसा' in English :- ")}
Word  = input("Enter the word you want meaning of : ")
print(dict[Word])


# Ans 2 :-
Data = set() 
s = int(input("enter the 1st number :-  "))
Data.add(s)
s = int(input("enter the 2nd number :-  "))
Data.add(s)
s = int(input("enter the 3rd number :-  "))
Data.add(s)
s = int(input("enter the 5th number :-  "))
Data.add(s)
s = int(input("enter the 6th number :-  "))
Data.add(s)
s = int(input("enter the 7th number :-  "))
Data.add(s)
s = int(input("enter the 8th number :-  "))
Data.add(s)

print("Set Data is :- ", Data)


# Ans 3 :- 
s = set()
s.add(int(input("enter an integer value :- ")))
s.add(input("enter an string value :- "))
print(s)


# Ans 4 :- 
s = set() 
s.add(20) 
s.add(20.0) 
s.add('20') # length of s after these operations?

# 1 == 1.0  . # Meaning :- In Python, the equality operator == checks whether the values on both sides are equal. When you compare 1 (an integer) and 1.0 (a floating-point number) using the equality operator, Python returns True.


# Reason for This Behavior :- 
'''Python follows a principle called "type coercion" during comparisons. When comparing an integer and a floating-point number, Python converts the integer to a floating-point number and then performs the comparison.'''

print("Length is :- ", len(s) , "set data  is :- " ,s)


# Ans 5 :-
s = {}
print(type(s))  # output :- <class 'dict'>


# Ans 6 :- 
# empty = {}
# empty = {input("Enter your Name : -  ") : input("Enter your favorite Language :- ") , input("Enter your Name : -  ") : input("Enter your favorite Language :- ") , input("Enter your Name : -  ") : input("Enter your favorite Language :- ") , input("Enter your Name : -  ") : input("Enter your favorite Language :- ")  }
# print("Empty Dictionary is filled by : - ", empty)


# or 

d= {}
name = input("Enter friends name : ")
lang = input("Enter Language name : ")
d.update({name : lang})

name = input("Enter friends name : ")
lang = input("Enter Language name : ")
d.update({name : lang})

name = input("Enter friends name : ")
lang = input("Enter Language name : ")
d.update({name : lang})

name = input("Enter friends name : ")
lang = input("Enter Language name : ")
d.update({name : lang})
print("Data is ", d)
print()


# Ans 7 :- If the names of 2 friends are same reference to the problem 6 then duplicate keys cannot be displayed only unique keys are considered.


# Ans 8 :- If languages of two friends are same reference to the problem 6 then both the values will be displayed . Here duplicate values are considered .


# Ans 9 :- 
s = {8, 7, 12, "Harry", [1,2]}
s[0] = 9  # Not possible throws error . list in set  is not possible .