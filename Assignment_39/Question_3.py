# Calculate model accuracy using accuracy_score.
# Display the result in percentage format.

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix
)

DataPath = "student_performance_ml.csv"
df = pd.read_csv(DataPath)

Border = "-" * 50

print(df.head())

feature_cols = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]

X = df[feature_cols]
Y = df["FinalResult"]

#############################################
# Split the dataset for training and testing
#############################################
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

#############################################
# Build the model
#############################################

Model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    random_state=42
)

print("Model is successfully created :",Model)

print(Border)

#############################################
# Train the model
#############################################

Model.fit(X_train, Y_train)

print("Model train successfully")

print(Border)

#############################################
# Test the model
#############################################

Y_pred = Model.predict(X_test)

print("Model test successfully")

print(Border)

print("Expected Answer : ")
print(Y_test)

print("Predicted Answer : ")
print(Y_pred)

#############################################
# Evaluate(Test) the model for performance
#############################################

print(Border)

accuracy = accuracy_score(Y_test, Y_pred)
print("Accuracy of the model is : ",accuracy * 100)