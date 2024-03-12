# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirimientos file
COPY requirimientos.txt .

# Install any dependencies specified in requirimientos.txt
RUN pip install --trusted-host pypi.python.org -r requirimientos.txt

# Copy the rest of the application code
COPY . .

# Expose port 8000 for the FastAPI application
EXPOSE 8000

# Command to run the application using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
