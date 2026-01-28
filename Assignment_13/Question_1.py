# Write a program which accepts length and width of rectangle and prints area.

def Display(Value1,Value2):
    Area = 0
    Area = Value1 * Value2   #Area = length * Width

    return(Area)

def main():
    No1 = 0
    No2 = 0
    Result = 0

    No1 = int(input("Enter the length of rectangle : "))
    No2 = int(input("Enter the width of rectangle : "))

    if((No1 <= 0) or (No2 <= 0)):
        print("Negative or zero value should not be accepted")
        return -1

    Result = Display(No1,No2)

    print("Area of rectangle is :",Result)

if __name__  == "__main__":
    main()