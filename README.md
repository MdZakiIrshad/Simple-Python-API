# Python Backend with FastAPI

This project is a simple backend application built with FastAPI.
It provides basic API endpoints for managing items and includes a simple frontend-style interface for interacting with the API.

## Project Overview

- Framework: FastAPI
- Language: Python
- Main entry file: main.py
- Dependency file: requirements.txt
- Container support: Dockerfile
- Kubernetes manifests: k8s/
- Helm chart: helm/python-backend/

## Features

- Get all items
- Get a single item by ID
- Create a new item
- Update an existing item
- Containerize the app with Docker
- Deploy the app with Kubernetes and Helm

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
8. Added Kubernetes deployment and service manifests in the k8s folder.
9. Added a Helm chart under helm/python-backend for deployment management.
10. Tested deployment locally using Minikube and exposed the service.

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

## Kubernetes Deployment

1. Apply the deployment:

   ```bash
   kubectl apply -f k8s/deployment.yaml
   ```

2. Apply the service:

   ```bash
   kubectl apply -f k8s/service.yaml
   ```

3. Check the status:

   ```bash
   kubectl get pods
   kubectl get svc
   ```

4. Access the app through the NodePort service.

## Helm Deployment

1. Lint the Helm chart:

   ```bash
   helm lint helm/python-backend
   ```

2. Install the release:

   ```bash
   helm install my-release helm/python-backend
   ```

3. Expose the service in Minikube:

   ```bash
   minikube service my-release-python-backend-service --url
   ```

4. Upgrade the release later if needed:

   ```bash
   helm upgrade my-release helm/python-backend
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

- Check running pods:

  ```bash
  kubectl get pods
  ```
