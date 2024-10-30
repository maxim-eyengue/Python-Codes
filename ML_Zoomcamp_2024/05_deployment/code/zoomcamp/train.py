#!/usr/bin/env python
# coding: utf-8

####### Save Churn Prediction Model #######

# Necessary import
import pickle
import requests
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, KFold
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score


### Parameters ###
print("Setting parameters")
# Regularization parameter
C = 1.0
# Number of splits for Kfold Cross-Validation
n_splits = 5
# model file name
output_file = f'model_C={C}.bin'

### Data Preparation ###
print("Preparing Data")
# read the data
df = pd.read_csv('data-week-3.csv')

# Normalize columns names
df.columns = df.columns.str.lower().str.replace(' ', '_')

# List of categorical variaables
categorical_columns = list(df.dtypes[df.dtypes == 'object'].index)

# For each categorical variable
for c in categorical_columns:
    # Normalize strings values
    df[c] = df[c].str.lower().str.replace(' ', '_')

# Convert `object` type to numeric
df.totalcharges = pd.to_numeric(df.totalcharges, errors = 'coerce')
# Fill missing values
df.totalcharges = df.totalcharges.fillna(0)

# Target encoding
df.churn = (df.churn == 'yes').astype(int)



# Split the data into full_train and test
df_full_train, df_test = train_test_split(df, test_size = 0.2, random_state = 1)


# List of numerical features
numerical = ['tenure', 'monthlycharges', 'totalcharges']

# List of categorical features
categorical = [
    'gender',
    'seniorcitizen',
    'partner',
    'dependents',
    'phoneservice',
    'multiplelines',
    'internetservice',
    'onlinesecurity',
    'onlinebackup',
    'deviceprotection',
    'techsupport',
    'streamingtv',
    'streamingmovies',
    'contract',
    'paperlessbilling',
    'paymentmethod',
]



# Function for training a logistic regression model
def train(df_train, y_train, C = 1.0):
    # Convert data to list of dictionaries
    dicts = df_train[categorical + numerical].to_dict(orient = 'records')

    # Initialize vectorizer for One-Hot-Encoding
    dv = DictVectorizer(sparse = False)
    # One-Hot-Encoding
    X_train = dv.fit_transform(dicts)

    # Initialize logistic regression model
    model = LogisticRegression(C = C, max_iter = 1000)
    # Model training
    model.fit(X_train, y_train)

    # return one-hot-encoder and logistic model
    return dv, model



def predict(df, dv, model):
     # Convert data to list of dictionaries
    dicts = df[categorical + numerical].to_dict(orient = 'records')

    # One-Hot-Encoding
    X = dv.transform(dicts)
    # Make soft predictions
    y_pred = model.predict_proba(X)[:, 1]

    # return predictions
    return y_pred


### Cross Validattion ###
print(f"Performing KFold Cross-Validation with C = {C}")
# Kfold cross-validation
kfold = KFold(n_splits = n_splits, shuffle = True, random_state = 1)

# Initialize scores
scores = []

# Initialize number of folds
fold = 0

# For each iteration of K-fold split and the pair of indexes generated
for train_idx, val_idx in kfold.split(df_full_train):
    # Select train and validation data
    df_train = df_full_train.iloc[train_idx]
    df_val = df_full_train.iloc[val_idx]

    # Select target variables
    y_train = df_train.churn.values
    y_val = df_val.churn.values

    # Train model
    dv, model = train(df_train, y_train, C = C)
    # Make predictions
    y_pred = predict(df_val, dv, model)

    # Get score
    auc = roc_auc_score(y_val, y_pred)
    # Store score
    scores.append(auc)
    # print auc
    print(f"auc on fold {fold} is {auc}.")

    # Increment number of fold
    fold += 1
    
# Print scores' means and standard deviations
print("Validation results:")
print('C = %s, mean = %.3f, std = +- %.3f' % (C, np.mean(scores), np.std(scores)))




### Final Training ###
print("Training the final model")
# Model training
dv, model = train(df_full_train, df_full_train.churn.values, C = 1.0)
# Make soft predictions
y_pred = predict(df_test, dv, model)

# Real test target values
y_test = df_test.churn.values
# AUC score
auc = roc_auc_score(y_test, y_pred)

# Print the final score
print(f"auc = {auc}")


### Save the model ###
print("Storing the model into a file")
# Open file and write bytes into it
with open(output_file, 'wb') as f_out: 
    # Save model 
    pickle.dump((dv, model), f_out)

print(f"The model is saved to {output_file}.")
# ---