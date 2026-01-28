# Write a program which contains one function ChkGreater() that accepts two numbers and prints the greater number. 

def ChkGreater(Value1,Value2):
    Ans = 0

    if(Value1 > Value2):
        Ans = Value1
    else:
        Ans = Value2

    return(Ans)

def main():
    No1 = 0
    No2 = 0
    Result = 0

    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    Result = ChkGreater(No1,No2)
    print("Greater number is : ",Result)

if __name__ == "__main__":
    main()