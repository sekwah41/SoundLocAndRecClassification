#!/bin/bash

cd src || exit
jupyter nbconvert --to python 2\ Model\ Training.ipynb --output train_model.py
ipython train_model.py
