# Train model with:
# max_depth = None
# Calculate:
# Training accuracy
# Testing accuracy
# If training accuracy is 100% but testing accuracy is lower, explain why this happens.

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
    max_depth=None,
    random_state=42
)

Model.fit(X_train, Y_train)

print("Model train successfully")

print(Border)

X_pred = Model.predict(X_train)

training_accuracy = accuracy_score(Y_train, X_pred)

print("Accuracy of the model after training is : ",training_accuracy * 100)

print(Border)

Y_pred = Model.predict(X_test)

print("Model testing complete")

accuracy = accuracy_score(Y_test, Y_pred)

print(Border)

print("Accuracy of the model after testing is  : ",accuracy * 100)

# The accuracy after training and testing both is 100% 
# The model predicted all training and testing data correctly









