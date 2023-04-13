# Use an official Python runtime as a parent image
FROM python:3.11-slim

# RUN apk update && apk add --no-cache musl-dev g++ lapack-dev openblas-dev gfortran
    # rm -rf /var/cache/apk/*

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt 

# Run app.py when the container launches
CMD ["python", "/app/src/main.py"]
