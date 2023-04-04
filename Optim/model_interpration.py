import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

# Load X
with open('X.pkl', 'rb') as f:
    X = pickle.load(f)

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Get feature importance
feature_importance = pd.DataFrame({'Feature': X.columns, 'Importance': model.coef_[0]})

# Sort by absolute importance
feature_importance['Abs_Importance'] = abs(feature_importance['Importance'])
feature_importance.sort_values(by='Abs_Importance', ascending=False, inplace=True)

# Plot feature importance
plt.figure(figsize=(10, 10))
sns.barplot(x='Importance', y='Feature', data=feature_importance)
plt.title('Feature Importance for Churn Prediction')
plt.show()
