FROM python:3.14-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY . .

# Make entrypoint script executable
RUN chmod +x scripts/entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/bin/bash", "scripts/entrypoint.sh"]
