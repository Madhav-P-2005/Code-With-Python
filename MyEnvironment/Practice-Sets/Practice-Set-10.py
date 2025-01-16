# Ans 1 :-
class Programmer:
    company = "Microsoft"

    def __init__(self, name=None , Age=None, Field=None , Salary=None):
        self.name = name
        self.Age = Age
        self.Field = Field
        self.Salary = Salary


    def info(self):
        print("# Welcome to Microsoft")
        self.name = input("Enter your Name :-  " )
        self.Age =  int(input("Enter your Age :-  " ))
        self.Field = input("Enter your Field :-  " )
        self.Salary = int(input("Enter your Salary :-  "))

        print(f"Displaying details related to the Programmers work in {self.company} are :- ")
        print("Name :-   ", self.name)
        print("Age :-    ", self.Age)
        print("Field :-   ", self.Field)
        print("Salary :-   ", self.Salary)
 
p = Programmer()
p.info()




# Ans 2 :- 

import math
class Calculator: 
    def __init__(self , number=None  ,  square=None , cube=None , square_root=None):
        self.number = number
        self.square = square
        self.cube = cube
        self.square_root =square_root

    def Cal(self):
        self.number = int(input("Enter any Number :-  "))
        C.result()
        
    def result(self):
        print(f"Square of {self.number} is :-   ",(self.number*self.number))
        print(f"Cube of  {self.number}  is :-   ",(self.number*self.number*self.number))
        print(f"Square Root of {self.number} is :-   ",math.sqrt(self.number))
    

C = Calculator()
C.Cal()




# Ans 3 :- 

class Demo:
      
    a = 4  # Class Attribute 


obj = Demo()
print(obj.a)  # Prints the class Attribute because instance attribute is not Present . Output :- 4

obj.a = 0   # Object/Instance  Attribute  is set .
Demo()

print(obj.a) # Prints the instance attribute because instance attribute is set .  Output :- 0
print(Demo.a)  # Ans :- Do not change . # Output :- 4




# Ans 4 :- 
import math
class Calculator: 
    def __init__(self , number=None  ,  square=None , cube=None , square_root=None):
        self.number = number
        self.square = square
        self.cube = cube
        self.square_root =square_root

    def Cal(self):
        self.number = int(input("Enter any Number :-  "))
        print(f"Square of {self.number} is :-   ",(self.number*self.number))
        print(f"Cube of  {self.number}  is :-   ",(self.number*self.number*self.number))
        print(f"Square Root of {self.number} is :-   ",math.sqrt(self.number))

    @staticmethod
    def hello():
        print("Hello Guys . This is a static method")
        
        
        
C = Calculator()
C.Cal()
C.hello()



# # Ans 5 :- 
from random import randint
class Train:

    def __init__(self , trainNo=None , fro=None , to=None):
        self.trainNo =  int(input("Enter the train No to book :-  "))
        self.fro =  input("Enter the starting Location :- ")
        self.to =   input("Enter the destination Location :- ")
         

    def book(self):
         print(f"Ticket is booked in train no :  {self.trainNo}  from  {self.fro} to {self.to}")
         
      
    def getStatus(self):
        print(f"Train no : {self.trainNo} is running on time ")

    def Fare_Info(self):   # Ctrl + Alt  + 4   => ₹
            print(f"Ticket fare in train no : {self.trainNo} from {self.fro} to {self.to} is ₹{randint(222, 555)}")

T = Train()
T.book()
T.getStatus()
T.Fare_Info()




# Ans 6 :-
class Demo:
     
     def __init__(harry , name , channel):
          harry.name = name
          harry.channel = channel

     def  info(harry):
          print("Name  :-   ",harry.name)  # Output :- Name  :-    Harry Bhai
          print("Channel Name :-  ",harry.channel)  # Output :-  Channel Name :-   CodeWithHarry

D = Demo("Harry Bhai" , "CodeWithHarry")
D.info()