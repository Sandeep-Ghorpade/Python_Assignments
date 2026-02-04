# Create on module named as Arithmetic which contains 4 functions as Add() for addition ,Sub() for substraction,mult() for multiplication,and div() for division. 
# All functions accepts two parameters as number and perform the operation . Write on python program which call all the functions from Arithmetic module by accepting the parameters from user. 
 
import Arithmetic

print("Inside Main",__name__)

Value1 = 0
Value2 = 0
Result = 0

Value1 = int(input("Enter first number of addition : "))
Value2 = int(input("Enter second  number of Addition : "))
Result = Arithmetic.Add(Value1,Value2)
print("Addition is : ",Result)

Value1 = int(input("Enter first  number of substraction : "))
Value2 = int(input("Enter second number of substraction : "))
Result = Arithmetic.Sub(Value1,Value2)
print("Substraction is : ",Result)

Value1 = int(input("Enter first number of multiplication : "))
Value2 = int(input("Enter second number of multiplication : "))
Result = Arithmetic.Mult(Value1,Value2)
print("Multiplication is : ",Result)

Value1 = int(input("Enter first number of Division : "))
Value2 = int(input("Enter second number of Division : "))
Result = Arithmetic.Div(Value1,Value2)
print("Division is : ",Result)
