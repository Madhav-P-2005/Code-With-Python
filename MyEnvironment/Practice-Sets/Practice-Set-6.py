# Ans 1:- 
user1 = int(input("Enter the 1st Number :- "))
user2 = int(input("Enter the 2nd Number :- "))
user3 = int(input("Enter the 3nd Number :- "))
user4 = int(input("Enter the 4th Number :- "))

if(user1>user2 and user1>user3 and user1>user3):
    print(f"{user1} is the Greatest amoung the Four user Inputs")
elif(user2>user1 and user2>user2 and user2>user4):
    print(f"{user2} is the Greatest amoung the Four user Inputs")
elif(user3>user1 and user3>user2 and user3>user4):
    print(f"{user3} is the Greatest amoung the Four user Inputs")
elif(user4>user1 and user4>user2 and user4>user3):
    print(f"{user4} is the Greatest amoung the Four user Inputs")


# Ans 2 :-
Student = input("Enter the Student name :- ")
sub1 = int(input("Enter the marks of Subject 1 :- "))
sub2 = int(input("Enter the marks of Subject 2 :- "))
sub3 = int(input("Enter the marks of Subject 3 :- "))

total = float(sub1 + sub2 + sub3)
print("Total sums up to :- ",total)
percentage = (total/300)*100
print("Overall Percentage  is :- ",percentage)

if sub1>0 and sub2>0 and sub3>0:
    if percentage>=40 and sub1>=33 and sub2>=33 and sub3>=33:
        print(f" {Student} has been Promoted . Passed Congrats 🥳 ")
    else:
        print(f"{Student} . Status :- Not Passed 😱 !")
else:
    print("Failed 😭 !")


# Ans 3 :-
s1 = "Make a lot of money"
s2 = "buy now"
s3 = "Subscribe this"
s4 = "Click this"

message = input("Enter your comment :- ")

if s1 in message or s2 in message or s3 in message or s4 in message:
    print("Spam detected ⚠️")
else:
    print("Spam not detected as not Present . Congo 🥳")


# Ans 4 :-
username = input("Enter you name :-  ")
count = len(username)
if count>=10:
    print(f"{username} contains more characters :- {count} than 10 ")
else:
    print(f"{username} contains less characters :- {count} than 10")
  

# Ans 5 :-
Data = ["Bridul" , "Sumit Bilagi" , "Ramanath Bhat " , "Jyothi More" , "Raghav"]

friend = input("Enter your friends's name :- ")
if friend in Data:
    print(f"{friend} is present in the list 🥳❤️")
else:
    print(f"{friend} not present in your list 😭 .")


# Ans 6 :- 
marks = int(input("Enter your marks (0 - 100) :-  "))
if marks>=90 and marks<=100:
    print("Grade :- EX")
elif marks>=80 and marks<90:
    print("Grade :- A")
elif marks>=70 and marks<80:
    print("Grade :- B")
elif marks>=60  and marks<70:
    print("Grade :- C")
elif marks>=50 and marks<60:
    print("Grade :- D")
else:
    print("Fail(F)")


# Ans 7:-
post = "Harry Bhai I Love You ❤️🫂, You are a Great Teacher 🙏🫡. Learned a lot From You 😘. You are a inspiration for Me. "

if ("Harry").lower() in post.lower():
    print(" Its talking about Harry ")
else:
    print("No its not talking about Harry")