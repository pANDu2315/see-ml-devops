# Base image with Python installed
FROM python:3.12-slim

# Install minimal runtime dependencies required by OpenCV
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    libxcb1 \
    && rm -rf /var/lib/apt/lists/*

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
