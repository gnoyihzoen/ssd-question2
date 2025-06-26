FROM python:3.10-slim

# Install git and bash (for running scripts)
RUN apt-get update && apt-get install -y git bash

# Set work directory
WORKDIR /app

# Copy your app code and git config script
COPY . .

# Run Git setup script
RUN bash git-setup.sh

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Start the web app
CMD ["python", "app.py"]
