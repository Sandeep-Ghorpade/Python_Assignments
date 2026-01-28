# Write a program which contains one function named as Add() which accept two numbers from user and return addition of that two numbers.

def Add(Value1,Value2):
    Ans = 0
    Ans = Value1 + Value2
    print("Addition of two numbers is :",Ans)

def main():
    No1 = 0
    No2 = 0

    No1 = int(input("Enter the first number : "))
    No2 = int(input("Enter the second number : "))

    Add(No1,No2)

if __name__ == "__main__":
    main()