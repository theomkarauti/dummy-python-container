# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt into the container and install dependencies
COPY requirements.txt /app/

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files (including dummy.py and dummy.cfg)
COPY . /app/

# Create the logs directory and set permissions
RUN mkdir -p logs && chmod 777 logs

# Expose port 5000 for Flask app (this is the default Flask port)
EXPOSE 5000

# Set environment variables for Flask
ENV FLASK_APP=dummy.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
