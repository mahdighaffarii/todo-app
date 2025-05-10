# 📝 To-Do List Microservice with Flask, Docker & Kubernetes

This project is a simple microservice built with **Flask (Python)** that allows users to manage a basic To-Do list. It is containerized using **Docker** and deployed to a local Kubernetes cluster via **Minikube**. The project includes a basic HTML interface and supports RESTful API endpoints for task management.

---

## ✨ Features

- RESTful API using Flask
- Lightweight HTML UI for basic interaction
- Containerized using Docker
- Kubernetes-ready deployment (via Minikube)
- Scalable via Deployment replicas
- Health check endpoint
- Ready for CI/CD integration (e.g., GitHub Actions)

---

## 📁 Project Structure

```
todo-app/
├── app.py                # Main Flask application
├── requirements.txt      # Python dependencies
├── Dockerfile            # Docker build configuration
├── deployment.yaml       # Kubernetes Deployment spec
├── service.yaml          # Kubernetes Service spec
└── templates/
    └── index.html        # Simple HTML front-end
```

---

## 🚀 Running Locally (Without Docker)

```bash
pip install -r requirements.txt
python app.py
```

Access at:  
`http://localhost:5000/`

---

## 🐳 Running with Docker

```bash
docker build -t todo-app .
docker run -p 5000:5000 todo-app
```

Access at:  
`http://localhost:5000/`

---

## ☸️ Deploying to Kubernetes with Minikube

### 1. Start Minikube and configure Docker environment:

<details>
<summary>For PowerShell (Windows)</summary>

```powershell
minikube start
minikube -p minikube docker-env | Invoke-Expression
```
</details>

<details>
<summary>For Linux/macOS</summary>

```bash
minikube start
eval $(minikube docker-env)
```
</details>

### 2. Build the Docker image inside Minikube:

```bash
docker build -t todo-app .
```

### 3. Apply Kubernetes manifests:

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### 4. Access the service:

```bash
minikube service todo-service
```

---

## 📦 API Endpoints

| Method | Endpoint         | Description               |
|--------|------------------|---------------------------|
| GET    | `/tasks`         | Retrieve all tasks        |
| POST   | `/tasks`         | Create a new task         |
| GET    | `/tasks/<id>`    | Get a task by ID          |
| DELETE | `/tasks/<id>`    | Delete a task by ID       |
| POST   | `/tasks/<id>`    | Delete task via HTML form |
| GET    | `/health`        | Health check              |
| GET    | `/`              | Simple HTML UI            |

---

## 🖥️ Web Interface

The front-end interface is served at `/` and provides:

- Task creation form
- Task list display
- Inline delete buttons

All interactions are POST-based and managed by Flask templates using `render_template`.

---

## 🛠 Kubernetes Configuration

### `deployment.yaml`
Defines a deployment with:
- 2 replicas
- Container image `todo-app`
- Container port: 5000
- Optional health checks (can be added)

### `service.yaml`
Defines a NodePort service exposing:
- Port 80 (maps to 5000 in pod)
- Access from outside via Minikube’s IP and port

---

## 👨‍💻 Author

Created by Mahdi Ghaffari Cloud Computing - Spring 1404
