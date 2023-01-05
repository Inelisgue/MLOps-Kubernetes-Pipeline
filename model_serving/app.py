from flask import Flask, request, jsonify
import joblib
import pandas as pd
import os

app = Flask(__name__)

# Load the trained model
MODEL_PATH = os.path.join("trained_model", "model.joblib")
model = joblib.load(MODEL_PATH)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json(force=True)
        df = pd.DataFrame(data)
        predictions = model.predict(df).tolist()
        return jsonify({"predictions": predictions})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
