# Use a lightweight official Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app.py .

# Expose port 8080 for the application
EXPOSE 8080

# Run the app using Gunicorn for production performance
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
