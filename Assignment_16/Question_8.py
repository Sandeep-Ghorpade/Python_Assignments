# Write a program which accepts number from user and print that number of "*" on screen.

def Display(Value):
    for i in range(1,Value + 1):
        print("*",end = "  ")
    
def main():
    No = 0

    No = int(input("Enter the number : "))

    if(No <= 0):
        print("Negative or zero value should not be accepted")

    Display(No)

if __name__ == "__main__":
    main()