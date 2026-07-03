FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    dbus \
    ethtool \
    iproute2 \
    iputils-ping \
    iw \
    network-manager \
    nodejs \
    npm \
    wireless-tools \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
COPY frontend/package.json /app/frontend/

COPY docker/start-dev.sh /usr/local/bin/start-dev.sh

RUN chmod +x /usr/local/bin/start-dev.sh

RUN pip install --no-cache-dir -r /app/requirements.txt

RUN node --version && npm --version

CMD ["python", "backend/app.py"]