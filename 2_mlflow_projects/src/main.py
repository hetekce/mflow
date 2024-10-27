# main.py
import argparse
import os
from preprocess import preprocess_data
from train import train_model
from evaluate import evaluate_model

def main(data_path, model_path, processed_data_path, test_data_path, epochs):
    # Step 1: Preprocess data
    preprocess_data(data_path, processed_data_path)

    # Step 2: Train model
    train_model(processed_data_path, model_path, epochs)

    # Step 3: Evaluate model
    evaluate_model(model_path, test_data_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_path", type=str, required=True, help="Path to the raw data file")
    parser.add_argument("--model_path", type=str, required=True, help="Path to save the trained model")
    parser.add_argument("--processed_data_path", type=str, required=True, help="Path to save processed data")
    parser.add_argument("--test_data_path", type=str, required=True, help="Path to the test data file")
    parser.add_argument("--epochs", type=int, default=10, help="Number of training epochs")
    args = parser.parse_args()

    main(args.data_path, args.model_path, args.processed_data_path, args.test_data_path, args.epochs)
