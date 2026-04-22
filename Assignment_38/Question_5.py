# Plot a histogram of StudyHours.
# Explain what the distribution tells you.

import pandas as pd
import matplotlib.pyplot as plt

DataPath = "student_performance_ml.csv"
df = pd.read_csv(DataPath)

plt.hist(df["StudyHours"])
plt.show()

# The distributions tells us that the most student studing moderate hours.
