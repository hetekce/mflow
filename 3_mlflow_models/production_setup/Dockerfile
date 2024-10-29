# Base image with Python
FROM python:3.11.2-slim

# Install Git
RUN apt-get update && apt-get install -y git

# Install required packages
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy model files into the Docker image
# COPY ./model /app/model

# Copy the source code
COPY src /app/src

COPY startup.sh /app/startup.sh

# Set the working directory
WORKDIR /app

# Expose the port if you're serving the model
EXPOSE 5000 5001 

# Command to run the model
# ENTRYPOINT ["mlflow", "models", "serve", "-m", "/app/model", "--no-conda", "--port", "5001"]

# Set entrypoint to the startup script
ENTRYPOINT ["sh", "/app/startup.sh"]
