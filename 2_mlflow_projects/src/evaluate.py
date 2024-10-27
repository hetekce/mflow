# evaluate.py
import pandas as pd
import argparse
from sklearn.metrics import accuracy_score, classification_report
import joblib

def evaluate_model(model_path, test_data_path):
    # Load test data
    df = pd.read_csv(test_data_path)
    X_test = df.drop("target", axis=1)
    y_test = df["target"]

    # Load model
    model = joblib.load(model_path)

    # Make predictions and evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    
    print(f"Test Accuracy: {accuracy}")
    print("Classification Report:\n", report)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_path", type=str, required=True, help="Path to the saved model")
    parser.add_argument("--test_data_path", type=str, required=True, help="Path to the test data")
    args = parser.parse_args()

    evaluate_model(args.model_path, args.test_data_path)
