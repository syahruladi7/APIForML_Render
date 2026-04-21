from flask import Flask, request, jsonify
import joblib
import pandas as pd
import os

# ========================
# Inisialisasi Flask App
# ========================
app = Flask(_name_)

# ========================
# Load Model dan Transformer
# ========================
model = joblib.load("linear_regression_model.pkl")
transformer = joblib.load("transformer.pkl")

# ========================
# Home Route
# ========================
@app.route("/")
def home():
    return "APIForML Render Berhasil Jalan!"

# ========================
# Predict Route
# ========================
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # Ubah input ke DataFrame
        df = pd.DataFrame([data])

        # Transform data
        transformed = transformer.transform(df)

        # Prediksi
        prediction = model.predict(transformed)

        return jsonify({
            "prediction": float(prediction[0])
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        })

# ========================
# Run Local / Render
# ========================
if _name_ == "_main_":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
