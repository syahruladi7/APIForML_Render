from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
import os

# ========================
# Inisialisasi Flask App
# ========================
app = Flask(__name__)

# ========================
# Load Model dan Transformer
# ========================
# Pastikan file .pkl ini berada di folder yang sama dengan app.py
try:
    model = joblib.load("linear_regression_model.pkl")
    transformer = joblib.load("transformer.pkl")
except Exception as e:
    print(f"Error loading model: {e}")

# ========================
# Home Route (Menampilkan HTML)
# ========================
@app.route("/")
def home():
    # Flask akan otomatis mencari file 'index.html' di dalam folder 'templates'
    return render_template("index.html")

# ========================
# Predict Route (API untuk Prediksi)
# ========================
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Mengambil data JSON dari request Frontend
        data = request.get_json()

        # Konversi data ke DataFrame (sesuai format saat training model)
        df = pd.DataFrame([data])

        # Melakukan transformasi data (Encoding/Scaling)
        transformed = transformer.transform(df)

        # Melakukan prediksi menggunakan model
        prediction = model.predict(transformed)

        # Mengembalikan hasil prediksi dalam format JSON
        return jsonify({
            "prediction": float(prediction[0])
        })

    except Exception as e:
        # Mengembalikan pesan error jika terjadi kegagalan
        return jsonify({
            "error": str(e)
        }), 400

# ========================
# Run App
# ========================
if __name__ == "__main__":
    # Mengambil port dari environment variable Render, atau gunakan 5000 untuk lokal
    port = int(os.environ.get("PORT", 5000))
    # Host 0.0.0.0 wajib digunakan agar server Render bisa mendeteksi aplikasi
    app.run(host="0.0.0.0", port=port)
