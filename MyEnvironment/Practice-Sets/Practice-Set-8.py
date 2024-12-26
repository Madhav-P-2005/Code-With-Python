# Ans 1 :- 
def Greatest_of_3():
     user1 = int(input("Enter the first Number :- "))
     user2 = int(input("Enter the second Number :-  "))
     user3 = int(input("Enter the third Number :- "))
     if user1>user2:
          if user1>user3:
               print(f"{user1} is the greatest among all three numbers ")
          else:
               print(f"{user3} is the greatest among all three numbers ")
     else:
          if user2>user3:
               print(f"{user2} is the greatest among all three numbers ")
          else:
               print(f"{user3} is the greatest among all three numbers ")

Greatest_of_3()



# Ans 2 :- 
def Convert():
     Celcius = int(input("Enter the temperature in Celcius :- "))
     Fahrenheit = (9/5 * Celcius) + 32
     print(f" Converted From {Celcius} to Fahrenheit is  :-  ", Fahrenheit ,"F")

Convert()
 


# Ans 3 :- 
print("a")
print("a")
print("c" , end="")
print("d" , end="")
print()



# Ans 4 :- 





# Ans 5 :- 




# Ans 6 :- 
def Convert_Cms():
     inches = int(input("Enter the value in inches :-  "))
     cms = inches * 2.54
     print(f"Converted from {inches} to Cms is :- ",cms,"cm") 

Convert_Cms()



# Ans 7 :- 
list_of_Elements=[]
def List():
    print("Enter the No of elements you want to insert in the List :- ")
    n = int(input())
    for i in range(n):
         data = input()
         list_of_Elements.append(data)

    print("Elements are " , list_of_Elements)


def remove():
     print("Enter the word to be removed from the list :- ")
     word=input() 
     if word in list_of_Elements:
          list_of_Elements.remove(word)
     print(f"Elements after removing {word} from the list is :- ",list_of_Elements)
     print("List after Strip method from String  :- ")
     string = "  ".join(list_of_Elements)
     print("Elements after converting list to string :-  ",string)
     string.strip()
     print(string)



List()
remove()



# Ans 8 :- 
def Multiply() : 
     limit = int(input("Enter your limit :-  "))
     user = int(input("Enter your number :-  "))
     print(f"Multiplication table of {user} is :- ")
     i=0
     for i in range(limit+1):
              result = user * i
              print(user,"*",i,"=","",result)
              i+=1

Multiply()