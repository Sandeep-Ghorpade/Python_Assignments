# Import DecisionTreeClassifer from sklearn.
# Create a model object and train it using fit().

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

DataPath = "student_performance_ml.csv"
df = pd.read_csv(DataPath)

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

#############################################
# Train the model
#############################################

Model.fit(X_train, Y_train)

print("Model train successfully")
