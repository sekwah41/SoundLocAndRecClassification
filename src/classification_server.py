
# Not a great framework but helpful for what we need
from flask import Flask, jsonify, request, render_template
app = Flask(__name__)

import sound_predictor
import numpy as np

sound_predictor.load_sound_model('sound_category_model.h5')

# Example payload to air conditioning sample
# {
#     "file_loc": "../resources/UrbanSound8K/audio/fold5/100852-0-0-0.wav"
# }

import traceback

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        json = request.get_json()
        if 'file_loc' in json:
            global sound_predictor
            print('Making predictions')
            print(json['file_loc'])
            try:
                predicted_class, predicted_proba, predicted_vector, label_names =\
                    sound_predictor.prediction(json['file_loc'], False)
                probability = {}
                for i in range(len(label_names)):
                    probability[label_names[i]] = str(predicted_proba[i])
                return jsonify({
                    'predicted_classes': predicted_class.tolist(),
                    'probabilities': probability
                    # 'predicted_proba': predicted_proba.tolist(),
                    # 'predicted_vector': predicted_vector.tolist(),
                    # 'label_names': label_names.tolist()
                })
            except AttributeError as err:
                traceback.print_exc()
                print(err)
                return jsonify({"error": str(err)}), 400
        else:
            return 'Missing file_loc', 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', threaded=False)
