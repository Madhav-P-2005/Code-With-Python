'''

⭐) Asynchronous I/O, or async for short, is a programming pattern that allows for high-performance I/O operations in a concurrent and non-blocking manner. In Python, async programming is achieved through the use of the asyncio module and asynchronous functions.

'''



'''

💡) Async IO is a powerful programming pattern that allows for high-performance and concurrent I/O operations in Python. With the asyncio module and asynchronous functions, you can write efficient and scalable code that can handle large amounts of data and I/O operations without blocking the main thread. Whether you're working on web applications, network services, or data processing pipelines, async IO is an essential tool for any Python developer.

'''



import time

import asyncio

# def function1():
#     time.sleep(3)
#     print("Function 1")

# def function2():
#     time.sleep(3)
#     print("Function 2")


# def function3():
#     time.sleep(3)
#     print("Function 3")


# function1()
# function2()
# function3()

'''

Output :- 

Function 1                                              
Function 2       
Function 3

'''




async def function1():
        await asyncio.sleep(1)
        print("Function 1")
        return "Madhav"

async def function2():
        await asyncio.sleep(1)
        print("Function 2")


async def function3():
        await asyncio.sleep(4)
        print("Function 3")



# async def main():
#       task = asyncio.create_task(function1())
#     #   await function1()
#       await function2()
#       await function3()


# asyncio.run(main())


'''

Output :- 

Function 2
Function 1
Function 3

'''




async def main():
        L = await asyncio.gather(
                function1(),
                function2(),
                function3(),
        )
        print(L)



asyncio.run(main())


'''

Output :- 

Function 1
Function 2
Function 3
['Madhav', None, None]

'''