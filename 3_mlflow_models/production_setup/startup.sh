#!/bin/sh
export MLFLOW_TRACKING_URI=http://localhost:5000

# Start the MLflow tracking server in the background
mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns --host 0.0.0.0 --port 5000 &

# Wait for the tracking server to start
sleep 5

# Start a new MLflow run, log the model, and get the run_id
run_id=$(python3 /app/src/log_model.py)

# Log the run_id for reference
echo "Run ID created: $run_id"
echo "Serving the MLflow model with Run ID: $run_id"

# Serve the model using MLflow and the generated run_id
mlflow models serve --model-uri "runs:/$run_id/model" --no-conda --host 0.0.0.0 --port 5001
