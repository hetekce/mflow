# Working with MLmodel

0. Supposing that the you are inside the main folder of the repository, lets change the directory to the belowed folder.

```sh
cd 3_mlflow_models/development_setup/
```

1. We start the mlflow server with sqlite:

```sh
mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns --host 0.0.0.0 --port 5000
```

2. Be sure to export the tracking uri before proceeding:

```sh
export MLFLOW_TRACKING_URI=http://127.0.0.1:5000
```

3. Then we can create a custom model and register it with `mlflow.pyfunc.log_model` in `log_model.py`. Note that we set trackingi uri inside the `log_model.py` before logging the model, if we did not export the variable in the previous step:
 `mlflow.set_tracking_uri("http://127.0.0.1:5000")`.

```sh
python log_model.py
```

Below files below will be automatically created once we logged the model: `conda.yaml`, `MLmodel`, `model.pkl`, `python_env.yaml` and `requirements.txt`.

4. Once the model is logged and the mlflow tracking uri is exported, we can serve it to use it as an api:

```sh
# The command below will be printed after you successfully run the log_model.py. run_id will be catched automatically.
# We open the port 5001 since 5000 is already occupied by the mlflow server.
mlflow models serve --model-uri runs:/$run_id/model --host 0.0.0.0 --port 5001
```

5. You can send your queries to the api endpoint. For that i created the `tests/*`. You can run one of them to see if the api is up and running.

```sh
cd 3_mlflow_models/development_setup/tests/

# To run the api test native from the cli
chmod +x curl.sh
./curl.sh

# To run the api as python subprocess
python curl_api_test.py

# To request the api with native python library with `input_data` parameter, which is the english text to be passed to translate
python api_test.py input_data='It was not easy at all to create the app.'
```
