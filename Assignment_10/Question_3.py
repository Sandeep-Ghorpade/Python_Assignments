# Write a program which accepts one number and prints factorial of that number

def Display(Value):
    Fact = 1
    for i in range(Value,1,-1):
        Fact = Fact * i

    return(Fact)

def main():
    No = 0
    Result = 0

    No = int(input("Enter the number : "))

    Result = Display(No)

    print("Factorial of number is : ",Result)

if __name__ == "__main__":
    main()
