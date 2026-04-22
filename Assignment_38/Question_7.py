# Draw a boxplot for Attendance.
# Identify if any outliers are present.

import pandas as pd
import matplotlib.pyplot as plt

DataPath = "student_performance_ml.csv"
df = pd.read_csv(DataPath)

df["Attendance"].plot.box()
plt.show()
