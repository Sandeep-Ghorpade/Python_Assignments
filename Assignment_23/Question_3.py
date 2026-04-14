# Write a Python program to implement a class named Numbers with the following specifications:
# The class should contain one instance variable:
#    Value

# Define a constructor (__init__) that accepts a number from the user and initializes Value.

# Implement the following instance methods:
#    ChkPrime() – returns True if the number is prime, otherwise returns False
#    ChkPerfect() – returns True if the number is perfect, otherwise returns False
#    Factors() – displays all factors of the number
#    SumFactors() – returns the sum of all factors
#    You may use this method as a helper in ChkPerfect() if required)
#Create multiple objects and call all methods.

class Numbers():

    def __init__(self,Value):
        self.Value = Value

    def ChkPrime(self):
        if(self.Value > 1):
            for i in range(2, self.Value):
                if((self.Value % i) == 0):
                    return False
            else:
                return True
            
    def ChkPerfect(self):
        Sum = 0
        for i in range(1,self.Value):
            if((self.Value % i) == 0):
                Sum += i
        if Sum == self.Value:
                return True
        else:
                return False
        
    def Factors(self):
        for i in range(1,self.Value + 1):
              if((self.Value % i) == 0):
                  print(i, end = " ")
        print("\n")

    def SumFactors(self):
        Sum = 0
        for i in range(1,self.Value + 1):
            if((self.Value % i) == 0):
                Sum = Sum + i
        return Sum
            
obj1 = Numbers(11)
Result = obj1.ChkPrime()
print(Result)

obj1 = Numbers(6)
Result = obj1.ChkPerfect()
print(Result)

obj1 = Numbers(12)
Result = obj1.Factors()

obj1 = Numbers(17)
Result = obj1.SumFactors()
print(Result)

obj2 = Numbers(13)
Result = obj2.ChkPrime()
print(Result)

obj2 = Numbers(28)
Result = obj2.ChkPerfect()
print(Result)

obj2 = Numbers(15)
Result = obj2.Factors()

obj2 = Numbers(20)
Result = obj2.SumFactors()
print(Result)