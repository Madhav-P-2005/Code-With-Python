# Parenthesized Context Managers :- A parenthesized context manager allows you to group multiple context managers in parentheses for improved readability and to span multiple lines when using the with statement.


# When Was It Released ?

'''

   ●) Parenthesized context managers were introduced in Python 3.10, released on October 4, 2021.

   ●) It was part of PEP 634, which focused on structural pattern matching, but the syntax for context managers also benefited from the enhanced parenthesized grouping.

'''

# Syntax :-   The syntax uses parentheses () to group multiple context managers

'''

with (
    context_manager1 as resource1,
    context_manager2 as resource2
):
    # Code block where resources are used

'''

# How It Works :- 

'''

 ●) The __enter__() method of each context manager is called when entering the with block.
 ●) The __exit__() method of each context manager is called in reverse order when exiting the with block.
 ●) This ensures that resources are properly cleaned up, even if exceptions occur during the execution of the block.

'''

# f = open(r"E:\Python Tutorial - Code With Harry\MyEnvironment\Files\Parenthesized Context Manager.txt" , 'r')
# f.close()
with( 
        open(r"E:\Python Tutorial - Code With Harry\MyEnvironment\Files\this.txt" , 'r',encoding="utf-8") as f1,
        open(r"E:\Python Tutorial - Code With Harry\MyEnvironment\Files\Parenthesized Context Manager.txt" , 'w',  encoding="utf-8") as f2
):
        content = f1.read()
        f2.write(content)