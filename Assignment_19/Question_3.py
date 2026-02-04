# Write a program which contains filter(), map() and reduce() in it. 
# Python application which contains one list of numbers. List contains the numbers which are accepted from user.
# Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90.
# Map function will increase each number by 10. Reduce will return product of all that numbers.

# Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
# List after filter = [76, 89, 86, 90, 70]
# List after map = [86, 99, 96, 100, 80]
# Output of reduce = 6538752000

from functools import reduce

Display = lambda No : 70 <= No <= 90

Increment = lambda No : No + 10

Mult = lambda No1, No2 : No1 * No2

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

    FData = list(filter(Display,Data))
    print("Data after filter is : ",FData)

    MData = list(map(Increment,FData))
    print("Data after map is : ",MData)

    RData = reduce(Mult,MData)
    print("Data after reduce is : ",RData)

if __name__ == "__main__":
    main()
