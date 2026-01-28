# Write a program which accepts one number and checks whether it is prime or not
def Display(Value):
    if(Value > 1):
        for i in range(2,Value):
            if((Value % i) == 0):
                print(Value, "is not prime number")
                break 
        else:
            print(Value, "is prime number")
    else:
        print(Value, "is not prime number")
    
def main():
    No = 0

    No = int(input("Enter the number : "))

    Display(No)

if __name__ == "__main__":
    main()
 