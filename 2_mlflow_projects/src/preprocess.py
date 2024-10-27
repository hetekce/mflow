# preprocess.py
import pandas as pd
import argparse

def preprocess_data(input_path, output_path):
    # Load data
    df = pd.read_csv(input_path)

    # Example preprocessing steps
    df.fillna(0, inplace=True)       # Fill missing values
    df = df.drop_duplicates()         # Remove duplicates
    df = df[df['column_name'] > 0]    # Example filter (customize as needed)

    # Save preprocessed data
    df.to_csv(output_path, index=False)
    print(f"Data preprocessed and saved to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_path", type=str, required=True, help="Path to the raw data file")
    parser.add_argument("--output_path", type=str, required=True, help="Path to save processed data")
    args = parser.parse_args()

    preprocess_data(args.input_path, args.output_path)
