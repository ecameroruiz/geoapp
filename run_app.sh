#!/bin/bash
docker run -d --name postgresdb -p 5435:5432 -e POSTGRES_PASSWORD=postgres pgrouting/pgrouting:11-2.5-2.6.3
docker exec -it postgresdb psql -h localhost -U postgres -c "CREATE EXTENSION postgis;"
./database/init_db.py
python3.8 -m venv app_env
source app_env/bin/activate
pip3.8 install -r requirements.txt
gunicorn app:app -b 0.0.0.0:8000