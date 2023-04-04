# Customer Churn Prediction

This project focuses on predicting customer churn for a telecommunications company using machine learning techniques. The goal is to identify customers at risk of leaving the company and help develop targeted retention strategies.

## Dataset Overview

The dataset used for this project contains information about 7,032 customers, including demographic data, account information, and churn status. Some key features include:

- Customer ID
- Gender
- Tenure
- Monthly Charges
- Total Charges
- Contract Type
- Payment Method

## Data Preprocessing and EDA

The data was preprocessed by handling missing values, converting data types, and encoding categorical variables. During the exploratory data analysis phase, visualizations were created to understand the distribution of churn and its relationship with different features.

![Churn Distribution](path/to/churn_distribution.png)

![Churn by Contract Type](path/to/churn_by_contract_type.png)

## Model Selection and Evaluation

A logistic regression model was used to predict customer churn. The model was trained on a subset of the data, and its performance was evaluated using the following metrics:

- Accuracy: 0.7948
- Precision: 0.84 (No Churn), 0.64 (Churn)
- Recall: 0.89 (No Churn), 0.53 (Churn)
- F1-score: 0.86 (No Churn), 0.58 (Churn)

## Feature Importance

The most important features for predicting customer churn were identified using the logistic regression model's coefficients. The plot below shows the top features in order of importance.

![Feature Importance](path/to/feature_importance.png)

## Conclusion and Recommendations

The logistic regression model performed reasonably well in predicting customer churn. The insights gained from the feature importance analysis suggest that contract type, tenure, and monthly charges are key factors in predicting churn. Based on these findings, the company could consider the following recommendations:

- Offer personalized contract options or incentives for customers with month-to-month contracts.
- Develop loyalty programs to increase customer tenure.
- Review pricing strategies to ensure competitive monthly charges.

## Code

For those interested in the technical details of the project, you can find the source code in this [GitHub repository](https://github.com/yourusername/your-repo).
