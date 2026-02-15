# Base Image
FROM python:3.9-slim

# Set up the application directory
WORKDIR /app

# Create a non-root user and grant permissions to the app directory
RUN useradd --create-home appuser && chown -R appuser:appuser /app
USER appuser

# Copy dependencies and install as the non-root user
COPY --chown=appuser:appuser requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code as the non-root user
COPY --chown=appuser:appuser main.py .

# Execution
CMD ["python", "main.py"]
