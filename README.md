# MLOps-Kubernetes-Pipeline

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square&logo=python)](https://www.python.org/)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-1.20%2B-326CE5?style=flat-square&logo=kubernetes)](https://kubernetes.io/)
[![Docker](https://img.shields.io/badge/Docker-20%2B-2496ED?style=flat-square&logo=docker)](https://www.docker.com/)
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-000000?style=flat-square&logo=flask)](https://flask.palletsprojects.com/)

A foundational MLOps pipeline demonstrating continuous integration and deployment of machine learning models using Kubernetes. This project includes model training, containerization, and deployment manifests for scalable inference.

## ✨ Features

-   **Model Training**: Example script for training a simple scikit-learn model.
-   **Model Serving**: A Flask application to serve the trained model via a REST API.
-   **Dockerization**: Dockerfile for containerizing the model serving application.
-   **Kubernetes Manifests**: Deployment, Service, and Ingress configurations for Kubernetes.
-   **Scalable Inference**: Designed for deploying ML models at scale.

## 🚀 Getting Started

### Prerequisites

-   Docker
-   Kubernetes cluster (e.g., Minikube, GKE, EKS, AKS)
-   `kubectl` configured to access your cluster

### Installation and Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Inelisgue/MLOps-Kubernetes-Pipeline.git
    cd MLOps-Kubernetes-Pipeline
    ```

2.  **Train the Model:**
    Navigate to the `model_training` directory and run the training script:
    ```bash
    cd model_training
    pip install -r requirements.txt
    python train.py
    ```
    This will save `model.joblib` in a `trained_model` directory.

3.  **Build Docker Image:**
    Ensure you are in the root of the repository. Build the Docker image for the model serving application. You might need to adjust the image name (`inelisgue/ml-model-server`) to your Docker Hub username or preferred registry.
    ```bash
    docker build -t inelisgue/ml-model-server:latest .
    docker push inelisgue/ml-model-server:latest
    ```

4.  **Deploy to Kubernetes:**
    Apply the Kubernetes manifests. Remember to update the `image` field in `kubernetes/deployment.yaml` if you used a different image name or tag.
    ```bash
    kubectl apply -f kubernetes/deployment.yaml
    kubectl apply -f kubernetes/service.yaml
    kubectl apply -f kubernetes/ingress.yaml
    ```
    *Note: For ingress to work, you need an Ingress Controller installed in your cluster (e.g., Nginx Ingress Controller).* You also need to configure your DNS to point `ml.example.com` to your Ingress Controller's external IP.

### Usage

Once deployed, you can send prediction requests to your model via the Ingress endpoint. For example, if your ingress is configured for `ml.example.com/predict`:

```bash
curl -X POST -H "Content-Type: application/json" -d   '[{"feature1": 0.1, "feature2": 0.2, "feature3": 0.3}, {"feature1": 0.8, "feature2": 0.7, "feature3": 0.9}]'   http://ml.example.com/predict
```

## 📚 Project Structure

```
MLOps-Kubernetes-Pipeline/
├── model_training/         # Scripts and dependencies for model training
│   ├── train.py            # Model training script
│   └── requirements.txt    # Python dependencies for training
├── model_serving/          # Flask application for model serving
│   ├── app.py              # Flask API for predictions
│   ├── Dockerfile          # Dockerfile for containerizing the app
│   └── requirements.txt    # Python dependencies for serving
├── kubernetes/             # Kubernetes deployment manifests
│   ├── deployment.yaml     # Kubernetes Deployment configuration
│   ├── service.yaml        # Kubernetes Service configuration
│   └── ingress.yaml        # Kubernetes Ingress configuration
├── README.md               # Project overview and documentation
└── .gitignore              # Git ignore file
```

## 🤝 Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
