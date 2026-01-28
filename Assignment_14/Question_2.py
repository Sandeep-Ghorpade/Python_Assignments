# Write a lambda function which accepts one number and returns cube of that number.

Cube = lambda Value: Value ** 3 

def main():
    Result = 0
    No = 0
    No = int(input("Enter the number : "))

    Result = Cube(No)

    print("cube of given number is : ",Result)

if __name__ == "__main__":
    main()