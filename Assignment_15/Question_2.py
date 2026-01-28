# Write a lambda function using filter() which accepts a list of numbers and returns a list of even number.

CheckEven = lambda No : ((No % 2) == 0)

def main():
    Data = [45,7,2,89,4,26,72,69,55,13]
    print("Actual Data is : ",Data)

    FData = list(filter(CheckEven,Data))
    print("Data after filter is : ",FData)

if __name__ == "__main__":
    main()