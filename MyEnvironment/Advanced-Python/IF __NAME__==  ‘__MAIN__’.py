''' 

The if __name__ == '__main__' construct is a common Python idiom used to define the entry point of a Python script. It ensures that certain blocks of code are executed only when the script is run directly, and not when it is imported as a module into another script.

'''


# How It Works :- 

'''

1) __name__ :- 

    a) Every Python module has a built-in variable called __name__.

    b) When a Python file is run directly, the __name__ variable is set to "__main__".

    c) If the file is imported as a module, __name__ is set to the name of the module (i.e., the filename without the .py extension).


2) Purpose of if __name__ == '__main__' :- 

    a) It allows you to define code that will only execute when the script is run directly.

    b) It prevents certain code from being executed when the file is imported as a module.


'''


# Syntax :- 

if __name__ == '__main__':
    # Code to be executed when the script is run directly
    pass




# Why Use if __name__ == '__main__'  ?

'''

1) Separation of Code :- 

      a) It helps to clearly separate code that should run only during direct execution from reusable components (e.g., functions, classes) that can be imported.

2) Reusability :-

      a) By using this idiom, you can create reusable modules without executing unnecessary code when imported.

3) Testing :- 

      a) Useful for testing scripts by allowing test-specific code to be included in the if __name__ == '__main__' block.


'''



# Note :-   Main.py and Module.py is interlinked to this file . They have a connection . 