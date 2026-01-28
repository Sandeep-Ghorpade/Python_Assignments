# Write a lambda function which accepts two numbers and returns maximum number.

Maximum = lambda Value1, Value2 : Value1 if Value1 > Value2 else Value2 

def main():
    Result = 0
    No1 = 0
    No2 = 0

    No1 = int(input("Enter the first number : "))
    No2 = int(input("Enter the second number : "))

    Result = Maximum(No1,No2)

    print("Maximum number is : ",Result)

if __name__ == "__main__":
    main()