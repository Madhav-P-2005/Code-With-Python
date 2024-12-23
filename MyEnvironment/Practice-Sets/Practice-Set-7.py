# Ans 1 :- 
limit = int(input("Enter your limit :-  "))
user = int(input("Enter your number :-  "))

print(f"Multiplication table of {user} is :- ")
i=0
for i in range(limit+1):
    result = user * i
    print(user,"*",i,"=","",result)
    i+=1


# Ans 2 :- 
l = ["Harry", "Soham", "Sachin", "Rahul"]

for name in l:
    if name.startswith("S"):
        print(f"Good morning , How are you  {name}")


# Ans 3 :-
limit = int(input("Enter your limit :-  "))
user = int(input("Enter your number :-  "))

print(f"Multiplication table of {user} is :- ")
i=0

while(i<=limit):
    result = user * i
    print(user,"*",i,"=","",result)
    i+=1


# Ans 4 :- 

'''
Learnings :- 

# Reassigning i:-  The for loop for i in range(user) reassigns i to every value in the range, starting from 0 up to user - 1. So, i starts as 0 during the first iteration, causing the ZeroDivisionError.
 
>> Why user + 1 in range(1, user + 1)?
=> range(start, end): The range function in Python generates numbers starting from start and goes up to, but not including, end. So, range(1, user + 1) generates numbers from 1 to user.

# Inclusive Loop: If you want the loop to include the number user itself, you need to set the end value to user + 1, because range(1, user) would only go up to user - 1.

'''

user = int(input("Enter your number :-  "))

flag=False
count=0
for i in range(1,user+1):
        if user % i == 0:
          count+=1
          i+=1
          flag=True
        else:
           flag=False

if count==2:
    print(f"{user} is a prime number ")
else:
    print(f"{user} is not a prime number")



# Ans 5 :- 
limit = int(input("Enter your number :-  "))
sum = 0
for i in range(limit+1):
    sum = sum + i
    i+=1

print(f"Sum of {limit} natural numbers are :-  ",sum)



# Ans 6 :-
user = int(input("Enter your number :-  "))
fact = 1
    
for i in range(1,user+1):
    fact = fact * i
    i+=1

print(f"Factorial of {user} is :- ",fact)


# Ans 7 :- 
user = int(input("Enter your number :-  "))
for i in range(1, user+1):
    print(" "* (user-i),end="")
    print("*"* (2*i-1),end="")
    print("")


# Ans 8 :- 
user = int(input("Enter your number :-  "))
for i in range(0,user+1):
   print("*" * (1*i+1) , end="")
   print()

# or 
for i in range(1, user+1):
    print("*"*i,end=" ")
    print()


# Ans 9 :- 
user = int(input("Enter your number :-  "))
for i in range(1, user+1):
    for j in range(1, user+1):
        if i==1 or i==user or j==1 or j==user:
            print("*" , end=" ")
        else:
            print(" ", end = " ")
    print()


# or 
user = int(input("Enter your number :-  "))
for i in range(1, user+1):
    if(i==1 or i==user):
        print("*" * user ,end="")
    else:
        print("*" ,end="")
        print(" "*(user-2),end="")
        print("*" , end="")
    print("")



# Ans 10 :- 
limit = int(input("Enter your limit :-  "))
user = int(input("Enter your number :-  "))

print(f"Multiplication table of {user} is :- ")
i=0
for i in range(0,limit+1):
    result = user * limit
    print(user,"*",limit,"=","",result)
    limit-=1
