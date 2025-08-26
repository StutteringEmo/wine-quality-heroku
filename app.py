from flask import Flask, request, jsonify, render_template_string
import joblib, numpy as np

# Load the trained model
model = joblib.load("wine_quality_model.pkl")

# Order of features must match training data
FEATURE_ORDER = [
    "fixed_acidity", "volatile_acidity", "citric_acid", "residual_sugar",
    "chlorides", "free_sulfur_dioxide", "total_sulfur_dioxide", "density",
    "pH", "sulphates", "alcohol"
]

app = Flask(__name__)

# Browser form route
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        values = [float(request.form[f]) for f in FEATURE_ORDER]
        pred = model.predict(np.array(values).reshape(1, -1))[0]
        return f"<h2>Predicted Wine Quality: {pred:.2f} (rounded → {round(pred)})</h2><a href='/'>Back</a>"
    return render_template_string('''
        <h2>Wine Quality Prediction</h2>
        <form method="post">
        {% for f in features %}
          <label>{{f}}: <input type="number" step="any" name="{{f}}" required></label><br>
        {% endfor %}
        <input type="submit" value="Predict">
        </form>
    ''', features=FEATURE_ORDER)

# JSON API route
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)
    x = [data["features"][k] for k in FEATURE_ORDER] if isinstance(data.get("features"), dict) else data["features"]
    pred = model.predict(np.array(x).reshape(1, -1))[0]
    return jsonify({"prediction": float(pred), "prediction_rounded": int(round(pred))})

if __name__ == "__main__":
    app.run(debug=True)