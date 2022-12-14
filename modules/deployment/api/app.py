
import pickle
from data_science.modelling import SimpleModel
import numpy as np
from flask import Flask, request, jsonify

MODEL = pickle.load(open('./ds/pred_mod, 'rb'))

app = Flask(__name__)

@app.route("/predict", methods=['POST'])
def predict():
    data = request.json

    label = MODEL.predict_with_logging(
        data["idx"],
        pd.DataFrame([data["features"]])
    )

    return {"label": int(label)}
