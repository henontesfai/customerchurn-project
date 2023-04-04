import pandas as pd
import numpy as np

# Load data
data = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

# Replace empty spaces with NaN
data.replace(" ", np.nan, inplace=True)

# Drop rows with missing values
data.dropna(subset=['TotalCharges'], inplace=True)

# Convert TotalCharges to float type
data['TotalCharges'] = data['TotalCharges'].astype(float)

# Encode categorical variables
data_encoded = pd.get_dummies(data, columns=['gender', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod'])

# Convert 'Yes' and 'No' in Churn column to 1 and 0
data_encoded['Churn'] = data_encoded['Churn'].map({'Yes': 1, 'No': 0})

# Save preprocessed data to a CSV file
data_encoded.to_csv('preprocessed_data.csv', index=False)
