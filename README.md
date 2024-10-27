# MLOps Tools: MLflow and Hugging Face

## 1. Installing and Using MLflow

```sh
# To create mlflow virtual environment For linux or WSL
sudo apt install python3 python3-pip ipython3 # install python3
sudo apt-get install python3-venv # install venv
python3 -m venv mlflow # create venv
source mlflow/bin/activate # activate venv

# To create mlflow virtual environment For Windows
python -m venv mlflow # create venv
python.exe -m pip install --upgrade pip # Optionally to update pip
.\mlflow\Scripts\activate   # To activate the mlflow environment

# To install the mlflow
pip install mlflow==2.17.1

# To open the mlflow user interface
mlflow ui

# For testing the logs, metrics and artifacts you can run the command below. Then mlruns folder will be created in the project folder
python .\1_installing_mlflow\testing.py
```
