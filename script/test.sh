#!/bin/bash
source ~/.bashrc
source ./venv/bin/activate

pip3 install pytest
pip3 install coverage
pip3 install Flask
pip3 install requests
python3 -m coverage run -m pytest test/testing.py
python3 -m coverage report -m