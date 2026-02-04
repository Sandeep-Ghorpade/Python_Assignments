# Write a program which accept number from user and return number of digits in that number.
# Input : 5187934
# Output : 7

def Display(Value):
    Digit = 0
    Count = 0

    while(Value != 0):
        Digit = Value % 10
        Value = Value // 10
        Count = Count + 1
    return(Count)
    

def main():     
    No = 0
    Result = 0

    No = int(input("Enter the number : "))

    Result = Display(No)
    print("Number of digits are : ",Result)

if __name__ == "__main__":
    main()