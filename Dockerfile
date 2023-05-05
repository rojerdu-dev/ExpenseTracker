# Base image on top of a slim Debian-based image (Debian Custer)
FROM python:3.11-slim-buster

# Docker creates a new directory called /app
WORKDIR /app

# copy requirements.txt from local machine to container
# pip install requirements.txt
COPY requirements.txt requirements.txt
RUN pip install --no-chache-dir -r requirements.txt

# copy the rest of the directory from local machine to container
COPY . /app

# Default commands to execute when container runs
CMD ["python", "app.py"]