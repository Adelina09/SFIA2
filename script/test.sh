#!/bin/bash
source ~/.bashrc
source /var/lib/jenkins/workspace/pipeline/venv/bin/activate

pip install coverage
pip install Flask
pip install requests
python3 -m coverage run -m pytest testing/test.py
python3 -m coverage report -m