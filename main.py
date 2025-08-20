import os
import requests
from flask import Flask, jsonify

app = Flask(__name__)

XANO_URL = "https://xj91-rcis-izm2.n2.xano.io/api:7KqKEvF6/gcr_testing"

def run_on_startup():
    payload = {"text": "hello world"}
    try:
        r = requests.post(XANO_URL, json=payload, timeout=10)
        print("✅ Success:", r.status_code)
        print("Response:", r.text[:500])
    except requests.RequestException as e:
        print("❌ Request failed:", e)

@app.route("/")
def home():
    return "OK"

@app.route("/health")
def health():
    return jsonify(status="ok"), 200

if __name__ == "__main__":
    run_on_startup()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
