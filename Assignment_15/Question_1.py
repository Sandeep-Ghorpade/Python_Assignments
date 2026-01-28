# Write a lambda function using map() which accepts a list of numbers and returns a list of square of each number.

Square = lambda No : No ** 2

def main():
    Data = [45,7,2,89,4,26,72,69,55,13]
    print("Actual Data is : ",Data)

    MData = list(map(Square,Data))
    print("Data after map is : ",MData)

if __name__ == "__main__":
    main()