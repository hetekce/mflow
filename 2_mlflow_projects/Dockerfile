# Base image with Python and ML dependencies
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Default command to prevent container from exiting
CMD ["sleep", "infinity"]
