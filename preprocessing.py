'''This file contains the preprocessing code for the Crop Recommendation dataset.'''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Load the dataset
def load_data(file_path):
    return pd.read_csv(file_path)

def preprocess_data(df):
    X = df.drop('Crop', axis=1)
    y = df[['Crop']]
    numerical_features = X.columns
    categorical_features = ['Crop']
    numerical_transformer = StandardScaler()
    categorical_transformer = OneHotEncoder(handle_unknown='ignore')
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numerical_transformer, numerical_features),
        ])
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test, preprocessor

if __name__ == '__main__':
    file_path = r"C:\Users\anish\OneDrive\Desktop\Coding\Python\PBL\project1\Crop_Recommendation(in).csv"
    df = load_data(file_path)
    X_train, X_test, y_train, y_test, preprocessor = preprocess_data(df)
    X_train_processed = preprocessor.fit_transform(X_train)
    X_test_processed = preprocessor.transform(X_test)
    encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
    y_train_encoded = encoder.fit_transform(y_train)
    y_test_encoded = encoder.transform(y_test)
    print("Shape of X_train_processed:", X_train_processed.shape)
    print("Shape of X_test_processed:", X_test_processed.shape)
    print("Shape of y_train_encoded:", y_train_encoded.shape)
    print("Shape of y_test_encoded:", y_test_encoded.shape)
