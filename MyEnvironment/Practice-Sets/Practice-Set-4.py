# Ans 1 :- 
fruits = []
# user1 = fruits.append(input("Enter any Fruit Name  :-  "))
# user2 = fruits.append(input("Enter any Fruit Name :-   "))
# user3 = fruits.append(input("Enter any Fruit Names  :-  "))
# user4 = fruits.append(input("Enter any Fruit Names  :-  "))
# user5 = fruits.append(input("Enter any Fruit Names  :-  "))
# user6 = fruits.append(input("Enter any Fruit Names  :-  "))
# print(fruits)


# Ans 2 :-
Students_Data = []
student1 = Students_Data.append(int(input("Enter your marks   :-  ")))
student2 = Students_Data.append(int(input("Enter any marks  :-  ")))
student3 = Students_Data.append(int(input("Enter any marks  :-  ")))
student4 = Students_Data.append(int(input("Enter any marks  :-  ")))
student5 = Students_Data.append(int(input("Enter any marks  :-  ")))
student6 = Students_Data.append(int(input("Enter any marks  :-  ")))

Students_Data.sort()
print("Sorted Data is :- ",Students_Data)


# Ans 3 :- 
tuple  = 1 , 2, 3
tuple[0] = "Madhav"
print(tuple)  # Output :- TypeError: 'tuple' object does not support item assignment

# Ans 4 :- 
list2 = [1,2,3,4,5]
print("sum of numbers :- ",sum(list2))


# Ans 5 :- 
a = (7, 0, 8, 0, 0, 9)
print("No of Occurences of 0 :- ", a.count(0))