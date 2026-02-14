from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUESTS = Counter("http_requests_total", "Total HTTP requests", ["path"])

@app.get("/")
def home():
    REQUESTS.labels(path="/").inc()
    return "DevOps demo is running ✅\n"

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
