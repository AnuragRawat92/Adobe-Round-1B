# Use official Python slim image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy only requirements first to leverage Docker layer caching
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Now copy the rest of the code
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Default execution command
CMD ["python", "-m", "src.main"]
