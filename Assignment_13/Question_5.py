# Write a program which accepts marks and displays grade.

def Display(Value):
    if(Value >= 75):
        print("Grade A+")
        print("Congrulations, you have achieved distinction")
    elif(Value >= 60):
        print("Grade A")
        print("Congrulations, you have achieved first class")
    elif(Value >= 50):
        print("Grade B")
        print("Congrulations, you have achieved second class")
    elif(Value >= 35):
        print("Grade C")
        print("Congrulations, you have achieved third class")
    elif(Value < 35):
        print("You have fail.Try next time.")

def main():
    No = 0

    No = int(input("Enter the marks :"))

    Display(No)

if __name__  == "__main__":
    main()