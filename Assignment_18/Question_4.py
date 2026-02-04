# Write a program which accept N numbers from user and store it into List. Accept one another number from user and return frequency of that number from List.
# Input : Number of elements : 11
# Input Elements : 13  5  45  7  4  56  5  34  2  5  65
# Element to search : 5
# Output : 3

def main():
    Size = 0
    Value = 0
    Data = list()
    SearchNo = 0
    Counter = 0

    print("Enter the numbers of elements : ")
    Size = int(input())

    print("Enter the elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    SearchNo = int(input("Enter the element that you want to search : "))
        
    for i in range(0,Size):
        if(SearchNo == Data[i]):
            Counter = Counter + 1
        
    print("Output is : ",Counter)

if __name__ == "__main__":
    main()