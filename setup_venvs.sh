#!/bin/bash

virtualenv venv_4.5.5
source venv_4.5.5/bin/activate
pip install opencv-contrib-python==4.5.5.62
deactivate

virtualenv venv_4.9.0
source venv_4.9.0/bin/activate
pip install opencv-python==4.9.0.80
deactivate