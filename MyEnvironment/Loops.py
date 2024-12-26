# Types of Loops :- 
''' 
1) Entry-Controlled Loops :- In an entry-controlled loop, the condition is evaluated before the loop's body is executed. This means that if the condition is false from the beginning, the loop's body will not execute even once. Examples :- a) For Loop b) While Loop

    
    a) For Loop :- A for loop in Python is a control flow statement used to iterate over a sequence (such as a list, tuple, dictionary, set, or string) and execute a block of code for each item in the sequence. It is commonly used when you know the number of iterations ahead of time, such as when iterating over a fixed list of elements.

    Example:- 
    # Using a for loop to iterate over a list
    numbers = [1, 2, 3, 4, 5]

    print("Using for loop:")
    for num in numbers:
              print(f"The number is {num}")

    
    b) While Loop :- A while loop in Python is a control flow statement that allows code to be executed repeatedly based on a given Boolean condition. The loop runs as long as the condition is True, and it stops running when the condition becomes False.

    Example :- 
    # Initializing a variable
    count = 0

    # Using a while loop
    while count < 5:
    print(f"The count is {count}")
    count += 1  # Incrementing the variable

    print("Loop finished.")


2) Exit-Controlled Loops :- In an exit-controlled loop, the condition is evaluated after the loop's body has been executed. This ensures that the loop's body is executed at least once, regardless of whether the condition is true or false at the start. Example :- do-while
 

    a) Do-while Loops :- Python does not have a built-in exit-controlled loop like the do-while loop found in some other programming languages (e.g., C, Java). However, similar behavior can be simulated using a while loop with a break condition inside.

    Example :- 
    count = 0
    while True:
        print(f"The count is {count}")
        count += 1
        if count >= 5:
               break


'''
print(1)
print(2)
print(3)
print(4)
print(5)
print() 

for i in range(1, 6):
    print(i,end=' ') # Output :- 1 2 3 4 5 
print()


# While - Loop :- 
i=1

while(i<6):
    print(i , end=' ')
    i+=1
print()


# Quiz ans 1:- 
i = 1
while(i<51):
    print(i)
    i+=1
print()


# Quiz ans 2 :-
l = [1, "Bridul" , "Shree Priya" , True , 34.56, "Raghav" , "Sumit Bilagi"]
i=0
while i<len(l):
    print(l[i])
    i+=1



# For Loop :-
'''
range: Represents a sequence of numbers. The range() function can take a maximum of three arguments:
syntax :- range(start, stop, step) . 
The start and step parameters in range() are optional.

'''

for i in range(4):
    print(i)
print()


# for loop in List :- 
l = [1 , 4, 6 , 234 , 6 , 764]
for i in l:
    print(i , end= ' ')
print()

# for loop in Tuple :-
t = (6 , 231 , 75 ,75 ,122)
for i in t:
    print(i, end= ' ')
print()

# for loop in String :- 
s = "Harry"
for i in s:
    print(i)


# For Loop with Else :- 
l = [1 , 7 ,8]

for item in l:print(item)

else: print("done") # this is printed when the loop exhausts ! 
