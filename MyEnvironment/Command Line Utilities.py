# 🛠️ Command-Line Utilities in Python


'''

⭐) Command-Line Utilities (CLIs) are tools that allow users to interact with a program via text-based commands in a terminal or command prompt. Python provides powerful tools and libraries to create such utilities, making it an excellent choice for building command-line interfaces.

'''


# ✅ Key Features of Command-Line Utilities

'''

1️⃣) Command Parsing :- Handle user-provided commands and arguments efficiently.

2️⃣) Options and Flags :-  Support switches (like -h, --help, --verbose) for better user interaction.

3️⃣) Dynamic Inputs :-  Accept arguments like file paths, configurations, or any data directly from the terminal.

4️⃣) Custom Commands :- Execute specific tasks based on the command provided.

'''



# 📚 How to Create Command-Line Utilities in Python   


["Note :- Python provides several modules and libraries for building CLIs. Here are the most common approaches  :- "]



# 1️⃣ Using sys.argv :- The sys module allows you to access command-line arguments through the argv list.


# Syntax :-

import sys
print(sys.argv)


# Example :- 
import sys

if len(sys.argv) < 2:
    print("Usage: python script.py <name>")
else:
    name = sys.argv[1]
    print(f"Hello, {name}!")


'''
Output :- Usage: python script.py <name>

'''




# 2️⃣ Using argparse  :- A more robust way to handle arguments and options.



# Syntax :- 
import argparse

parser = argparse.ArgumentParser(description="Your program description")
parser.add_argument("name", help="Your name")
args = parser.parse_args()
print(f"Hello, {args.name}!")



# Example :- 
import argparse

parser = argparse.ArgumentParser(description="Greet the user.")
parser.add_argument("name", help="Name of the user")
parser.add_argument("--age", type=int, help="Age of the user", required=False)

args = parser.parse_args()

print(f"Hello, {args.name}!")
if args.age:
    print(f"Your age is {args.age}.")


'''

Output :- 

usage: main.py [-h] [--age AGE] name
main.py: error: the following arguments are required: name

'''



# 3️⃣ Using click (Third-party Library)  :- click is a popular library for building CLIs with minimal boilerplate.


# Installation :- pip install click


# Syntax :- 
import click # type: ignore

@click.command()
@click.argument("name")
def greet(name):
    click.echo(f"Hello, {name}!")

if __name__ == "__main__":
    greet()



# Example :- 
import click # type: ignore

@click.command()
@click.argument("name")
@click.option("--age", default=0, help="Your age")
def greet(name, age):
    click.echo(f"Hello, {name}!")
    if age > 0:
        click.echo(f"You are {age} years old.")

if __name__ == "__main__":
    greet()




# 4️⃣ Using typer (Third-party Library) :- typer is a modern and easy-to-use library based on Python's type hints.


# Installation :- pip install typer


# Syntax :- 
import typer # type: ignore

def greet(name: str):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    typer.run(greet)




# Example :- 
import typer # type: ignore

def greet(name: str, age: int = 0):
    print(f"Hello, {name}!")
    if age > 0:
        print(f"Your age is {age}.")

if __name__ == "__main__":
    typer.run(greet)




# Need to explore on this topic ....