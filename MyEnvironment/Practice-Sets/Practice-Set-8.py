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
 
# or

def f_to_c(f):
      return 5*(f-32)/9

f = int(input("Enter temperature in F : "))
c = f_to_c(f)
print(f"{round(c,2)} C")




# Ans 3 :- 
print("a")
print("a") 
print("c" , end="")
print("d" , end="")
print()



# Ans 4 :- 

'''
sum(1) = 1
sum(2) = 1 + 2 
sum(3) = 1 + 2 + 3 
sum(n) = 1 + 2 + 3 + 4 + 5 .... + n

'''

def Sum(n):
     if n==1 :return 1 
     else:
          return Sum(n-1) + n
     

n = int(input("Enter any Number :-  "))
print(f"Sum of {n} Natural Numbers are :- ",Sum(n))



# Ans 5 :- 
# Using Function :- 
def Pattern1(user):
  for i in range(0,user+1):
     for j in range(user, i, -1):  # j starts at i and decrements by 1 each iteration
          print("*", end=" ")
     print()  
   

user = int(input("Enter the number of rows: "))
Pattern1(user)


# Using Recursion :- 
def Pattern(user):
     if user==0:return  # return stops the statement 
     print("*" * user)
     Pattern(user-1)


user = int(input("Enter the size of elements :- "))
Pattern(user)




# Ans 6 :- 
def Convert_Cms():
     inches = int(input("Enter the value in inches :-  "))
     cms = inches * 2.54
     print(f"Converted from {inches} to Cms is :- ",cms,"cm") 

Convert_Cms()


# or Using return 
def inch_to_cms(inches):
     return inches * 2.54

inches = int(input("Enter the value in inches :-  "))
print(f"The corresponding value in cms is {inch_to_cms(inches)}")




# Ans 7 :- 
list_of_Elements=[]
def List():
    print("Enter the No of elements you want to insert in the List :- ")
    n = int(input())
    for i in range(n):
         data = input()
         list_of_Elements.append(data)

    print("Elements are " , list_of_Elements)

List()

def remove(list_of_Elements):
     new_list=[]
     print("Enter the word to be Modified ")
     word = input()
     print("Enter the part of that word to be striped ")
     word_part = input()

     for item in list_of_Elements:
        if item.strip() == word:
            modified_word = item.strip(word_part)
            new_list.append(modified_word)
        else:
            new_list.append(item) 



     print("Original List Of Elements:", list_of_Elements)
     print("New List of Elements:", new_list)

remove(list_of_Elements)

# or 

def rem(l , word):
    n = []
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n
        

l=["Harry" , "Rohan" , "Shubham"]
print(rem(l, "Roh"))




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