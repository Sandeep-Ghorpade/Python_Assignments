# Write a program which accepts one number and prints binary equivalent.

def Display(Value):
    Place = 1
    Binary = 0

    while(Value > 0):
        Binary = Binary + (Value % 2) * Place
        Value = Value // 2 
        Place = Place * 10
        
    return(Binary)
    
def main():
    No = 0
    Result = 0

    No = int(input("Enter the number :"))

    Result = Display(No)

    print("Binary equivalent of a given number is :",Result)

if __name__  == "__main__":
    main()