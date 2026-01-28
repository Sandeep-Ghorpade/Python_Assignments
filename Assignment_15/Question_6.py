# Write a lambda function using reduce() which accepts a list of numbers and returns the minimum element.

from functools import reduce

Minimum = lambda No1,No2 : No1 if No1 < No2 else No2

def main():
    Data = [45,7,2,89,4,26,72,69,55,13]
    print("Actual Data is : ",Data)

    RData = reduce(Minimum,Data)
    print("Data after reduce is : ",RData)

if __name__ == "__main__":
    main()