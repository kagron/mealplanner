#!/usr/bin/bash

echo "[REACT] Starting $NODE_ENV server."
npm install

if [ ! -d /code/frontend/build ] && [ $NODE_ENV = 'production' ]; then
    echo "[BUILD] Failed to detect build folder. Running yarn build..."
    cd /code/frontend/src
    npm build
fi

npm start
exec "$@"