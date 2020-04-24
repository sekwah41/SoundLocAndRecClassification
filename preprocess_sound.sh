#!/bin/bash

cd src
jupyter nbconvert --to python 1\ Preprocess\ Data.ipynb --output classification_server.py
ipython train_model.py
