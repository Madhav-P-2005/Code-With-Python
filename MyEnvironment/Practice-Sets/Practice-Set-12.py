# Ans 1 :- 

try:
  with open(r"E:\Python Tutorial - Code With Harry\MyEnvironment\Files\Open-a-File-on-the-Server.txt" , "r") as file :
    print(file.read())
except FileNotFoundError as e:
    print(e)

try:
  with open(r"E:\Python Tutorial - Code With Harry\MyEnvironment\Files\1.txt" , "r") as file:
    print(file.read())
except FileNotFoundError as e:
  print(e)

try:
  with open(r"E:\Python Tutorial - Code With Harry\MyEnvironment\Files\2.txt" , "r") as file:
    print(file.read())
except FileNotFoundError as e:
  print(e)
print("Thank You")


'''

Output :-  


Madhav is a Bad Boy . 
ReadLines() and ReadLine() Body :-  
I am third Line 
This is a demo to represent how to use ReadLines() function  in a File . 
[Errno 2] No such file or directory: 'E:\\Python Tutorial - Code With Harry\\MyEnvironment\\Files\\1.txt'
[Errno 2] No such file or directory: 'E:\\Python Tutorial - Code With Harry\\MyEnvironment\\Files\\2.txt'


'''




# Ans 2 :- 

List = [1 ,2,3 , 4, 5 ,6 ,7]

for index , item  in enumerate(List):
  if index == 2 or index == 4 or index == 6:
    print(item)



# Ans 3 :- 
num = int(input("Enter any number :-  "))
Multiply = [num * i  for i in range(1,11)]

print(Multiply)



'''

Output :- 

Enter any number :-  5
[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]


'''





# Ans 4  :- 

try : 
  number1 = int(input("Enter your Numerator  :- "))
  number2 = int(input("Enter your Denominator  :- "))

  divide = number1/number2
  print(f"Division of {number1} / {number2} is :- ", divide)

except ZeroDivisionError as e :
  print("Error :- ",e)
  print("Infinite")

finally : 
  print("Program ended")



'''

Output :- 

Enter your Numerator  :- 12
Enter your Denominator  :- 0
Error :-  division by zero
Infinite
Program ended

'''


# Ans 5 :- 

with open(r"E:\Python Tutorial - Code With Harry\MyEnvironment\Files\Tables.txt" , "a") as file:
  num = int(input("Enter any number :-  "))
  Multiply = [num * i  for i in range(1,11)]
  file.write(f"Table of {num} is :=  {str(Multiply)}  \n")


'''

Output :-   Enter any number :-  17

see tables.txt file 

'''