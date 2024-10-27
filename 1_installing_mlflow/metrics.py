from random import choice
from mlflow import log_metric

metrics = ['ram', 'memory', 'storage', 'accuracy']

percentages = [el for el in range(0, 100)]

for _ in range(80):
    log_metric(choice(metrics), choice(percentages))