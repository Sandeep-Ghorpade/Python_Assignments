# Write a program which accepts one number and prints square of that numbers of that number.

def Display(Value):
    Value = Value ** 2
    return(Value)

def main():
    No = 0
    Result = 0

    No = int(input("Enter the number : "))
    Result = Display(No)
    print("Square of number is :",Result)

if __name__ == "__main__":
    main()