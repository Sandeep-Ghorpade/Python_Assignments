# Write a program which accepts one number and prints sum of digits. 

def Display(Value):
    i = 0
    Digit = 0
    Sum = 0
    while(Value != 0):
        Digit = Value % 10
        Sum = Sum + Digit 
        Value = Value // 10

    return(Sum)
    
def main():
    No = 0
    Result = 0

    No = int(input("Enter the number : "))

    Result = Display(No)

    print("Summation of digits are : ",Result)

if __name__ == "__main__":
    main()
  