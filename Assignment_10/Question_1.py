# Write a program which accepts one number and prints multiplication table of that number

def Display(Value):
    for i in range(Value,Value * 10 + 1,Value):
        print(i,end = ' ')

def main():
    No = 0

    No1 = int(input("Enter the number : "))

    Display(No)

if __name__ == "__main__":
    main()
