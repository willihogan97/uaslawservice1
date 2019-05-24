#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn server1.wsgi:application \
    --bind 0.0.0.0:21020 \
    --workers 3