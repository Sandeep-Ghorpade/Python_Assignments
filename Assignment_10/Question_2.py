# Write a program which accepts one number and print sum of first N natural numbers.

def Display(Value):
    Sum = 0
    for i in range(1,Value + 1):
        Sum = Sum + i
    return(Sum)

def main():
    No = 0
    Result = 0

    No = int(input("Enter the number : "))

    Result = Display(No)

    print("Sum of first n natural numbers are : ",Result)

if __name__ == "__main__":
    main()
