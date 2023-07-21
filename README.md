# About

# Credit-Fraud-Detection-DL-model

This project is a part of my personal projects.

# Aim
To develop a powerful predictive model to identify fraudulent transactions with utmost efficiency.

# Summary
* The dataset was collected from Kaggle [[Link](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)].
* The dataset was observerd to be highly imbalanced. So, we planned to experimenting with 2 approaches.
  # 1. Under Sampling:
    * The technique here was to use an *Undersampled* data of the original dataframe having a balanced Class 0 and Class 1 in the target.
    * Multiple ML models were developed, but they always ended up with the model overfitting.
    * Best model was *Logistic Regression* with over 94% accuracy in both train and test data.
    * We also developed a simple neural netword model with *Multi-Layer Perceptron* using Sklearn acheiving a similar performance.
    * HyperParameter tuning was performed using Grid Search, yet we had a small number of unstable False Negative predictions (model predicted a fraudulent transaction as a legit transaction) only able to attain an accuracy of 94%.
 
  # 2. Cost Sensitive Neural Network:
    * Here we used the original data to develop DL model with the help of adding weights to the classes according to the imbalance ratio
    * With this we obtained the best performing model with over 96% accuracy on Test and Train data.
    
* Finally the model was saved as a pickle file and reused to create an external app using streamlit.
