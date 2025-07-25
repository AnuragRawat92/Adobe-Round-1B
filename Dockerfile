# Use official Python image
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Copy the project files
COPY . .

# Upgrade pip
RUN pip install --upgrade pip

# Install dependencies
RUN pip install -r requirements.txt

# Set environment variables (optional)
ENV PYTHONUNBUFFERED=1

# Default command
CMD ["python", "-m", "src.main"]
