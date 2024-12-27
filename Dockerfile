# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the application code and requirements file to the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask default port
EXPOSE 5050

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5050", "--debug"]

