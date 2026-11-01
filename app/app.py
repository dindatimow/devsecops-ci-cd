
"""Aplikasi web DevSecOps CI/CD dengan monitoring Prometheus."""

from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics
from flask_talisman import Talisman

app = Flask(__name__)

# Mengaktifkan HTTP security headers.
Talisman(
    app,
    force_https=False,
    content_security_policy={
        "default-src": "'self'",
        "object-src": "'none'",
        "frame-ancestors": "'none'",
        "base-uri": "'self'"
    }
)

# Mengaktifkan endpoint metrics untuk Prometheus.
metrics = PrometheusMetrics(app)


@app.route("/")
def home():
    """Menampilkan informasi aplikasi."""
    return jsonify({
        "application": "DevSecOps CI/CD",
        "status": "running",
        "message": "Welcome to the DevSecOps application"
    })


@app.route("/health")
def health():
    """Memeriksa kondisi kesehatan aplikasi."""
    return jsonify({
        "status": "healthy"
    }), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
