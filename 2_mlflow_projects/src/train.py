# train.py
import pandas as pd
import argparse
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

def train_model(data_path, model_path, epochs):
    # Load preprocessed data
    df = pd.read_csv(data_path)
    X = df.drop("churn", axis=1)
    y = df["churn"]

    # Split data
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestClassifier(n_estimators=epochs, random_state=42)
    model.fit(X_train, y_train)

    # Validate model
    y_pred = model.predict(X_val)
    accuracy = accuracy_score(y_val, y_pred)
    print(f"Validation Accuracy: {accuracy}")

    # Save model
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_path", type=str, required=True, help="Path to the preprocessed data file")
    parser.add_argument("--model_path", type=str, required=True, help="Path to save the trained model")
    parser.add_argument("--epochs", type=int, default=10, help="Number of training epochs")
    args = parser.parse_args()

    train_model(args.data_path, args.model_path, args.epochs)
