# Use secure and minimal base image
FROM python:3.11-alpine

# Set working directory
WORKDIR /app

# Install build dependencies (required for some packages)
RUN apk add --no-cache gcc musl-dev libffi-dev make

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your app code
COPY . .

# Expose port
EXPOSE 8000

# Run FastAPI with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
