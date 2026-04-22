# Write a Python program to load the file student_performance_ml.csv using pandas.
# Display:
#    First 5 records
#    Last 5 records
#    Total number of rows and columns
#    List of column names
#    Data types of each column

import pandas as pd

DataPath = "student_performance_ml.csv"
df = pd.read_csv(DataPath)

print("First five records are : ")
print(df.head())

print("Last five records are : ")
print(df.tail())

print("Total number of rows and columns are : ")
print(df.shape)

print("Columns name : ",list(df.columns))

print("Data types of columns : ")
print(df.dtypes)

