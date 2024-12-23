# Python Program to demonstrate the Dictionaries ?

# x={}

# print("How many players?",end='')
# n=int(input())

# for j in range(n):
#     print("Enter player name",end='')
#     k=input()
#     print("enter runs:",end='')
#     v=int(input())
#     x.update({k:v})

# print("\n players in this match:")
# for pname in x.keys():
#     print(pname)
# print ("enter player name:",end='')
# name=input()
# runs=x.get(name,-1)
# print(runs)
# if(runs==-1):
#     print("player not found")
# else:
#     print("{} made runs {}.".format(name,runs))


# try:
#     lst = eval(input("Enter numbers separated by a comma:"))
#     tot = 0
#     if not lst:
#         raise RuntimeError()
#     else:
#         for x in lst:
#             tot += x
#         result = tot / len(lst)
#         print("Result is", result)
# except ZeroDivisionError:
#     print("Division by Zero")
# except SyntaxError:
#     print("A comma may be missing in the input")
# except RuntimeError:
#     print("Maybe Meaningless")
# except TypeError:
#     print("Enter only numbers")
# except:
#     print("Something is wrong")
# else:
#     print("No Exceptions")
# finally:
#     print("Finally Clause is executed")



# List  = []
# n = int(input("enter the size :- "))

# for i in range(n):
#     value = int(input(f"Enter value {i + 1} : "))
#     List.append(value)

# mid_point = len(List)//2
# first_half = List[:mid_point]
# second_half = List[mid_point:]
# positive_in_firsthalf = sum(1 for num in first_half if num > 0)
# positive_in_secondhalf = sum(1 for num in second_half if num > 0)

# print(f"Number of positive numbers in first Half " , positive_in_firsthalf)
# print(f"Number of positive numbers in second Half " , positive_in_secondhalf)

# Max = List[0]
# for j in List :
#     if Max < j:
#         Max = j 
# print(f" The max numbers in list is " , {Max})
# print(".......")
# print()
# Min = List[0]
# for j in List:
#     if Min > j:
#         Min = j  

# print(f" The min number in list is  : ",{Min})




# import os

# # Open a file in read and binary mode
# f1 = open("Python_Type_codes.png", "rb")
# f2 = open("download7.png", "wb")  # Changed output filename to avoid overwriting
# bytes = f1.read()
# f2.write(bytes)
# f1.close()
# f2.close()

# # Display the file name
# print()
# print(os.path.basename("E:/Python Tutorial - Code With Harry/MyEnvironment/demo.py"))
# print()

# # Write text to a file
# f = open("myfile.txt", "a")
# text = input("Enter text: ")
# f.write(text + '\n')  # Adding newline for better readability
# f.close()

# # Read text from file
# f = open("myfile.txt", "r")
# text = f.read()
# print(text)
# f.close()

# # Write numbers to a file and close it
# f = open("myfile.txt", "a")
# for i in range(10):
#     print(i, file=f)
# f.close()  # Close the file when we're done!

# # Reading file line by line till the end of file
# f = open("myfile.txt", "r+")
# line = f.readline()
# while line:
#     print(line, end='')  # Use end='' to avoid extra newlines
#     line = f.readline()
# f.close()


''' 

The f in f-string stands for formatted string literals. This feature was introduced in Python 3.6 and provides a way to embed expressions inside string literals using curly braces {}. The f before the string indicates that it is a formatted string, and it allows you to include variables and expressions directly within the string.

Benefits of Using f-strings :-

Readability: It makes the code more readable and easier to write, especially when concatenating multiple variables into a string.

Efficiency: f-strings are generally faster than other string formatting methods.

Simplicity: It simplifies the process of embedding variables and expressions in strings.

'''

# a) Print the list in last in first out mode :- 
# lst=[]
# print("Enter the size of the list :-  ")
# n=int(input())
# for i in range(n):
#     value=int(input(f"Enter the element {i} :- "))
#     lst.append(value)
# for i in lst:
#     print(lst[-i] , end=' ')




# lst=[]
# print("Enter the size of the list :-  ")
# n=int(input())
# for i in range(n):
#     value=int(input(f"Enter the element {i} :- "))
#     lst.append(value)

# count_positive=0
# count_negative=0
# for j in lst:
#     if j>0:
#         count_positive+=1
#     else:
#         count_negative+=1

# print(f"No of Positive Numbers in list are :- ",count_positive)
# print(f"No of Negative Numbers in list are :- ",count_negative)


# c. Search for a specific element in the list
# lst=[]
# print("Enter the size of the list :-  ")
# n=int(input())
# for i in range(n):
#     value=int(input(f"Enter the element {i} :- "))
#     lst.append(value)

# flag=False
# key=int(input("Enter the element you want to search :-  "))
# for i in range(n):
#     if key==lst[i]:
#         print(f"{key} is present in location {i}")
#         flag=True
#     else:
#         flag=False

