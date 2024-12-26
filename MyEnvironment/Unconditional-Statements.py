# 1) break :- It is a keyword which is used to terminate the loop from the block . General Usage: Mostly used within loops to terminate the iteration based on a condition.

for i in range(10):
    if i == 5:
        break  # Exits the loop when i is 5
    print(i)
# Output :- 0 1 2 3 4 


# 2) continue :- Skips the rest of the code inside the current loop iteration and jumps to the next iteration. General Usage: Used within loops to skip over certain conditions without terminating the loop.

for i in range(5):
    if i == 2:
        continue  # Skips the iteration when i is 2
    print(i)
# Output: 0 1 3 4


# 3) pass :- A null operation; it does nothing and is used as a placeholder. General Usage: Used when a statement is syntactically required but no code needs to be executed.

for i in range(645):
    pass   # Placeholder for future implementation

i = 0
while(i<45):
    print(i)
    i+=1



# 4) return :- Exits a function and optionally returns a value to the caller. General Usage: Used in functions to end execution and return a result to the calling code.

def add(a, b):
    return a + b  # Returns the sum of a and b

result = add(5, 3)
print(result)
# Output: 8


# 5) exit() and sys.exit() :- 

# exit() :- the exit() function is used to terminate the execution of the program. It is particularly intended for interactive use, such as in the Python interpreter . exit() is part of the site module and is meant for use in the Python interactive shell (REPL). It provides a convenient way to exit the interpreter.

'''
>>> print("Hello, World!")
Hello, World!
>>> exit()

'''
# Exits the Python interpreter


# sys.exit() :- sys.exit() is part of the sys module and is used to terminate the execution of a Python script. It raises a SystemExit exception, which can be caught in an exception block if needed .

# syntax :-    # import sys
               # sys.exit([arg])

# Example :- 
import sys
sys.exit()  # Exits the script

print("This will not be printed.")
# No output, as the script is terminated


# 6) assert() :-  Used for debugging purposes. Tests a condition and raises an AssertionError if the condition is false. Usage: Ensures that conditions expected to be true actually hold at specific points in the code.

x = 5
assert x <= 0, "x should be positive"  # No error if x > 0

# If x <= 0, raises AssertionError with the message "x should be positive"
