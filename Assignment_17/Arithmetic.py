# Create on module named as Arithmetic which contains 4 functions as Add() for addition ,Sub() for substraction,mult() for multiplication,and div() for division. 
# All functions accepts two parameters as number and perform the operation . Write on python program which call all the functions from Arithmetic module by accepting the parameters from user. 

print("Inside Arithmetic Module : ",__name__)

def Add(No1,No2):
    Ans = 0
    Ans = No1 + No2
    return Ans

def Sub(No1,No2):
    Ans = 0
    Ans = No1 - No2
    return Ans

def Mult(No1,No2):
    Ans = 0
    Ans = No1 * No2
    return Ans

def Div(No1,No2):
    Ans = 0
    Ans = No1 / No2
    return Ans