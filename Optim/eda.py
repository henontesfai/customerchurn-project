import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# Load the original data
data = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

# Replace empty spaces with NaN
data.replace(" ", np.nan, inplace=True)

# Drop rows with missing values
data.dropna(subset=['TotalCharges'], inplace=True)

# Visualize the distribution of churn
sns.countplot(x='Churn', data=data)
plt.savefig("churn_distribution.png")
plt.show()

# Visualize Churn by Contract Type
plt.figure(figsize=(10, 4))
sns.countplot(x='Contract', hue='Churn', data=data)
plt.savefig("churn_by_contract_type.png")
plt.show()
