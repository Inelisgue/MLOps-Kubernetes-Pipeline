# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the trained model from the training stage (assuming it's built separately or available)
# For this example, we'll assume the model is copied into the context or pre-exists
# In a real MLOps pipeline, this would come from a model registry or a previous build stage
COPY trained_model/model.joblib ./trained_model/model.joblib

# Copy the model serving application and its requirements
COPY model_serving/requirements.txt ./requirements.txt
COPY model_serving/app.py ./app.py

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]
