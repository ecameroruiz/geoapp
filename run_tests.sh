#!/usr/bin/env bash
source app_env/bin/activate
pip3.8 install -r requirements.txt
python3.8 -m unittest discover -s tests -p 'tests.py' -v
