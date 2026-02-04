# Design a Python application that creates two threads named EvenList and OddList.
# Both threads should accept a list of integers as input.
# The EvenList thread should:
#       Extract all even elements from the list.
#       Calculate and display their sum.
# The OddList thread should:
#       Extract all odd elements from the list.
#       Calculate and display their sum.
# Threads should run concurrently. 

import threading

def EvenList(Data):
    EvenSum = 0
    for i in Data:
        if((i % 2) == 0):
            print(i, end = " ")
            EvenSum = EvenSum + i
    print("Sum of even numbers is : ",EvenSum)
        
def OddList(Data):
    OddSum = 0
    for i in Data:
        if((i % 2) != 0):
            print(i, end = " ")
            OddSum = OddSum + i
    print("Sum of odd number is : ",OddSum)
        
def main():
    Value = 0
    Size = 0
    Data = list()

    print("Enter the number of elements : ")
    Size = int(input())

    print("Enter the elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    t1 = threading.Thread(target=EvenList,args = (Data,))
    t2 = threading.Thread(target=OddList,args = (Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()