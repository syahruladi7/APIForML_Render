from flask import Flask
import joblib
import pandas as pd
import os

app = Flask(_name_)

@app.route('/')
def home():
    return "API ML Berjalan!"

if _name_ == "_main_":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
