# Write a program which contains filter(), map() and reduce() in it. 
# Python application which contains one list of numbers. List contains the numbers which are accepted from user.
# Filter should filter out all such numbers which are even.
# Map function will calculate its square.
# Reduce will return addition of all that numbers.

# Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
# List after filter = [2, 4, 4, 2, 8, 10]
# List after map = [4, 16, 16, 4, 64, 100]
# Output of reduce = 204

from functools import reduce

Even = lambda No : ((No % 2) == 0)

Square = lambda No : No ** 2

Add = lambda No1, No2 : No1 + No2

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

    FData = list(filter(Even,Data))
    print("Data after filter is : ",FData)

    MData = list(map(Square,FData))
    print("Data after map is : ",MData)

    RData = reduce(Add,MData)
    print("Data after reduce is : ",RData)

if __name__ == "__main__":
    main()
