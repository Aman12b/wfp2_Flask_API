# Use the official Python image as a base
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt (if you have it) and the rest of your app
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Expose the port Flask will run on (5000 by default)
EXPOSE 8080

# Command to run the Flask app
CMD ["python", "main.py"]
