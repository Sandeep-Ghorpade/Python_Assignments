# Objective of the Dataset

# Analyze how different factors affect student performance.
# Build a Machine Learning model to predict whether a student will pass or fail.
# Understand concepts such as training, testing, accuracy, confusion matrix, overfitting, and model evaluation.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

Border = "-" * 50

#############################################
# Step 1 : Load the dataset
#############################################

print(Border)
print("Step 1 : Load the dataset")
print(Border)

DatasetPath = "student_performance_ml.csv"
df = pd.read_csv(DatasetPath)

print("Dataset loaded successfully")
print("Initial entries from dataset : ")
print(df.head())

#############################################
# Step 2 : Data Analysis (EDA)
#############################################

print(Border)
print("Step 2 : Data Analysis (EDA)")
print(Border)

print("Shape of dataset : ",df.shape)
print("Columns Name : ",list(df.columns))
print("Missing Values (Per Colums)")
print(df.isnull().sum())

print("Statistical report of dataset")
print(df.describe())

#############################################
# Step 3 : Decide Independent and dependent variable
#############################################

print(Border)
print("Step 3 : Decide Independent and dependent variable")
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

print("X Shape : ",X.shape)
print("Y Shape : ",Y.shape)

#############################################
# Step 4 : Visualization of dataset
#############################################

print(Border)
print("Step 4 : Visualization of dataset")
print(Border)

plt.figure(figsize=(7,5))

for rlt in df["FinalResult"].unique():
    temp = df[df["FinalResult"] == rlt]
    plt.scatter(temp["PreviousScore"], temp["AssignmentsCompleted"], label = rlt)

plt.legend()
plt.grid(True)
plt.show()

#############################################
# Step 5 : Split the dataset for training and testing
#############################################

print(Border)
print("Step 5 : Split the dataset for training and testing")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

print("Data spliting activity done : ")

print("X-Independent : ",X.shape)
print("Y-Independent : ",Y.shape)

print("X_train : ",X_train.shape)
print("X_test : ",X_test.shape)

print("Y_train : ",Y_train.shape)
print("Y_test : ",Y_test.shape)

#############################################
# Step 6 : Build the model
#############################################

print(Border)
print("Step 6 : Build the model")
print(Border)

Model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    random_state=42,
)

print("Model successfully created : ",Model)

#############################################
# Step 7 : Train the model
#############################################

print(Border)
print("Step 7 : Train the model")
print(Border)

Model.fit(X_train, Y_train)

print("Model train successfully")

#############################################
# Step 8 : Test the model
#############################################

print(Border)
print("Step 8 : Test the model")

Y_pred = Model.predict(X_test)

print("Model testing complete")

print(Y_pred.shape)

print("Expected Answer : ")
print(Y_test)

print("Predicted Answer : ")
print(Y_pred)

#############################################
# Step 9 : Evaluate(Test) the model for performance
#############################################

print(Border)
print("Step 9 : Evaluate(Test) the model for performance")
print(Border)

accuracy = accuracy_score(Y_test, Y_pred)
print("Accuracy of the model is : ",accuracy * 100)

cm = confusion_matrix(Y_test, Y_pred)
print("Confusion Matrix : ")
print(cm)

print("Classification report : ")
print(classification_report(Y_test, Y_pred))

#####################################################
# Step 10 : Plot confusion matrix
#####################################################

print(Border)
print("Step 10 : Plot confusion matrix") 
print(Border)

data = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=Model.classes_)
data.plot()

plt.title("Confusion matrix of student_performance_ml dataset")
plt.show()
