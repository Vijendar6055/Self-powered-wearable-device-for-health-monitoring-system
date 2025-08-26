import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

import joblib



# Load the dataset

file_path = r"C:\New folder\data\sensor_disease_data_updated.xlsx"

df = pd.read_excel(file_path)



# Separate features (sensor values) and labels (disease names)

X = df.drop(columns=["Disease"])  # All columns except "Disease"

y = df["Disease"]  # Target column



# Split data for training and testing

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



# Train the Random Forest model

model = RandomForestClassifier(n_estimators=100, random_state=42)

model.fit(X_train, y_train)



# Save the trained model

joblib.dump(model, r"C:\New folder\data\random_forest_model.pkl")



print("✅ Model trained and saved successfully!")