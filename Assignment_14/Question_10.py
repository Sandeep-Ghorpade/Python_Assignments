# Write a lambda function which accepts three number and returns largest number.

Largest = lambda Value1, Value2, Value3 : Value1 if Value1 > Value2 and Value1 >Value3 else(Value2 if Value2 > Value1 and Value2 >Value3 else Value3)

def main():
    Result = 0
    No1 = 0
    No2 = 0
    No3 = 0

    No1 = int(input("Enter the first number : "))
    No2 = int(input("Enter the second number : "))
    No3 = int(input("Enter the third number : "))

    Result = Largest(No1,No2,No3)

    print("Largest number is : ",Result)

if __name__ == "__main__":
    main()