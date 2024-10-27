from mlflow import log_metric, log_param, log_artifact


if __name__ == '__main__':
    log_param("treshold_value", 3)
    log_param('verbosity_value', "DEBUG")
    
    log_metric("ts", 20000)
    log_metric('ttc', 123)
    
    log_artifact("1_installing_mlflow/dataset.csv")