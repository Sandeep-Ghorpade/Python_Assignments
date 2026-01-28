# Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise returns false. 

def Divisible(Value):
    return ((Value % 5) == 0)
    
def main():
    No = 0
    Result = 0

    No = int(input("Enter the number : "))

    Result = Divisible(No)

    print(Result)

if __name__ == "__main__":
    main()