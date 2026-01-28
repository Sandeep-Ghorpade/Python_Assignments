# Write a program which accepts one number and prints count of digits in that number. 

def Display(Value):
    i = 0
    while(Value != 0):
        Value = Value // 10
        i = i + 1

    return(i)
    
def main():
    No = 0
    Result = 0

    No = int(input("Enter the number : "))

    Result = Display(No)

    print("Number of digits are : ",Result)

if __name__ == "__main__":
    main()
 