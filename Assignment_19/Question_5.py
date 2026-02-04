# Write a program which contains filter(), map() and reduce() in it. 
# Python application which contains one list of numbers. List contains the numbers which are accepted from user.
# Filter should filter out all prime numbers. 
# Map function will multiply each number by 2.
# Reduce will return Maximum number from that numbers. (You can also use normal functions instead of lambda functions).

# Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
# List after filter = [2, 11, 17, 23, 31]
# List after map = [4, 22, 34, 46, 62]
# Output of reduce = 62

from functools import reduce

def Prime(No):
    if(No > 1):
        for i in range(2,No):
            if((No % i) == 0):
                break
        else:
            return No
    else:
         return -1

Mult = lambda No : No * 2

Max = lambda No1, No2 : No1 if No1 > No2 else No2

def main():
    Data = list()
    Size = 0
    Value = 0

    print("Enter the number of elements : ")
    Size = int(input())

    print("Enter the elements")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    FData = list(filter(Prime,Data))
    print("Data after filter is : ",FData)

    MData = list(map(Mult,FData))
    print("Data after map is : ",MData)

    RData = reduce(Max,MData)
    print("Data after reduce is : ",RData)

if __name__ == "__main__":
    main()
