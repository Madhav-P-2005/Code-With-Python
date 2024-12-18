# Ans 1 :- 
user = input("Enter the user Name : - ")
print("Good Afternoon,",user)

date = input("Enter any Date : - ")
print("Date is ,",date)


# Ans 2:- 
letter =     f'''  
       Dear {user}, 
       You are selected! 
       {date} 
       '''
print(letter)

print()


letter =   '''  
       Dear <|Name|>, 
       You are selected! 
       <|Date|> 
       '''
print(letter.replace("<|Name|>" , "Madhav").replace("<|Date|>" , "15-12-2024"))


# Ans 3 :- 
str = "Madhav  is  a  bad  Boy "
print(str.find(" ")) 



# Ans 4 :- 
print(str.replace("  "," "))

print(str)  # Strings are immutable which means that you cannot change them by running functions on them .

# Ans 5:-
letter = "Dear Harry, \n \t this python course is nice. \nThanks!" 
print(letter)