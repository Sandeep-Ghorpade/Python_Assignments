# Write a program which accept one number and display below pattern.
#Input : 5
#Output : 1             
#         1    2        
#         1    2    3    
#         1    2    3    4    
#         1    2    3    4    5

def Pattern(Row,Col):
    for i in range(1,Row + 1):
        for j in range(1,Col + 1):
            if(i >= j):
                print(j,end = "   ")
        print("\n")

def main():
    No1 = 0
    No2 = 0

    No1 = int(input("Enter the number of rows : "))
    No2 = int(input("Enter the number of columns : "))

    if((No1 <= 0) or (No2 <= 0)):
        print("Negative and zero value should not be accepted") 

    Pattern(No1,No2)

if __name__ == "__main__":
    main()