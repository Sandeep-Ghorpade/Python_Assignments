# Write a program which accepts one number and checks whethers it is divisible by 3 and 5.

def Display(Value):
    if((Value % 3) == 0) and ((Value % 5) == 0):
        print("Number is divisible by 3 and 5")
    else:
        print("Number is not divisible by 3 and 5")
    return(Value)

def main():
    No = 0
    Result = 0

    No = int(input("Enter the number : "))

    Result = Display(No)

if __name__ == "__main__":
    main()