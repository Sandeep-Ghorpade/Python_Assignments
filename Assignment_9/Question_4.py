# Write a program which accepts one number and prints cube of that number.

def Display(Value):
    Value = Value ** 3
    return(Value)

def main():
    No = 0
    Result = 0

    No = int(input("Enter the number : "))
    Result = Display(No)
    print("Cube of number is :",Result)

if __name__ == "__main__":
    main()