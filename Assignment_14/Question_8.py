# Write a lambda function which accepts two number and returns addition.

Addition = lambda Value1, Value2 : Value1 + Value2 

def main():
    Result = 0
    No1 = 0
    No2 = 0

    No1 = int(input("Enter the first number : "))
    No2 = int(input("Enter the second number : "))

    Result = Addition(No1, No2)

    print("Addition of two number is : ",Result)

if __name__ == "__main__":
    main()