# Write a program which accepts one number and prints its factors.

def Display(Value):
    for i in range(1,Value + 1):
        if((Value % i) == 0):
            print(i,end = " ")

def main():
    No = 0

    No = int(input("Enter the number : "))

    Display(No)

if __name__ == "__main__":
    main()