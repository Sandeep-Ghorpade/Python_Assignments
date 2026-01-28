# Write a program which accept nummber from user and checks whether that number is positive or negative or zero.

def ChkNum(Value):
    if(Value > 0):
        print("Positive number")
    elif(Value < 0):
        print("Negative number")
    else:
        print("Number is zero")

def main():
    No = 0

    No = int(input("Enter the number : "))

    ChkNum(No)

if __name__ == "__main__":
    main()