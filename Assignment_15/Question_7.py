# Write a lambda function using filter() which accepts a list of strings and returns a list of strings having length greater than 5.

Length = lambda word : len(word) >= 5

def main():
    Data = ["Red","Black","Blue","Orange","Yellow","White","Pink","Violet","Green","Grey"]
    print("Actual Data is : ",Data)

    FData = list(filter(Length,Data))
    print("Data after filter is : ",FData)

if __name__ == "__main__":
    main()