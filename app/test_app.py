
from app.app import app


def test_home_endpoint():
    """Memastikan halaman utama mengembalikan informasi aplikasi."""
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.is_json

    data = response.get_json()
    assert data["application"] == "DevSecOps CI/CD"
    assert data["status"] == "running"
    assert data["message"] == "Welcome to the DevSecOps application"


def test_health_endpoint():
    """Memastikan health check aplikasi berjalan dengan baik."""
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.is_json
    assert response.get_json() == {"status": "healthy"}


def test_metrics_endpoint():
    """Memastikan endpoint metrik Prometheus tersedia."""
    client = app.test_client()
    response = client.get("/metrics")

    assert response.status_code == 200
    assert b"python_info" in response.data or b"process_" in response.data
