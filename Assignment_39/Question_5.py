# Calculate:
# Training accuracy
# Testing accuracy
# Compare both and comment whether the model is overfitting or underfitting.

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

print(Border)

cm = confusion_matrix(Y_test, Y_pred)
print("Confusion matrix : ")
print(cm)

print(Border)

training_pred = Model.predict(X_train)
training_acc = accuracy_score(training_pred, Y_train)
print("Training accuracy is : ",training_acc * 100)

print(Border)

testing_pred = Model.predict(X_test)
testing_acc = accuracy_score(testing_pred, Y_test)
print("Testing accuracy is : ",testing_acc * 100)

# The model is neither overfitting nor underfitting beacause both training and testing accuracy is 100%.
# The model gives 100% accuracy beacause the dataset is small and simple. So it can learn pattern easily.