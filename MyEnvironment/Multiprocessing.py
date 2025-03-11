'''

⭐) Multiprocessing in Python allows a program to execute multiple processes simultaneously, leveraging multiple CPU cores for true parallelism. Unlike multithreading, multiprocessing is ideal for CPU-bound tasks because each process runs independently with its own memory space.

'''


# 🔑 Key Concepts  ? 

'''

1️⃣) Process :-  An independent execution unit with its own memory and resources.

2️⃣) Parallelism :-  True simultaneous execution on multi-core processors.

3️⃣) Global Interpreter Lock (GIL) :-  Unlike threads, processes in Python are not affected by the GIL, enabling true parallelism for CPU-bound tasks.
    
'''





# ✅ When to Use Multiprocessing ? 

'''

1) Best for CPU-bound tasks :- 

    a) Heavy computations like mathematical calculations, data analysis, or machine learning.

    b) Parallelizing large data processing.

    
2) Not ideal for I/O-bound tasks :- 

    a) Use multithreading for tasks involving waiting (e.g., file operations, network requests).

'''





# ✅ How It Works  ? 

'''

💡) The multiprocessing module in Python enables the creation of multiple processes. These processes run independently, and communication between them is achieved using pipes or queues.


1) Target Function :-  Define the function you want the process to execute.

2) Process Creation :-  Use multiprocessing.Process to create a new process.

3) Start the Process :-  Call start() to begin execution.

4) Join the Process :-  Use join() to wait for the process to complete before continuing.

'''


import multiprocessing  as mp

import time 

import math


results_a = []
results_b = []
results_c = []


def make_calculation_one(numbers):
    for number in numbers:
        results_a.append(math.sqrt(number ** 3))


def make_calculation_two(numbers):
    for number in numbers:
        results_a.append(math.sqrt(number ** 4))


def make_calculation_three(numbers):
    for number in numbers:
        results_a.append(math.sqrt(number ** 5))



# this is must if you are doing multiprocessing 
if __name__ == '__main__':
    number_list = list(range(1000000))

    p1 = mp.Process(target=make_calculation_one , args=(number_list, ))
                    
    p2 = mp.Process(target=make_calculation_two , args=(number_list, ))
                    
    p3 = mp.Process(target=make_calculation_three, args=(number_list, ))
                    

    start = time.time()
    p1.start()
    p2.start()
    p3.start()

    end  = time.time()

    make_calculation_one(number_list)

    make_calculation_two(number_list)

    make_calculation_three(number_list)

    end = time.time()

    print(end-start)


["Note :- Need to explore more..... "]