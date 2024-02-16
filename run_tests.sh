#!/bin/bash

echo "Running tests on 4.5.5"
source venv_4.5.5/bin/activate
python test_charuco.py --old-api
deactivate

echo ""

echo "Running tests on 4.6.0"
source venv_4.6.0/bin/activate
python test_charuco.py --old-api
deactivate

echo ""

echo "Running tests on 4.8.1"
source venv_4.8.1/bin/activate
python test_charuco.py
deactivate

echo ""

echo "Running tests on 4.9.0"
source venv_4.9.0/bin/activate
python test_charuco.py
deactivate