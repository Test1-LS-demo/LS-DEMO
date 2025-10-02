# Vulnerable Dockerfile for demo purposes
FROM python:3.7-slim

# Security misconfiguration: Running as root
USER root

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Security misconfiguration: Exposing sensitive files
COPY /etc/passwd /app/passwd

# Security misconfiguration: Using outdated base image
# python:3.7-slim is EOL

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
