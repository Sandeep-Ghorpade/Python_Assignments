# Using pandas functions, calculate and display:
#    Average StudyHours
#    Average Attendance
#    Maximum PreviousScore
#    Minimum SleepHours

import pandas as pd

DataPath = "student_performance_ml.csv"
df = pd.read_csv(DataPath)

average_studyhours = df["StudyHours"].mean()
print("Average study hours is :",average_studyhours)

average_attendance = df["Attendance"].mean()
print("Average attendance is : ",average_attendance)

maximum_previousscore = df["PreviousScore"].max()
print("Maximum previous score is :",maximum_previousscore)

minimum_sleephours = df["SleepHours"].min()
print("Minimum sleep hours is : ",minimum_sleephours)