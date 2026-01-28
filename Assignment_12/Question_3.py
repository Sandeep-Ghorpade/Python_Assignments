# Write a program which accepts two numbers and prints addition,substraction,multiplication,and division.

def Display(Value1,Value2):
    Ans = 0
    Ans = Value1 + Value2 
    print("Addition of two number is : ",Ans)

    Ans = Value1 - Value2
    print("Substraction of two number is : ",Ans)

    Ans = Value1 * Value2
    print("Multiplication of two number is : ",Ans)

    Ans = Value1 / Value2
    print("Division of two number is : ",Ans)    

def main():
    No1 = 0
    No2 = 0

    No1 = int(input("Enter the first number : "))
    No2 = int(input("Enter the second number : "))

    Display(No1,No2)

if __name__ == "__main__":
    main()