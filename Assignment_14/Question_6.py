# Write a lambda function which accepts one number and returns True if number is odd otherwise False.

EvenNumber = lambda Value : ((Value % 2) != 0)

def main():
    Result = 0
    No = 0

    No = int(input("Enter the number : "))

    Result = EvenNumber(No)

    print(Result)

if __name__ == "__main__":
    main()