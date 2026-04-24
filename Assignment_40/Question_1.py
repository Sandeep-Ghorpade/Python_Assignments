# After training the Decision Tree model, use:
# model.feature_importances_
# Display importance score of each feature.
# Which feature contributes the most in predicting FinalResult?
# Which feature contributes the least?

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

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

importance = Model.feature_importances_

for features, values in zip(X.columns, importance):
    print(features, ":", values)

# StudyHours : 0.0
# Attendance : 1.0
# PreviousScore : 0.0
# AssignmentsCompleted : 0.0
# SleepHours : 0.0

# The attendace predicting the final result.
# Other than attendance all feature contributes zero.
