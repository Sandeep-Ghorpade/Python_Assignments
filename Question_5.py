# Write a program which accepts one number and prints all odd numbers till that number.

def Display(Value):
    for i in range(1,Value+1):
        if((i % 2) != 0):
            print(i,end = "  ")

def main():
    No = 0

    No = int(input("Enter the number : "))

    Display(No)

if __name__ == "__main__":
    main()
