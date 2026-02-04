# Design a Python application that creates two separate threads named Even and Odd.
# The Even thread should display the first 10 even numbers.
# The Odd thread should display the first 10 odd numbers.
# Both threads should execute independently using the threading module.
# Ensure proper thread creation and execution.

import threading

def Even(No):
    for i in range(2,No+1,2):
        print("Even numbers are : ",i)
        
def Odd(No):
    for i in range(1,No+1,2):
        print("Odd numbers are : ",i)
        
def main():
    t1 = threading.Thread(target=Even,args = (20,))
    t2 = threading.Thread(target=Odd,args = (20,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()