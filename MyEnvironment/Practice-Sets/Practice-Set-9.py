# Ans 1 :- 
with open("E:\Python Tutorial - Code With Harry\MyEnvironment\Files\poems.txt" , "w") as f:
    f.write("twinkle")

with open("E:\Python Tutorial - Code With Harry\MyEnvironment\Files\poems.txt", 'r') as f:
    if(f.readline() == "twinkle"):
        print("Word \"twinkle\" is Present ")
    else:
        print("Word \"twinkle\" is not Present")



# Ans 2 :-
import random
def game():
    print("You are playing the Game ..... ")
    score  = random.randint(1,100)

    # Fetch the Hi - Score 
    with open("E:\Python Tutorial - Code With Harry\MyEnvironment\Files\hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore!=""):
            hiscore = int(hiscore)
        else:
            hiscore=0
        
    print(f"Your score :  {score}")

    if(score>hiscore or hiscore==""):
         # Write this hiscore to the file 
         with open("E:\Python Tutorial - Code With Harry\MyEnvironment\Files\hiscore.txt" , "w") as f:
             f.write(str(score))


    return score

game()



# Ans 3 :- 
def Tables(n):
    table = ""
    for i in range(1, 11):
        result = n * i
        table += f"{n} * {i} = {result}\n"
        i+=1

    with open(f"E:\Python Tutorial - Code With Harry\MyEnvironment\Files/table_Of_{n}.txt", "w") as f:
        f.write(table)


for i in range(2,21):
       Tables(i)




# Ans 4 :- 
with open("E:\Python Tutorial - Code With Harry\MyEnvironment\Files\Donkey.txt" , "w") as f:
        f.write("Donkey is a good animal . It is a kind animal . The most hardworking animal it is ! # SafeDonkey\n")
            
# # Read the Contents of the file :- 
with open(r"E:\Python Tutorial - Code With Harry\MyEnvironment\Files\Donkey.txt" , "r") as f:
            lines = f.readlines()
            print(lines)

with open(r"E:\Python Tutorial - Code With Harry\MyEnvironment\Files\Donkey.txt" , "w") as f:
 for line in lines:
    if  "Donkey" in line:
            f.write(line.replace("Donkey" , "#####"))
    else:
            f.write(line)



# Ans 5 :- 
# Read the Contents of the file :- 
words=["possessions" , "essential" , "demonstrates" , "groceries"]
  
with open(r"E:\Python Tutorial - Code With Harry\MyEnvironment\Files\Words-Q5.txt" , "r") as f:
            lines = f.readlines()
            print(lines)

with open(r"E:\Python Tutorial - Code With Harry\MyEnvironment\Files\Words-Q5.txt" , "w") as f: 
 for line in lines:
       for word in words:
              if word in line:
                line = line.replace(word , "#####")
       f.write(line)



# Ans 6 :- 
with open(r"E:\Python Tutorial - Code With Harry\MyEnvironment\Files\log.txt" , "r") as f:
    lines = f.readline()
    print(lines , end="")
    print()

word = "Python"
with open(r"E:\Python Tutorial - Code With Harry\MyEnvironment\Files\log.txt" , "r") as f:
        if word in lines:
            print(f"{word} is present ") 
        else:
            print(f"{word} is  not present")



# Ans 7 :- 
with open(r"E:\Python Tutorial - Code With Harry\MyEnvironment\Files\log.txt" , "r") as f:
     lines = f.readlines()

line_no = 1
for line in lines:
     if word in line:
        print(f"{word} is present  and Line_Number :- {line_no}") 
        break
     line_no+=1

else:
    print("No Python is not present")
       


# Ans 8 :- 
# Reading the content with UTF-8 encoding
with open(r"E:\Python Tutorial - Code With Harry\MyEnvironment\Files\this.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Writing the content with UTF-8 encoding
with open(r"E:\Python Tutorial - Code With Harry\MyEnvironment\Files\this_copy.txt", "w", encoding="utf-8") as f:
    f.write(content)

print("Content copied successfully.")



# Ans 9 :- 
with open(r"E:\Python Tutorial - Code With Harry\MyEnvironment\Files\this.txt", "r", encoding="utf-8") as f:
    with open(r"E:\Python Tutorial - Code With Harry\MyEnvironment\Files\this_copy.txt", "r", encoding="utf-8") as s:
        if f.readlines() == s.readlines():
            print("Both the files are Indentical")
        else:
            print("Both files are different ")



# Ans 10 :- 
with open(r"E:\Python Tutorial - Code With Harry\MyEnvironment\Files\this.txt", "r", encoding="utf-8") as f:
    f.write()



# Ans 11 :-
with open(r"E:\Python Tutorial - Code With Harry\MyEnvironment\Files\Old.txt", "r", encoding="utf-8") as f:
    content = f.read()

with open(r"E:\Python Tutorial - Code With Harry\MyEnvironment\Files\renamed_by_python.txt", "w", encoding="utf-8") as f:
    f.write(content)



