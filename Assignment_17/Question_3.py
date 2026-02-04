# Write a program which accepts one number from user and return its factorial.

def Factorial(Value):
    Fact = 1

    for i in range(1,Value+1):
        Fact = Fact * i
    return(Fact)

def main():
    No = 0
    Result = 0

    No = int(input("Enter the number : "))

    if(No <= 0):
        print("Negative and zero value should not be accepted") 

    Result = Factorial(No)
    print("Factorial of given is : ",Result)

if __name__ == "__main__":
    main()