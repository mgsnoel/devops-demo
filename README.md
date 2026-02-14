# DevOps Demo: Containerised Flask App

A minimal DevOps project demonstrating:
- Docker containerisation
- Local run via port mapping
- (Next) CI/CD with GitHub Actions
- (Next) Infrastructure as Code with Terraform
- (Next) Monitoring with Prometheus + Grafana

## Run locally (Docker)

Build:
```bash
docker build -t devops-demo:1.0 ./app

docker run --rm -p 5050:5000 devops-demo:1.0


## 2) Add a `.dockerignore`

```bash
cat > app/.dockerignore <<'EOF'
__pycache__/
*.pyc
*.pyo
*.pyd
.env
.venv/
.DS_Store
