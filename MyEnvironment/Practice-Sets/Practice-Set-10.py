# Ans 1 :-
# class Programmer:
#     company = "Microsoft"

#     def __init__(self, name=None , Age=None, Field=None , Salary=None):
#         self.name = name
#         self.Age = Age
#         self.Field = Field
#         self.Salary = Salary


#     def info(self):
#         print("# Welcome to Microsoft")
#         self.name = input("Enter your Name :-  " )
#         self.Age =  int(input("Enter your Age :-  " ))
#         self.Field = input("Enter your Field :-  " )
#         self.Salary = int(input("Enter your Salary :-  "))

#         print(f"Displaying details related to the Programmers work in {self.company} are :- ")
#         print("Name :-   ", self.name)
#         print("Age :-    ", self.Age)
#         print("Field :-   ", self.Field)
#         print("Salary :-   ", self.Salary)
 
# p = Programmer()
# p.info()



# Ans 2 :- 
class Calculator: 
    def __init__(self , number=None  ,  square=None , cube=None , square_root=None):
        self.number = number
        self.square = square
        self.cube = cube
        self.squarsquare_root =square_root

    def Cal(self):
        self.number = int(input("Enter any Number :-  "))
        C.result()
        
    def result(self):
        input(f"Square root of {self.number} is :-   ",(self.number*self.number))
        input(f"Cube of  {self.number}  is :-   ",(self.number*self.number*self.number))
        input(f"Square Root of {self.number} is :-   ",(self.number**2))

C = Calculator()
C.Cal()