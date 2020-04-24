
# Not a great framework but helpful for what we need
from flask import Flask, jsonify, request, render_template
app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        print('Incoming..')
        print(request.get_json())
        return 'OK', 200
