'''
Q) 1)  We all have played snake, water gun game in our childhood. If you haven’t, google the 
rules of this game and write a python program capable of playing this game with the 
user.

'''

# To generate a random number in Python, you can use the random module. This module provides various functions to generate random numbers. Here's how you can generate a random number:

# 1) Import the random Module: This module needs to be imported to use its functions.

# 2) Use random.randint(a, b): This function returns a random integer N such that a <= N <= b.

import random

Rules = {0 : "Snake" , 1 : "Water" , 2 : "GUN"}
print(Rules)

choices_dict = {0 : "Snake" , 1 : "Water" , 2 : "GUN"}

user = int(input("Enter your Choice  :- "))
print(choices_dict.get(user))
computer = random.randint(1,2)
print(f"The Computer's  number is : ",computer)
print(choices_dict.get(computer))


if((user==0 and computer==1) or (user==1 and computer==0)  or (user==2 and computer==0)):
    print(f"{user} :- You Won ! Congrats 🥳😎")
elif ((user==1 and computer==0) or (user==1 and computer==0)  or (user==2 and computer==1)):
    print(f"{computer} :- Computer Won ! Congrats 🥳😎")
elif((user==1 and computer==1) or (user==0 and computer==0)  or (user==2 and computer==2)):
    print(f"{user} == {computer} . Draw 😵‍💫. Better luck next Time")
else:
    print("Please choose a valid Input")






