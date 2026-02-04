# Design a Python application that creates two threads named Prime and NonPrime.
# Both threads should accept a list of integers.
# The Prime thread should display all prime numbers from the list.
# The NonPrime thread should display all non-prime numbers from the list.

import threading

def Prime(Data):
        print("Prime numbers  are : ")
        for No in Data:
             if(No > 1):
                  for i in range(2,No):
                       if((No % i) == 0):
                            break
                  else:
                       print(No,end = " ")
        print()  # prints blank line             
                    
def NonPrime(Data):
        print("Non prime numbers are : ")
        for No in Data:
            if(No > 1):
                for i in range(2,No):
                    if((No % i) == 0):
                        print(No,end = " ")
                        break
        print()    
                       
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

    t1 = threading.Thread(target = Prime,args = (Data, ))
    t2 = threading.Thread(target = NonPrime,args = (Data, ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
