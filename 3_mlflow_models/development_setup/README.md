# Working with MLmodel

0. Supposing that the you are inside the main folder of the repository, lets change the directory to the belowed folder.

```sh
cd 3_mlflow_models/development_setup/
```

1. We start the mlflow server with sqlite:

```sh
mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns --host 0.0.0.0 --port 5000
```

2. Then we can create a custom model and register it with `mlflow.pyfunc.log_model` in `log_model.py`. Note that we set trackingi uri inside the `log_model.py` before logging the model:
 `mlflow.set_tracking_uri("http://127.0.0.1:5000")`.

```sh
python log_model.py
```

Below files below will be automatically created once we logged the model: `conda.yaml`, `MLmodel`, `model.pkl`, `python_env.yaml` and `requirements.txt`.

3. Be sure to export the tracking uri:

```sh
export MLFLOW_TRACKING_URI=http://127.0.0.1:5000
```

4. Once the model is logged and the uri is exported, we can serve it to use it as an api:

```sh
# The command below will be printed after you successfully run the log_model.py. run_id will be catched automatically.
# We open the port 5001 since 5000 is already occupied by the mlflow server.
mlflow models serve -m runs:/$run_id/model --no-conda -p 5001
```

5. You can send your queries to the api endpoint. For that i created the `tests/*`. You can run one of them to see if the api is up and running.

```sh
cd tests/
chmod +x curl.sh
./curl.sh    
```
