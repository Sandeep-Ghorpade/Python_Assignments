# Write a program which accept N numbers from user and store it into List.
# Return addition of all prime numbers from that List.
# Main python file accepts N numbers from user and pass each number to ChkPrime() function which is part of our user defined module named as MarvellousNum. 
# Name of the function from main python file should be ListPrime().

print("MarvellousNum Module : ",__name__)
def ChkPrime(No):
    if(No > 1):
        for i in range(2,No):
            if((No % i) == 0):
                return -1
        else:
            return No
    else:
         return -1

    
                