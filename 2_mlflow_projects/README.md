# MLflow Project

## 1. Overview of the MLproject

Here’s how the project directory structure would look when set up for an MLflow project using Docker, with the `MLProject` and `Dockerfile` files included:

```md
ml_project/
├── data/
│   └── raw_data.csv               # Example raw data file
├── models/                        # Directory to store models
│   └── model.pkl                  # Placeholder for trained model
├── notebooks/                     # Jupyter notebooks for exploration (optional)
├── src/                           # Source code for the project
│   ├── main.py                    # Main script to run the entire project
│   ├── preprocess.py              # Script for data preprocessing
│   ├── train.py                   # Script for model training
│   └── evaluate.py                # Script for evaluating the model
├── MLProject                      # MLflow configuration file
├── Dockerfile                     # Docker configuration file for reproducible environment
├── requirements.txt               # Python dependencies
└── README.md                      # Project description and instructions
```

Explanation of Each Component:

- **data/**: Folder to store raw and processed data files, like `raw_data.csv`. MLflow will treat this directory as part of the artifact storage for any data processed within the project.

- **models/**: Directory to save trained models (e.g., `model.pkl`). MLflow can save models in this directory as part of the project artifacts.

- **notebooks/**: Jupyter notebooks for data exploration, EDA (optional). This is useful during the development phase but optional for MLflow project runs.

- **src/**: Directory containing all project source code.
  - `main.py`: Primary script that can run the whole workflow, potentially orchestrating `preprocess.py`, `train.py`, and `evaluate.py`.
  - `preprocess.py`: Script to handle data preprocessing tasks.
  - `train.py`: Script for training the machine learning model.
  - `evaluate.py`: Script for evaluating model performance.

- **MLProject**: MLflow project file that defines entry points and the Docker environment to be used.

- **Dockerfile**: Docker configuration to set up the project environment, including any dependencies listed in `requirements.txt`.

- **requirements.txt**: Python packages needed for the project (e.g., pandas, scikit-learn, numpy).

## 2. Running MLproject within Docker Environment

- **Build Docker Image**:

```sh
docker build -t my_ml_project_image .
```

- **Run MLflow Project Using Docker**:

When you run the command `mlflow run .`, MLflow will use the **default entry point**, which is the one named `main` in the `MLProject` file unless you specify a different entry point. If you want to run a specific entry point other than `main`, you can specify it with the `-e` option.

Here’s how to run each entry point:

- **Default entry point** (`main`):
  
```sh
mlflow run .
```

- **Default entry point with building a new image** (`main`):

```sh
mlflow run . --build-image
```

- **Specific entry points**:

  If you want to run, say, the `train` entry point, you can specify it like this:

```sh
mlflow run . -e train
```

  Similarly, you can specify `preprocess` or `evaluate` as entry points:

```sh
mlflow run . -e preprocess
mlflow run . -e evaluate
```

## 3. Running MLproject from remote Git repositories

If the repository consists of MLproject you can run it as below:

```sh
# -P you can add the required parameters that entry point requires.
mlflow run git@github.com:mlflow/mlflow-example.git -P alpha=0.7
```


## 4. Connection Mlflow to Databricks and Azure ML

Create the tokens in databricks then you can connect as below.

```sh
export MLFLOW_TRACKING_URI=databricks

# Specify the workspace hostname and token
export DATABRICKS_HOST="..."
export DATABRICKS_TOKEN="..."

# Or specify your databricks username & pw
export DATABRICKS_USERNAME="..."
export DATABRICKS_PASSWORD="..."
```

You can connect azure ml within a python file as below:

```py
import mlflow


aml_region = ""
subscription_id = ""
aml_resource_group = ""
aml_workspace_name = ""

azureml_mlflow_uri = f"azureml://{aml_region}.api.azureml.ms/mlflow/v1.0/subscriptions/{subscription_id}/resourceGroups/{aml_resource_group}/providers/Microsoft.MachineLearningServices/workspaces/{aml_workspace_name}"

mlflow.set_registry_uri(azureml_mlflow_uri)
```
