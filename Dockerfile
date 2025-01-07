FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy files
COPY . /app

# Install the dependencies
RUN pip install -r requiremnts.txt

# Expose port 5000
EXPOSE 5000

# Start the app
CMD ["python", "app.py"]
