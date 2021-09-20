#!/bin/bash
docker run --name postgresdb -p 5435:5432 -e POSTGRES_PASSWORD=postgres
python database/init_db.py
source app_env/bin/activate
pip3 install -r requirements.txt
gunicorn app:app -b 0.0.0.0:8000
