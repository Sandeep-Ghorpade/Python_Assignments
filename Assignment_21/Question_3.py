# Design a Python application where multiple threads update a shared variable.
# Use a Lock to avoid race conditions.
# Each thread should increment the shared counter multiple times.
# Display the final value of the counter after all threads complete execution.

import threading
from threading import Lock

Counter = 0

def Increment():
    global Counter
    Counter = Counter + 1
    print("Increment is happen",Counter)

def ThreadWork(lock):
    for i in range(100):
        lock.acquire()
        Increment()
        lock.release()

def main():
    lock = threading.Lock() # lock object is created

    t1 = threading.Thread(target = ThreadWork,args = (lock, ))
    t2 = threading.Thread(target = ThreadWork,args = (lock, ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Final value of counter is : ",Counter)

if __name__ == "__main__":
    main()
