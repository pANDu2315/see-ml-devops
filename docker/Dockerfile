# Base image with Python installed
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements file
COPY app/requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy Flask app code
COPY app/ app/

# Copy ML model and related files
COPY ml/ ml/

# Expose Flask port
EXPOSE 5000

# Run the Flask application
CMD ["python", "app/app.py"]
