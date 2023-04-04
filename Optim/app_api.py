from flask import Flask, request, jsonify
import pandas as pd
import pickle

# Your existing preprocess function
def preprocess(input_data):
    # Your preprocess function code here
    pass

app = Flask(__name__)


with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.json
    input_data_df = pd.DataFrame(input_data, index=[0])
    input_data_encoded = preprocess(input_data_df)
    prediction = model.predict(input_data_encoded)
    return jsonify({"prediction": int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
