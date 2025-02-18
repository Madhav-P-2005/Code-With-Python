'''

⭐) Multithreading is a programming technique that enables a program to run multiple threads (smaller units of a process) concurrently. In Python, multithreading allows tasks to run in parallel, enabling more efficient use of resources, especially for I/O-bound operations.

'''


# 🔑 Key Concepts  ? 

'''

1) Thread :-  A lightweight, independent subprocess.

2) Concurrency :-  Running multiple threads "at the same time" (but not simultaneously in CPU-bound tasks due to Python's Global Interpreter Lock (GIL)).
                                                             
3) Parallelism :-  True simultaneous execution on multi-core processors (requires multiprocessing).

'''


# 📚 How Python Handles Threads ? 

'''

💡) Python uses the threading module to create and manage threads. However :-

      a) Python's GIL prevents true parallel execution of threads in CPU-bound tasks. For I/O-bound tasks, multithreading is effective because the GIL is released during I/O operations.

'''



# Example 

import threading
import time
from concurrent.futures import ThreadPoolExecutor


# Indicates some task being done 
def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)


time1 = time.perf_counter()
# Normal Code 
# func(4)
# func(2)
# func(1)

'''

Output :- 
Sleeping for 4 seconds
Sleeping for 2 seconds
Sleeping for 1 seconds
Thread is running

'''

time2 = time.perf_counter()

print("Difference in Time :- ",time2 - time1)       # Output :- Difference in Time :-  7.0035046999691986

# Same code using Threads
t1 = threading.Thread(target=func , args=[4])
t2 = threading.Thread(target=func , args=[2])
t3 = threading.Thread(target=func , args=[1])


t1.start()
t2.start()
t3.start()


# If you want to wait 
t1.join()
t2.join()
t3.join()

time2 = time.perf_counter()

print("Difference in Time :- ",time2 - time1)       # Output :- Difference in Time :-   0.0025108999689109623

'''
Output :- 

Sleeping for 4 seconds
Sleeping for 2 seconds
Sleeping for 1 seconds
Thread is running

'''



def poolingDemo():
    with ThreadPoolExecutor() as executor:
        future1 = executor.submit(func , 3)
        future2 = executor.submit(func , 2)
        future3 = executor.submit(func , 4)
        print(future1.result())
        print(future2.result())
        print(future3.result())


poolingDemo()


'''

Output :- 

Sleeping for 3 seconds
Sleeping for 2 seconds
Sleeping for 4 seconds
None
None
None
Thread is running

'''



# Using Map() 

def poolingDemo():
    with ThreadPoolExecutor() as executor:

        l = [3 , 5 ,1 ,2]
        results = executor.map(func , l)
        for result in results:
            print(result)



poolingDemo() 


'''

Output :- 

Sleeping for 3 seconds
Sleeping for 5 seconds
Sleeping for 1 seconds
Sleeping for 2 seconds
None
None
None
None
Thread is running

'''



# ✅ Threading with Arguments  ?
import threading

def greet(name):
    print(f"Hello, {name}!")               # Output :- Hello, Alice!

# Create a thread with arguments
thread = threading.Thread(target=greet, args=("Alice",))
thread.start()
thread.join()






# ✅ Thread Safety and Locks  :- When multiple threads access shared data, it can cause race conditions. Use locks to synchronize thread access.

import threading

# Shared resource
counter = 0
lock = threading.Lock()

def increment():
    global counter
    with lock:  # Lock acquired
        counter += 1  # Critical section

# Create threads
threads = [threading.Thread(target=increment) for _ in range(10)]

# Start and join threads
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print(f"Final Counter: {counter}")       # Output :- Final Counter: 10




# ✅ Daemon Threads :- Daemon threads run in the background and automatically terminate when the main program exits.

import threading
import time

def background_task():
    while True:
        print("Daemon thread is running")
        time.sleep(1)

# Create a daemon thread
daemon_thread = threading.Thread(target=background_task, daemon=True)
daemon_thread.start()

# Main thread sleeps for 3 seconds
time.sleep(3)
print("Main thread exiting")


'''

Output :- 

Daemon thread is running
Daemon thread is running
Daemon thread is running
Main thread exiting

'''


# ✅ Thread Subclassing :- Threads can also be created by subclassing the Thread class.

import threading

class MyThread(threading.Thread):
    def run(self):
        print(f"Thread {self.name} is running")          # Output :- Thread Thread-1 is running

# Create and start the thread
thread = MyThread()
thread.start()
thread.join()





# ✅ Types of Tasks Best Suited for Multithreading

'''

1️⃣) I/O-bound tasks :- 

              a) File operations

              b) Network requests (e.g., downloading files, web scraping)

              c) Database queries


2️⃣) Not ideal for CPU-bound tasks :-  Heavy computations (e.g., mathematical calculations, data analysis).

⭐ -  For CPU-bound tasks, multiprocessing is better than multithreading.

'''




# ✅ Syntax for Multithreading  :- Using the threading Module 

import threading

# Target function to run in a thread
def my_function():
    print("Thread is running")

# Creating a thread
thread = threading.Thread(target=my_function)

# Starting the thread
thread.start()

# Waiting for the thread to complete
thread.join()





# ✅ How It Works ? 

'''

1️⃣) Create Threads :-  Define tasks (functions) to run as separate threads.

2️⃣) Start Threads :-  Use start() to begin thread execution.

3️⃣) Join Threads :-  Use join() to wait for a thread to finish before proceeding.
    
4️⃣) Thread Safety :-  Use locks or other synchronization mechanisms to prevent data corruption when multiple threads access shared resources.

'''




# ✅ Usage of Multithreading   ?

'''

1️⃣) Web Scraping :- Fetch data from multiple web pages concurrently.

2️⃣) File Operations :- Read/write large files or process multiple files simultaneously.

3️⃣) Network Requests :- Handle multiple API calls or downloads at the same time.

4️⃣) GUI Applications :- Keep the UI responsive while performing background tasks.

'''



# ✅ Advantages of Multithreading ? 

'''

1️⃣) Efficient for I/O-bound tasks :- Threads can operate while waiting for external I/O operations.
    
2️⃣) Better resource utilization :- Can perform multiple tasks concurrently.

3️⃣) Simpler than multiprocessing :- No need to manage multiple processes or inter-process communication.

'''




# ✅ Limitations of Multithreading ? 

'''

1️⃣) GIL limitation :- Prevents true parallel execution for CPU-bound tasks.
    
2️⃣) Complexity :- Debugging multithreaded code can be challenging due to race conditions and deadlocks.

3️⃣) Not ideal for heavy computation :- Use multiprocessing for CPU-intensive tasks

'''