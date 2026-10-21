# 🛡️ SecOps HTTP Security Headers Checker

A lightweight, containerized Python CLI tool designed to audit modern HTTP security headers against OWASP recommendations. Built with security best practices, non-root execution, and automated CI/CD pipelines.

---

## 🚀 Key Features

* **Comprehensive Header Audit**: Checks both traditional security headers and modern Cross-Origin isolation policies.
* **CLI Flexibility**: Supports custom input lists (`targets.txt`) and JSON report output.
* **Container Hardening**: Built on a lightweight Alpine Linux image running under a strict **non-root user** (`secopsuser`).
* **CI/CD Automation**: Integrated with GitHub Actions for automated linting, local dry-run tests, and container image builds.

---

## 📋 Checked Security Headers

### Classic Security Headers
* `Strict-Transport-Security` (HSTS)
* `Content-Security-Policy` (CSP)
* `X-Frame-Options`
* `X-Content-Type-Options`
* `X-XSS-Protection`
* `Referrer-Policy`
* `Permissions-Policy`

### Modern Cross-Origin Isolation Policies
* `Cross-Origin-Opener-Policy` (COOP)
* `Cross-Origin-Embedder-Policy` (COEP)
* `Cross-Origin-Resource-Policy` (CORP)

---

## 📁 Project Structure

```
secops-header-checker/
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions CI pipeline
├── checker.py              # Main Python CLI audit script
├── Dockerfile              # Hardened multi-stage/alpine container definition
├── requirements.txt        # Python dependencies
├── targets.txt             # Default list of URLs to scan
└── README.md
```

# ⚙️ Local Installation & Usage
## 1. Clone the repository & set up a virtual environment

git clone [https://github.com/YourUsername/secops-header-checker.git](https://github.com/YourUsername/secops-header-checker.git)
cd secops-header-checker

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## 2. Run the tool locally

python checker.py -i targets.txt -o security_report.json

# 🐳 Docker Usage (Hardened Container)
### Build the Docker image

docker build -t secops-header-checker .

### Run the container

docker run --rm -v $(pwd):/app secops-header-checker -i targets.txt -o security_report.json

# 🔄 CI/CD Pipeline

### The project includes an automated GitHub Actions workflow (.github/workflows/ci.yml) that triggers on every push and pull_request:

    Sets up the Python environment.

    Installs dependencies and runs a dry-run test.

    Builds the hardened Docker image.

    Executes the containerized security audit.

# 🛠️ Tech Stack

    Language: Python 3.11

    Libraries: requests

    Containerization: Docker (Alpine Linux base)

    CI/CD: GitHub Actions