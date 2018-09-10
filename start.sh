#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn Server
exec gunicorn aws_poc.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3