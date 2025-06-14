# LLM-Pipeline
# CI/CD Pipeline for LLM-Powered Application on Google Cloud Run

![CI/CD Pipeline Diagram Placeholder](https://via.placeholder.com/800x400?text=CI/CD+Pipeline+Diagram)
*(Consider adding a simple diagram here later, showing GitHub -> GitHub Actions -> Artifact Registry -> Cloud Run)*

## 🚀 Project Overview

This project demonstrates the implementation of a Continuous Integration/Continuous Deployment (CI/CD) pipeline for a simple LLM-powered API application. The pipeline automates the process of building, testing, and deploying the application to Google Cloud Run whenever new code changes are pushed to the `main` branch of this GitHub repository.

This showcases a critical aspect of MLOps: **operationalizing advanced AI models** with robust, automated software engineering practices.

## ✨ What This Project Demonstrates

By successfully completing this project, I've gained hands-on experience and demonstrated proficiency in:

* **Generative AI / LLM Application Development:** Building a basic API that interacts with a Large Language Model.
* **Robust API Design:** Implementing a simple RESTful API using Flask/Gunicorn.
* **Containerization (Docker):** Packaging the application into a portable Docker image for consistent deployment.
* **CI/CD Tooling (GitHub Actions):** Automating the build, push, and deployment process based on Git events.
* **Cloud Platforms (GCP):** Utilizing key Google Cloud services for MLOps:
    * **Artifact Registry:** For managing Docker container images.
    * **Cloud Run:** For deploying scalable, serverless containerized applications.
    * **Service Accounts & IAM:** For secure authentication and authorization within GCP.
* **Version Control Best Practices:** Using Git and GitHub for collaborative development and automated workflows.
* **Problem-Solving & Troubleshooting:** Navigating and resolving various real-world deployment challenges in a cloud environment.

## 🏗️ Architecture & Workflow

The CI/CD pipeline follows these steps:

1.  **Code Commit:** Developer pushes code changes to the `main` branch of this GitHub repository.
2.  **CI Trigger:** GitHub Actions detects the push and triggers the `deploy-cloud-run.yml` workflow.
3.  **Build Docker Image:** GitHub Actions executes Docker commands to build the application's Docker image.
4.  **Push to Artifact Registry:** The newly built Docker image is pushed to Google Cloud Artifact Registry.
5.  **Deploy to Cloud Run:** GitHub Actions then uses `gcloud` commands to deploy the latest Docker image to the specified Cloud Run service. Cloud Run automatically manages the infrastructure, scaling, and HTTPS.
6.  **API Available:** The LLM API is now updated and accessible via its Cloud Run URL.

## 🚀 Getting Started

Follow these steps to set up and run this CI/CD pipeline in your own GCP project.

### Prerequisites

* **Google Cloud Platform (GCP) Project:** An active GCP account with billing enabled.
* **GCP APIs Enabled:**
    * `Cloud Run API`
    * `Artifact Registry API`
    * `Cloud Build API` (used by GitHub Actions for GCP integration)
* **GitHub Account:** And a new, empty repository (this one, once cloned).
* **Docker Desktop:** Installed and running locally (for optional local testing).
* **LLM API Key:** An API key for an LLM service (e.g., OpenAI API Key, Gemini API Key).

### 1. Local Application Setup

Clone this repository and set up the basic Flask application.

```bash
# Clone the repository
git clone [https://github.com/YOUR_GITHUB_USERNAME/llm-cicd-demo.git](https://github.com/YOUR_GITHUB_USERNAME/llm-cicd-demo.git)
cd llm-cicd-demo

# Create a Python virtual environment
python -m venv venv
source venv/bin/activate # On Linux/macOS
# .\venv\Scripts\activate # On Windows

# Install Python dependencies
pip install -r requirements.txt

# --- Configure LLM API Key (for local testing ONLY) ---
# Create a .env file in the root of the project (add it to .gitignore!)
echo "OPENAI_API_KEY=sk-YOUR_ACTUAL_OPENAI_API_KEY_HERE" > .env
# OR for Gemini:
# echo "GEMINI_API_KEY=YOUR_ACTUAL_GEMINI_API_KEY_HERE" > .env

# --- Optional: Test the application locally ---
python app.py
# Open your browser to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
# Use curl or Postman to test the /generate endpoint with a POST request:
# curl -X POST -H "Content-Type: application/json" -d '{"prompt": "Tell me a joke."}' [http://127.0.0.1:5000/generate](http://127.0.0.1:5000/generate)
