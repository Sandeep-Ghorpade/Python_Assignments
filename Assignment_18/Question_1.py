# Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List.
# Input : Number of elements : 6
# Input Elements : 13   5   45   7   4   56
# Output : 130

def main():
    Size = 0
    Value = 0
    Data = list()
    Sum = 0

    print("Enter the numbers of elements : ")
    Size = int(input())

    print("Enter the elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    for i in range(Size):
        Sum = Sum + Data[i]
    
    print("Addition of all elements from the list is : ",Sum)

if __name__ == "__main__":
    main()