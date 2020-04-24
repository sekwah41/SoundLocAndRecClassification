#!/bin/bash

cd src
jupyter nbconvert --to python 2\ Model\ Training.ipynb --output train_model.py
ipython train_model.py
