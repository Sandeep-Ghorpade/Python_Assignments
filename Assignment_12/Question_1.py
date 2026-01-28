# Write a program which accepts one character and checks whether it is vowel or consonant.

def Display(data):
    pattern = 'A,E,I,O,U,a,e,i,o,u'

    for ch in data:
        if(ch in pattern):
            print("It is vowel")
        else:
            print("It is consonant")
    

def main():

    ch = input("Enter a character: ")[0]

    Display(ch)

if __name__ == "__main__":
    main()