#!/bin/bash

/usr/sbin/nginx

export LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu/

PY=python3
if [[ -z "$WS" || $WS -lt 1 ]]; then
  WS=1
fi

cd /workspace/server

function start_admin(){
    while [ 1 -eq 1 ];do
      $PY -m uvicorn asgi:app --port 8000 > /workspace/logs/run_admin.log 2>&1
    done
}

start_admin &

while [ 1 -eq 1 ];do
    $PY -m uvicorn asgi_front:app --port 8002 | tee /workspace/logs/run_front.log
done

wait;
