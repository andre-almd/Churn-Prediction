from pickle import load
import xgboost as xgb
import pandas as pd
import numpy as np

def load_dados():
    # Loading the scalers for data pre process
    X_scaler = load(open('dados/X_enc_model.sav', 'rb'))
    #print(X_scaler)

    minmax_enc = load(open('dados/minmax_enc_model.sav', 'rb'))

    X_scaler_names = np.array(['Gender_Male', 'SeniorCitizen_Yes', 'Partner_Yes', 'Dependents_Yes', 'PhoneService_Yes', 'MultipleLines_No', 'MultipleLines_No phone service', 'MultipleLines_Yes',
    'InternetService_DSL', 'InternetService_Fiber optic', 'InternetService_No', 'OnlineSecurity_No', 'OnlineSecurity_No internet service', 'OnlineSecurity_Yes',
    'OnlineBackup_No', 'OnlineBackup_No internet service', 'OnlineBackup_Yes', 'DeviceProtection_No', 'DeviceProtection_No internet service', 'DeviceProtection_Yes',
    'TechSupport_No', 'TechSupport_No internet service', 'TechSupport_Yes', 'StreamingTV_No', 'StreamingTV_No internet service', 'StreamingTV_Yes', 'StreamingMovies_No',
    'StreamingMovies_No internet service', 'StreamingMovies_Yes', 'Contract_Month-to-month', 'Contract_One year', 'Contract_Two year', 'PaperlessBilling_Yes',
    'PaymentMethod_Bank transfer (automatic)', 'PaymentMethod_Credit card (automatic)', 'PaymentMethod_Electronic check', 'PaymentMethod_Mailed check',
    'Tenure', 'Charges_Monthly', 'Charges_Total'], dtype=object)

    # Loading the model from XGBoost
    model = xgb.XGBClassifier(gamma=0, learning_rate=0.01, max_depth=6, n_estimators=125, subsample=0.7)
    model.load_model('dados/XGB_final_otimizado.model')

    return X_scaler, minmax_enc, X_scaler_names, model


def main():
    print('Ok!')

if __name__ == '__main__':
    main()