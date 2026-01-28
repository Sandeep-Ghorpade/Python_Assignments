# Write a lambda function which accepts one number and returns True if number is divisible by 5.

Divisible = lambda Value : ((Value % 5) == 0)

def main():
    Result = 0
    No = 0

    No = int(input("Enter the number : "))

    Result = Divisible(No)

    print(Result)

if __name__ == "__main__":
    main()