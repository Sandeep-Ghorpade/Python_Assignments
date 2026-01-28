# Write a lambda function using filter() which accepts a list of numbers and returns the count of even numbers.

EvenCount = lambda No :((No % 2) == 0)

def main():
    Data = [45,7,2,89,4,26,13,98,110,61]
    print("Actual Data is : ",Data)

    FData = list(filter(EvenCount,Data))
    print("Data after filter is : ",FData)

    Count = len(FData)
    print("Count of even numbers are : ",Count)

if __name__ == "__main__":
    main()