#!/bin/bash

# Define the MLflow model endpoint URL
URL="http://127.0.0.1:5001/invocations"

# Define the input JSON data
# Make sure to structure the input data to match your model’s expected format
DATA='{
  "dataframe_split": {
    "columns": ["text"],
    "data": [["It was not easy at all to create the app."]]
  }
}'

# Use curl to send a POST request with the data
curl -X POST $URL \
     -H "Content-Type: application/json" \
     -d "$DATA"
