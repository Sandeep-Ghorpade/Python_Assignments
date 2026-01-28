# Write a program which accepts name from user and display length of its name.

def Length(Value):
    print(len(Value))
    
def main():
    Word = {'\0'}

    Word = (input("Enter the name : "))

    Length(Word)

if __name__ == "__main__":
    main()