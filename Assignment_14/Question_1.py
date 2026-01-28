# Write a lambda function which accepts one number and returns square of that number.

Square = lambda Value: Value ** 2

def main():
    Result = 0
    No = 0
    No = int(input("Enter the number : "))

    Result = Square(No)

    print("Square of given number is : ",Result)

if __name__ == "__main__":
    main()