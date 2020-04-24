#!/bin/bash

cd src
jupyter nbconvert --to python 2\ Model\ Training.ipynb --output classification_server.py
ipython classification_server.py
