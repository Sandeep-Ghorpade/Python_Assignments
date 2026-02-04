# Design a Python application that creates two threads.
# Thread 1 should calculate and display the maximum element from an list.
# Thread 2 should calculate and display the minimum element from the same list.
# The list should be accepted from the user.

import threading

def Maximum(Data):
        MaxNo = Data[0]
        for i in range(1,len(Data)):
              if(Data[i] > MaxNo):
                    MaxNo = Data[i]
        print("Maximum element is : ",MaxNo) 
              
                
def Minimum(Data):
        MinNo = Data[0]
        for i in range(1,len(Data)):
              if(Data[i] < MinNo):
                    MinNo = Data[i]
        print("Minimum element is : ",MinNo)   

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

    t1 = threading.Thread(target = Maximum,args = (Data, ))
    t2 = threading.Thread(target = Minimum,args = (Data, ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
