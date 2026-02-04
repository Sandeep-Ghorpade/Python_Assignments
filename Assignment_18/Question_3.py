# Write a program which accept N numbers from user and store it into List. Return Minimum number from that List.
# Input : Number of elements : 4
# Input Elements : 13   5   45   7      
# Output : 5

def main():
    Size = 0
    Value = 0
    Data = list()
    Min = 0

    print("Enter the numbers of elements : ")
    Size = int(input())

    print("Enter the elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Min = Data[0]

    for i in range(1,Size):
        if(Data[i] < Min):
            Min = Data[i]
        
    print("Minimum number is : ",Min)

if __name__ == "__main__":
    main()