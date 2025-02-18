# def myfunc():
#     print("Hello World ")


# myfunc()
# print(__name__)


# if __name__ == "__main__":
#     # If this code is directly executed by running the file its present in 
#     print("We are directly running this code")
#     myfunc()
#     print(__name__)     # Output :- __main__

'''

Output :- 

We are directly running this code
Hello World 
__main__


'''




# Without IF__Name__ == "__main__"
def Welcome():
    print("This statement is from Module.py file")


# Welcome()


'''

Output :- 

>>> python MyEnvironment/Advanced-Python/Module.py

This statement is from Module.py file


'''


# Using IF __NAME__ == __MAIN__   ?

print(__name__)

if __name__ == "__main__":
    Welcome()