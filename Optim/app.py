import os
import pandas as pd
import numpy as np
import pickle
from flask import Flask, render_template, request, jsonify

# Load the feature names
current_directory = os.path.dirname(os.path.abspath(__file__))
feature_names_path = os.path.join(current_directory, 'feature_names.txt')

with open(feature_names_path, 'r') as f:
    feature_names = [line.strip() for line in f]

model_path = os.path.join(current_directory, 'model.pkl')
scaler_path = os.path.join(current_directory, 'scaler.pkl')

with open(model_path, 'rb') as f:
    model = pickle.load(f)

with open(scaler_path, 'rb') as f:
    scaler = pickle.load(f)

def preprocess(input_data):
    # Convert TotalCharges to float type
    input_data['TotalCharges'] = input_data['TotalCharges'].astype(float)

    # Encode categorical variables
    input_data_encoded = pd.get_dummies(input_data, columns=['Contract'])

    # Add any missing columns with default values
    for col in feature_names:
        if col not in input_data_encoded.columns:
            input_data_encoded[col] = 0

    # Reorder the columns to match your original dataset
    input_data_encoded = input_data_encoded[feature_names]

    # Scale the numeric variables
    input_data_encoded_scaled = scaler.transform(input_data_encoded)

    return input_data_encoded_scaled

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        contract = request.json['contract']
        tenure = int(request.json['tenure'])
        monthly_charges = float(request.json['monthly_charges'])
        total_charges = float(request.json['total_charges'])

        input_data = pd.DataFrame([[contract, tenure, monthly_charges, total_charges]],
                                  columns=["Contract", "tenure", "MonthlyCharges", "TotalCharges"])
        input_data_encoded = preprocess(input_data)
        prediction = model.predict(input_data_encoded)

        return jsonify({"prediction": int(prediction[0])})
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
