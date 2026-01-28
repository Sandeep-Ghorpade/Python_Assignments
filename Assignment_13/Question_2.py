# Write a program which accepts radius of circle and prints area of circle.

def Display(Value):
    pi = 3.14
    Area = 0
    Area = pi * Value ** 2  # Area = pi * (r*r)

    return(Area)
    

def main():
    No = 0
    Result = 0

    No = int(input("Enter the radius of circle : "))

    if(No <= 0):
        print("Negative or zero value should not be accepted")
        return -1

    Result = Display(No)

    print("Area of circle is :",Result)

if __name__  == "__main__":
    main()