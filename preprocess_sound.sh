#!/bin/bash

cd src || exit
jupyter nbconvert --to python 1\ Preprocess\ Data.ipynb --output preprocess_data.py
ipython preprocess_data.py
