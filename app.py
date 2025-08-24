from flask import Flask, request, jsonify
import joblib, numpy as np

# Load the trained model
model = joblib.load("wine_quality_model.pkl")

# Order of features must match training data
FEATURE_ORDER = [
    "fixed_acidity","volatile_acidity","citric_acid","residual_sugar",
    "chlorides","free_sulfur_dioxide","total_sulfur_dioxide","density",
    "pH","sulphates","alcohol"
]

app = Flask(__name__)

@app.route("/")
def home():
    return "Wine Quality Prediction API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)
    if isinstance(data.get("features"), dict):
        x = [data["features"][k] for k in FEATURE_ORDER]
    else:
        x = data["features"]
    pred = model.predict(np.array(x).reshape(1, -1)).tolist()[0]
    return jsonify({"prediction": pred})

if __name__ == "__main__":
    app.run(debug=True)