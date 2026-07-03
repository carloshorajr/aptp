#!/bin/sh

set -e

echo "==> Starting APTP development environment..."

cd /app/frontend

if [ ! -d node_modules ]; then
    echo "==> Installing frontend dependencies..."
    npm install
else
    echo "==> Frontend dependencies already installed."
fi

cd /app

echo "==> Starting Flask..."

echo "==> Starting Tailwind watcher..."

npm run watch &

cd /app

echo "==> Starting Flask..."

exec flask \
    --app backend.app \
    run \
    --host=0.0.0.0 \
    --port=8080 \
    --debug