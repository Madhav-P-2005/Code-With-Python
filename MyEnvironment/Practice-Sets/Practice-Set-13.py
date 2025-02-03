# Ans 1 :- 

#  Using Power Shell  another way is :-  virtualenv env1

#  python  -m  venv  myEnvironment


# pip install pandas




# Ans 2 :- 

name = input("Enter your name ? :- ")
marks = int(input("Enter your Marks ? :- "))
phoneno = int(input("Enter your Phone No  ? :- "))


String = "The name of the student is {0} his marks are {1} and phone number is {2}".format(name,marks,phoneno)


print(String)        # Output :-   The name of the student is Madhav his marks are 100 and phone number is 9283783874




# Ans 3 :- 

Multiply = [str(7*i) for i in range(1,11)]
# print(String)

Vertical_String = "\n".join(Multiply)

print(Vertical_String)

'''

Output :- 

7
14
21
28
35
42
49
56
63
70

'''




# Ans 4 :-
List = []
n = int(input("Enter your size of the list :- "))        
print(f"Enter your {n} of elements are :-   ") 
for i in range(n):
    data = int(input())
    List.append(data)  

def Divisible(num):
 if num%5==0:
     return True

                 
final = filter(Divisible , List)
convert  = list(final)
print(convert)


'''

Output :- 

Enter your size of the list :- 5 
Enter your 5 of elements are :-   
23
5
15
55
99
[5, 15, 55]


'''




# Ans 5 :- 
from functools import reduce

List = []
n = int(input("Enter your size of the list :- "))        
print(f"Enter your {n} of elements are :-   ") 
for i in range(n):
    data = int(input())
    List.append(data)  
    

def Maximum(num , Max=0):
    if num>Max:
        Max=num
        return Max
    else:
        return Max
        
       
final = reduce(Maximum, List)
print("Maximum element the List is :- ",final)


'''

Output :- 

Enter your size of the list :- 5
Enter your 5 of elements are :-   
123
10000
5
6
100
Maximum element the List is :-  10000


'''


# Ans 6 :- 

'''

pip freeze > requirements.txt 

virtualenv harryenv

.harryenv\Scripts\activate.ps1

pip install -r .requirements.txt

'''





# Ans 7 :- 
'''
pip freeze > requirements.txt 
virtualenv harryenv



pip install flask 


from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
    
'''



'''

Output :- 

Hello, World!

'''