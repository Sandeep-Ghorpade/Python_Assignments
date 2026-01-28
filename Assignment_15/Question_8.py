# Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5.

Divisible = lambda No : (((No % 3) == 0) and ((No % 5) == 0))

def main():
    Data = [45,9,2,700,315,55,3,555]
    print("Actual Data is : ",Data)

    FData = list(filter(Divisible,Data))
    print("Data after filter is : ",FData)

if __name__ == "__main__":
    main()