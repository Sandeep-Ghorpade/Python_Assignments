# Write a program which accepts one number from user and return addition of its factors.

def AddFactors(Value):
    Sum = 0

    for i in range(1,Value):
        if((Value % i) == 0):
            Sum = Sum + i
    return(Sum)
            
def main():
    No = 0
    Result = 0

    No = int(input("Enter the number : "))

    if(No <= 0):
        print("Negative and zero value should not be accepted") 

    Result = AddFactors(No)

    print("Addition of factors is : ",Result)

if __name__ == "__main__":
    main()