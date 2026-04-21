import os

if __name__ == "__main__":
    # Render akan memberikan port melalui os.environ.get('PORT')
    # Gunakan 5000 sebagai fallback untuk lokal
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
