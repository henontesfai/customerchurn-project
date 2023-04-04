import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import pickle

# Load preprocessed data
data_encoded = pd.read_csv('preprocessed_data.csv')


# Split the data into features and target
X = data_encoded.drop(columns=['customerID', 'Churn'])
y = data_encoded['Churn']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Add this line after splitting the dataset into X and y
with open('feature_names.txt', 'w') as f:
    for col in X.columns:
        f.write(f"{col}\n")


# Scale the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train the model
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# Make predictions
y_pred = model.predict(X_test_scaled)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Save X
with open('X.pkl', 'wb') as f:
    pickle.dump(X, f)

# Save the trained model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Save the scaler object
with open('scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)