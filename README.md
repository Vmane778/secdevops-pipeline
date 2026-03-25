# SecDevOps Pipeline

A secure Python Flask application with automated CI/CD pipeline featuring Docker containerization, security scanning, and vulnerability analysis.

## Features

- **Flask Web Application** - Lightweight Python web app running on port 8080
- **Automated CI/CD** - GitHub Actions pipeline with continuous integration
- **Security Scanning** - Trivy vulnerability scanning for Docker images
- **Code Quality** - Flake8 linting for Python code standards
- **Container Registry** - Automatic push to GitHub Container Registry (ghcr.io)
- **Security Reporting** - Results uploaded to GitHub Security tab

## Quick Start

### Prerequisites
- Python 3.9+
- Docker
- pip

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd secdevops-pipeline
```

2. Create a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python main.py
```

The application will be available at `http://localhost:8080`

### Docker

Build and run with Docker:
```bash
docker build -t secdevops-pipeline .
docker run -p 8080:8080 secdevops-pipeline
```

## CI/CD Pipeline

The GitHub Actions workflow (`ci.yml`) automatically:
1. Lints Python code with flake8
2. Builds a Docker image
3. Scans the image for vulnerabilities using Trivy
4. Uploads results to GitHub Security tab
5. Pushes the image to GitHub Container Registry
6. Builds Lambda deployment package
7. Deploys infrastructure using Terraform to AWS Lambda with API Gateway

Triggered on every push to `main` and pull requests.

## Infrastructure as Code

The project uses Terraform to provision cloud infrastructure with security guardrails:

- **AWS Lambda**: Serverless function running the Flask application
- **API Gateway**: HTTP API for accessing the Lambda function
- **IAM Roles/Policies**: Least-privilege access controls
- **KMS Encryption**: Environment variable encryption
- **CloudWatch Logs**: Centralized logging with retention policies

### Guardrails Implemented

- **Security Policies**: IAM roles with minimal required permissions
- **Access Controls**: KMS key policies restricting access to authorized principals
- **Encryption**: Environment variables encrypted with customer-managed KMS keys
- **Logging**: CloudWatch logs with 30-day retention for audit trails
- **Tagging**: Consistent resource tagging for governance

### Deployment

The CI/CD pipeline automatically deploys to AWS on pushes to `main`. To deploy manually:

1. Set up AWS credentials in GitHub Secrets:
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`

2. Ensure you have appropriate AWS permissions for Terraform operations

3. The Terraform configuration is in the `terraform/` directory

4. After deployment, the API Gateway URL will be available in the Terraform outputs

### Guardrails Summary

- **Identity & Access Management**: Least-privilege IAM roles and policies
- **Encryption**: KMS encryption for Lambda environment variables
- **Logging & Monitoring**: CloudWatch logs with 30-day retention
- **API Security**: API Gateway with proper permissions
- **Resource Tagging**: Consistent tagging for governance

## Security

See [SECURITY.md](SECURITY.md) for security policy and vulnerability reporting procedures.

## License

This project is provided as-is for development and educational purposes.
