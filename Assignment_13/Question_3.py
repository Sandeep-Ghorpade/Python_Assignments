# Write a program which accepts one number and checks whether it is perfect number or not.

def Display(Value):
    Sum = 0

    for i in range(1,Value):
        if((Value % i )== 0):
            Sum += i
    if(Sum == Value):        
        print("Its a perfect number")
    else:
        print("Its not a perfect number")

def main():
    No = 0

    No = int(input("Enter the number :"))

    if(No <= 0):
        print("Negative or zero value should not be accepted")
        return -1

    Display(No)

if __name__  == "__main__":
    main()