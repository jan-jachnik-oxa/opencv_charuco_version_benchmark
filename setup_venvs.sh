#!/bin/bash

virtualenv venv_4.5.5
source venv_4.5.5/bin/activate
pip install opencv-contrib-python-headless==4.5.5.62
deactivate

virtualenv venv_4.6.0
source venv_4.6.0/bin/activate
pip install opencv-contrib-python-headless==4.6.0.66
deactivate

virtualenv venv_4.8.1
source venv_4.8.1/bin/activate
pip install opencv-python-headless==4.8.1.78
deactivate

virtualenv venv_4.9.0
source venv_4.9.0/bin/activate
pip install opencv-python-headless==4.9.0.80
deactivate