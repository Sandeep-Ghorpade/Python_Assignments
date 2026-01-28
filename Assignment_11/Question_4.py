# Write a program which accepts one number and prints reverse of that number.

def Display(Value):
    Digit = 0
    Reverse = 0

    while(Value != 0):
        Digit = Value % 10
        Reverse = Reverse * 10 + Digit
        Value = Value // 10

    return(Reverse)
    
def main():
    No = 0
    Result = 0

    No = int(input("Enter the number : "))

    Result = Display(No)

    print("Reverse of the number is : ",Result)

if __name__ == "__main__":
    main()
  