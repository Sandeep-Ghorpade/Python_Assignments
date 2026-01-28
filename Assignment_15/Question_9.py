# Write a lambda function using reduce() which accepts a list of numbers and returns a list of numbers and returns the product of all elements.

from functools import reduce

Product = lambda No1, No2 : No1 * No2

def main():
    Data = [45,7,2,89,4,26,13]
    print("Actual Data is : ",Data)

    RData = reduce(Product,Data)
    print("Data after reduce is : ",RData)

if __name__ == "__main__":
    main()