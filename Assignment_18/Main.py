# Write a program which accept N numbers from user and store it into List.
# Return addition of all prime numbers from that List.
# Main python file accepts N numbers from user and pass each number to ChkPrime() function which is part of our user defined module named as MarvellousNum. 
# Name of the function from main python file should be ListPrime().

import MarvellousNum

print("Inside Main",__name__)

def ListPrime(Data):
    Result = 0
    Ret = 0

    for No in Data:
        Ret = MarvellousNum.ChkPrime(No)

        if(Ret != -1):
            Result = Result + Ret

    print("Addition of all prime numbers is : ",Result)

def main():
    Size = 0
    Value = 0
    Data = list()

    print("Enter the numbers of elements : ")
    Size = int(input())

    print("Enter the elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    ListPrime(Data)

if __name__ == "__main__":
    main()