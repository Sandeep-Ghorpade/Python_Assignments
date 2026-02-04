# Design a Python application that creates two threads.
# Thread 1 should compute the sum of elements from a list.
# Thread 2 should compute the product of elements from the same list.
# Return the results to the main thread and display them.

import threading

def Summation(Data):
    Sum = 0
    for i in range(0,len(Data)):
        Sum = Sum + Data[i]
    print("Summation of elements is : ",Sum)
                
def Multiplication(Data):
    Mult = 1
    for i in range(0,len(Data)):
        Mult = Mult * Data[i]
    print("Product of all elements is : ",Mult)       

def main():
    Value = 0
    Size = 0
    Data = list()

    print("Enter the numbers of elements : ")
    Size = int(input())

    print("Enter the elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    t1 = threading.Thread(target = Summation,args = (Data, ))
    t2 = threading.Thread(target = Multiplication,args = (Data, ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
