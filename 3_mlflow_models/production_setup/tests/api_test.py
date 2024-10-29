import requests
import json
import sys


def test_api(**kwargs):
    input_data = kwargs.get('input_data', None)
    # Define the MLflow model endpoint URL
    url = "http://127.0.0.1:5001/invocations"

    # Define the input JSON data
    # Make sure to structure the input data to match your model’s expected format
    data = {
        "dataframe_split": {
            "columns": ["text"],
            "data": [[input_data]]
        }
    }

    # Convert the data to JSON format
    json_data = json.dumps(data)

    # Send the POST request
    response = requests.post(url, headers={"Content-Type": "application/json"}, data=json_data)

    # Print the response from the server
    print("Response Status Code:", response.status_code)
    print("Response JSON:", response.json())  # Use .json() if the response is JSON formatted


if __name__ == '__main__':
    args = {}
    # catch input_data argument by runtime directly in terminal
    for i, arg in enumerate(sys.argv[1:]):
        k, v = arg.split('=')
        args[k] = v
        
    test_api(**args)
