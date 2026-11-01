
FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

# Update paket sistem operasi Debian
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Salin dan instal dependensi aplikasi
COPY requirements.txt requirements-prod.txt ./

RUN pip install --no-cache-dir -r requirements-prod.txt \
    && rm -rf /usr/local/lib/python3.14/site-packages/pip \
              /usr/local/lib/python3.14/site-packages/pip-*.dist-info \
              /usr/local/bin/pip \
              /usr/local/bin/pip3 \
              /usr/local/bin/pip3.14

# Salin source code aplikasi
COPY app/ ./app/

# Gunakan user non-root
RUN addgroup --system app \
    && adduser --system --ingroup app app \
    && chown -R app:app /app

USER app

EXPOSE 5000

CMD ["gunicorn", "--no-control-socket", "--bind", "0.0.0.0:5000", "--workers", "2", "app.app:app"]
