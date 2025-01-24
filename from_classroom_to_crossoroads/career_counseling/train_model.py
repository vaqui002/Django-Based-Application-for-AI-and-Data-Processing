import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib
import os

# Define the path to the CSV file
csv_path = os.path.abspath('career_counseling/data/Cleaned_Survey_Data.csv')

# Load data
print("Loading data...")
data = pd.read_csv(csv_path)

# Data Preprocessing
print("Preprocessing data...")

# Selecting relevant columns for features and target
columns_of_interest = [
    ' Are you currently enrolled in a formal education program?',
    'If you answered "No" to the previous question, please specify the reason for dropping out or not enrolling.',
    'What challenges do you face in your current educational journey? (Select all that apply)',
    'On a scale of 1 to 5, how important is personalized support and guidance in your decision-making process regarding education and career choices?'
]

# Filter the data to only include the columns of interest
data_filtered = data[columns_of_interest].copy()

# Drop rows with missing data in these columns
data_filtered.dropna(inplace=True)

# Encode categorical data into numerical form
encoder = LabelEncoder()

# Encode the target variable (enrollment status)
data_filtered['Enrollment_Status'] = encoder.fit_transform(
    data_filtered[' Are you currently enrolled in a formal education program?']
)

# Encode the dropout reason and challenges
data_filtered['Dropout_Reason'] = encoder.fit_transform(
    data_filtered['If you answered "No" to the previous question, please specify the reason for dropping out or not enrolling.']
)
data_filtered['Challenges'] = encoder.fit_transform(
    data_filtered['What challenges do you face in your current educational journey? (Select all that apply)']
)

# Define the feature set (X) and the target variable (y)
X = data_filtered[['Dropout_Reason', 'Challenges', 'On a scale of 1 to 5, how important is personalized support and guidance in your decision-making process regarding education and career choices?']]
y = data_filtered['Enrollment_Status']

# Split the data into training and testing sets (80/20 split)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train logistic regression model
print("Training model...")
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate the model
print("Evaluating model...")
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# Print evaluation metrics
print(f"Model accuracy: {accuracy:.2f}")
print(f"Model precision: {precision:.2f}")
print(f"Model recall: {recall:.2f}")
print(f"Model F1 score: {f1:.2f}")

# Define the path to save the trained model
model_path = os.path.join('career_counseling', 'ml_model', 'trained_model.pkl')

# Save the trained model
print(f"Saving model to {model_path}...")
joblib.dump(model, model_path)

print("Model training and saving complete!")
