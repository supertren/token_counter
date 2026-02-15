# Base Image
FROM python:3.9-slim

# Working Directory
WORKDIR /app

# Dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create a non-root user
RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser

# Application Code
COPY main.py .

# Execution
CMD ["python", "main.py"]
