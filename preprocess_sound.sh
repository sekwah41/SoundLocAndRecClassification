#!/bin/bash

cd src
jupyter nbconvert --to python 1\ Preprocess\ Data.ipynb --output preprocess_data.py
ipython preprocess_data.py
