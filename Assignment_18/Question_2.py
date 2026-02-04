# Write a program which accept N numbers from user and store it into List. Return Maximum number from that List.
# Input : Number of elements : 7
# Input Elements : 13   5   45   7   4   56 34
# Output : 56

def main():
    Size = 0
    Value = 0
    Data = list()
    Max = 0

    print("Enter the numbers of elements : ")
    Size = int(input())

    print("Enter the elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Max = Data[0]

    for i in range(1,Size):
        if(Data[i] > Max):
            Max = Data[i]
        
    print("Maximum number is : ",Max)

if __name__ == "__main__":
    main()