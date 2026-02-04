# Write a program which contains one lambda function which accepts two parameter and return its multiplication.
# Input : 4    3   Output : 12
# Input : 6    3   Output : 18

Multiplication = lambda  No1, No2 : No1 * No2

def main():
    Value1 = 0
    Value2 = 0
    Ret = 0

    Value1 = int(input("Enter the first number : "))
    Value2 = int(input("Enter the second number : "))

    Ret = Multiplication(Value1,Value2)

    print("Multiplication of two number is : ",Ret)

if __name__ == "__main__":
    main()