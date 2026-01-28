# Write a program which accepts one number and checks wheather it is palindrome or not.

def Display(Value):
    Digit = 0
    Reverse = 0
    Original = Value

    while(Value != 0):
        Digit = Value % 10
        Reverse = Reverse * 10 + Digit
        Value = Value // 10

    if(Original == Reverse):
        print("It is palindrome")
    else:
        print("It is not palindrome")
    
def main():
    No = 0
    Result = 0

    No = int(input("Enter the number : "))

    Result = Display(No)

if __name__ == "__main__":
    main()
  