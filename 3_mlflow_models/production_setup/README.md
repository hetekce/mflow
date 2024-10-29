# Setting Up Production Environment for MLmodel

0. Supposing that the you are inside the main folder of the repository, lets change the directory to the belowed folder.

```sh
cd 3_mlflow_models/production_setup/
```

1. Start building the model:

```sh
docker build -t my_docker_image:latest .

```

2. Run the container and expose the mlflow server port to 5000 and model port to 5001

```sh
docker run -p 5000:5000 -p 5001:5001 my_docker_image:latest
```

3. You can send your queries to the api endpoint. For that i created the `tests/*`. You can run one of them to see if the api is up and running.

```sh
cd 3_mlflow_models/production_setup/tests/

# To run the api test native from the cli
chmod +x curl.sh
./curl.sh

# To run the api as python subprocess
python curl_api_test.py

# To request the api with native python library with `input_data` parameter, which is the english text to be passed to translate
python api_test.py input_data='It was not easy at all to create the app.'
```
