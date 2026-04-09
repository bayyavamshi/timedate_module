import time

# def task1():
#     print("Task 1 started")
#     time.sleep(2)  # simulating a long-running task
#     print("Task 1 finished")

# def task2():
#     print("Task 2 started")
#     time.sleep(2)
#     print("Task 2 finished")

# task1()
# task2()
import time
import threading
# def vamshi():
#     print('threading started')
#     time.sleep(3)
#     print('hii vamshi')
# vamshi()
import time
import threading
import asyncio
async def task1():
    print('vamsi 1')
    # await asyncio.sleep(3)
    time.sleep(3)
    print('vamshi 2')
async def task2():
    print('vamshi3')
    # await asyncio.sleep(3)
    time.sleep(3)
    print('vamshi 4')
async def main():
    await asyncio.gather(task1(),task2())
asyncio.run(main())
# import time
# import asyncio
# import os
# async def task1():
#     print(os.getpid())
#     print("Task 1 started")
#     await asyncio.sleep(3)
#     print("Task 1 finished")

# async def task2():
#     print(os.getpid())
#     print("Task 2 started")
#     await asyncio.sleep(5)
#     print("Task 2 finished")
# async def main():
#     await asyncio.gather(task1(),task2())
# asyncio.run(main())

# import threading
# import time
# import os
# def task1(name):
#     print(os.getpid())
#     print(f'{name}is started')
#     time.sleep(2)
#     print(f'{name}is finished')
# t1=threading.Thread(target=task1,args=('vamshi',))

# t2=threading.Thread(target=task1,args=('vamshi',))
# t1.start()
# t2.start()


# t1.join()
# t2.join()
# import time

# def square_numbers():
#     for i in range(5):
#         print(i * i)
#         time.sleep(1)

# start = time.time()
# square_numbers()
# square_numbers()
# end = time.time()


# print("Total time:", end - start)


# import multiprocessing
# import time
# import os
# def square_numbers():
#     for i in range(5):
#         print(i * i)
#         time.sleep(1)
#         print(os.getpid())
# if __name__ == "__main__":
#     start = time.time()
    
#     p1 = multiprocessing.Process(target=square_numbers)
#     p2 = multiprocessing.Process(target=square_numbers)
    
#     p1.start()
#     p2.start()
    
#     p1.join()
#     p2.join()
    
#     end = time.time()
#     print("Total time:", end - start)
