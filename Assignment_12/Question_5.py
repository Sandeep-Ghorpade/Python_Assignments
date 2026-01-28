# Write a program which accepts one number and prints that many numbers in reverse order.

def Display(Value):
    for i in range(Value,0,-1):
        print(i,end = " ")

def main():
    No = 0

    No = int(input("Enter the number : "))

    Display(No)

if __name__ == "__main__":
    main()