# Python Backend with FastAPI

This project is a simple backend application built with FastAPI.
It provides basic API endpoints for managing items and includes a simple frontend-style interface for interacting with the API.

## Project Overview

- Framework: FastAPI
- Language: Python
- Main entry file: main.py
- Dependency file: requirements.txt
- Container support: Dockerfile

## Features

- Get all items
- Get a single item by ID
- Create a new item
- Update an existing item

## Steps Followed

1. Installed Python and verified the local environment.
2. Created a FastAPI application in main.py.
3. Added dependencies in requirements.txt.
4. Ran the app locally with Uvicorn.
5. Added CRUD-style endpoints for items.
6. Created a Dockerfile to containerize the application.
7. Built a Docker image using:
   
   ```bash
   docker build -t python-backend-image .
   ```

## How to Run Locally

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Start the server:

   ```bash
   python -m uvicorn main:app --host 127.0.0.1 --port 8000
   ```

3. Open the browser at:

   ```text
   http://127.0.0.1:8000
   ```

## How to Run with Docker

1. Build the image:

   ```bash
   docker build -t python-backend-image .
   ```

2. Run the container:

   ```bash
   docker run -d -p 8000:8000 --name python-backend python-backend-image
   ```

3. Access the application:

   ```text
   http://localhost:8000
   ```

## Useful Commands

- Stop the container:

  ```bash
  docker stop python-backend
  ```

- Remove the container:

  ```bash
  docker rm python-backend
  ```

- Check running containers:

  ```bash
  docker ps
  ```