# if key>n:
#     print(f"{key} Not Found ! in the list ")
    

# # d. Sort the elements in the list
# lst=[]
# print("Enter the size of the list :-  ")
# n=int(input())
# for i in range(n):
#     value=int(input(f"Enter the element {i} :- "))
#     lst.append(value)

# print("Elements before Sorting :-  \n")
# for i in range(n):
#     print(lst[i])

# flag=False
# print("Elements after Sorting :- \n")
# for i in range(n-1):
#     for j in range(n-i-1):
#         if lst[j] > lst[j+1]:
#             flag=True
#             temp = lst[j]
#             lst[j] = lst[j+1]
#             lst[j+1] = temp
#         else:
#             flag=False
    
# if flag==False:
#     print("It is in descending order ")
# else:
#    print(f"Sorted Elements are (ascending order: small to big): {lst}")

# lst=[]
# print("Enter the size of the list :-  ")
# n=int(input())
# for i in range(n):
#     value=int(input(f"Enter the element {i} :- "))
#     lst.append(value)

# print("Elements before Sorting :-  \n")
# for i in range(n):
#     print(lst[i])

# flag=False
# print("Elements after Sorting :- \n")
# for i in range(n-1):
#     for j in range(n-i-1):
#         if lst[j] < lst[j+1]:
#             flag=True
#             temp = lst[j]
#             lst[j] = lst[j+1]
#             lst[j+1] = temp
#         else:
#             flag=False
    
# if flag==False:
#     print("It is in ascending order ")
# else:
#    print(f"Sorted Elements are (descending order:-  Big to small): {lst}")


# e. Find the largest and smallest elements in the list

# lst=[]
# print("Enter the size of the list :-  ")
# n=int(input())
# for i in range(n):
#     value=int(input(f"Enter the element {i} :- "))
#     lst.append(value)


# print("Displaying the elements in the list :- ")
# for i in range(n):
#     print(lst[i])

# large=lst[0]
# for j in range(n):
#     if large < lst[j]:
#         large=lst[j]


# print(f"Largest element in the list is ",large)

# small=lst[0]
# for j in range(n):
#     if small > lst[j]:
#         small=lst[j]

# print(f"Smallest element in the list is ",small)



# lst=[]
# print("Enter the size of the list :-  ")
# n=int(input())
# for i in range(n):
#     value=int(input(f"Enter the element {i} :- "))
#     lst.append(value)


# print("Displaying the elements in the list :- ")
# for i in range(n):
#     print(lst[i])

# large = max(lst)
# small = min(lst)
# print(f"Largest element in the list is ",large)
# print(f"Smallest element in the list is ",small)

# Reassigning i: The for loop for i in range(user) reassigns i to every value in the range, starting from 0 up to user - 1. So, i starts as 0 during the first iteration, causing the ZeroDivisionError.



# # Ans 7 :- 
# user = int(input("Enter your number :-  "))
# for i in range(1, user+1):
#     print(" "* (user-i),end="")
#     print("*"* (2*i-1),end="")
#     print("")


# # Ans 6 :- 
# user = int(input("Enter your number :-  "))
# for i in range(0,user+1):
#    print("*" * (1*i+1) , end="")
#    print()


# # Ans 7 :-





# user = int(input("Enter your number :-  "))
# for i in range(1, user+1):
#     print("***"* (2*i-1),end="")

#     print(" "* (user-i),end="")
#     print("***"* (2*i-1),end="")
    
# user = int(input("Enter your number :-  "))
# for i in range(1, user+1):
#     for j in range(1, user+1):
#         if i==1 or i==user or j==1 or j==user:
#             print("*" , end=" ")
#         else:
#             print(" ", end = " ")
#     print()
# user = int(input("Enter your number :-  "))
# for i in range(1, user+1):
#     print("*"*i,end=" ")
#     print()

# user = int(input("Enter your number :-  "))
# for i in range(1, user+1):
#     if(i==1 or i==user):
#         print("*" * user ,end="")
#     else:
#         print("*" ,end="")
#         print(" "*(user-2),end="")
#         print("*" , end="")
#     print("")


# dict = {}
# print("How many players ? ",end=" ")
# n = int(input())
# for i in range(n):
#     print("Enter Player Name " , end = "")
#     p = input()
#     print("Enter the runs ",end = " ")
#     r = int(input())
#     dict.update({p:r})

# print("\nPlayers in this Match :- ")
# for pname in dict.keys():
#     print(pname)

# print("Enter the player name :-  ",end= " ")
# name=input()
# runs=dict.get(name,-1)
# if runs==-1:
#     print(f"{name} Player Not Found ")
# else:
#     print('{} made {} '.format(name,runs))
