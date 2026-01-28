# Write a program which contains one function named as ChkNum() which accept one parameter as number . if number is even then it should display "Even number" otherwise display "Odd number" on console.

def ChkNum(Value):
    if((Value % 2) == 0):
        print("Even number")
    else:
        print("Odd number")

def main():
    No = 0

    No = int(input("Enter the number : "))

    ChkNum(No)

if __name__ == "__main__":
    main()