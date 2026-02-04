# Write a program which accept number from user and return addition of digits in that number.
# Input : 5187934
# Output : 37

def Display(Value):
    Digit = 0
    Sum = 0

    while(Value != 0):
        Digit = Value % 10
        Sum = Sum + Digit
        Value = Value // 10
        
    return(Sum)
    

def main():     
    No = 0
    Result = 0

    No = int(input("Enter the number : "))

    Result = Display(No)
    print("Summation of digits are : ",Result)

if __name__ == "__main__":
    main()