import librosa
import librosa.display
import numpy as np
import tensorflow as tf
from keras.models import load_model
import pickle

compute_device = None

# Setup extraction
num_rows = 40
num_columns = 174
num_channels = 1

max_pad_len = 174

model = None

from datetime import datetime

def prediction(file_name, print_data = False):
    prediction_feature = extract_features(file_name)
    prediction_feature = prediction_feature.reshape(1, num_rows, num_columns, num_channels)

    predicted_vector = model.predict_classes(prediction_feature)
    predicted_proba_vector = model.predict_proba(prediction_feature)

    predicted_class = le.inverse_transform(predicted_vector)
    predicted_proba = predicted_proba_vector[0]
    if print_data:
        print("The predicted class is:", predicted_class[0], '\n')

        for i in range(len(predicted_proba)):
            category = le.inverse_transform(np.array([i]))
            print(category[0], "\t\t : ", format(predicted_proba[i], '.32f') )
    #return (predicted_class[0], format(predicted_proba[predicted_vector[0]] * 100, '.32f'))
    return (predicted_class, predicted_proba, predicted_vector, label_names)

def load_sound_model(model_loc):
    global model
    if model != None:
        del model
    model = load_model(model_loc)

def extract_features(file_name):

    try:
        audio, sample_rate = librosa.load(file_name, res_type='kaiser_fast')
        mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
        pad_width = max_pad_len - mfccs.shape[1]
        mfccs = np.pad(mfccs, pad_width=((0, 0), (0, pad_width)), mode='constant')

    except Exception as e:
        print("Error encountered while parsing file: ", file_name, e)
        return None

    return mfccs

# Load model and label encoder
sound_model_file = "sound_category_model"
label_encoder_file = "labelencoder.pkl"

with open(label_encoder_file, 'rb') as file:
    le = pickle.load(file)

label_names = le.classes_

num_labels = len(le.classes_)

print("Labels Loaded:", num_labels)
