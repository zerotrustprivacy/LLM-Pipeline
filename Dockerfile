# Dockerfile
# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster 

# Set the working directory in the container
WORKDIR /app

# Install any dependencies specified in requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose the port that the app runs on
EXPOSE 8080

# Run the Flask app with Gunicorn
# Gunicorn is recommended for production. It uses the PORT env var set by Cloud Run.
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
