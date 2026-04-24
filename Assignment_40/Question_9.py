# PerformanceIndex = (StudyHours * 2) + Attendance
# Train the model including this new feature.
# Does accuracy improve?

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import(
    accuracy_score
)
from matplotlib import pyplot as plt

DataPath = "student_performance_ml.csv"
df = pd.read_csv(DataPath)

Border = "-" * 50
print(Border)

feature_cols = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]

df["PerformanceIndex"] = (df["StudyHours"] * 2) + df["Attendance"]

feature_cols.append("PerformanceIndex")

X = df[feature_cols]
Y = df["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

Model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    random_state=42
)

Model.fit(X_train, Y_train)

print("Model train successfully")

print(Border)

Y_pred = Model.predict(X_test)

print("Model testing complete")

accuracy = accuracy_score(Y_test, Y_pred)

print(Border)

print("Accuracy of the model is : ",accuracy * 100)

# The accuracy still 100 % after adding new feature PerformanceIndex 










