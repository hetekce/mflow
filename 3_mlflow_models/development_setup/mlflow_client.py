
from mlflow.tracking import MlflowClient

mlflow_client = MlflowClient()

mlflow_client.create_registered_model("google-t5/t5-small")

mlflow_client.delete_registered_model("google-t5/t5-small")

mlflow_client.update_model_version(
    name="model_translator",
    version=2,
    description="We update the model description"
)
