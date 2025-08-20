import os
import requests
from flask import Flask, jsonify

app = Flask(__name__)

XANO_URL = "https://xj91-rcis-izm2.n2.xano.io/api:7KqKEvF6/gcr_testing"
_ran = False  # flag to prevent multiple calls

def run_on_startup():
    payload = {"text": "hello world 2"}
    try:
        r = requests.post(XANO_URL, json=payload, timeout=10)
        print("✅ Success:", r.status_code)
        print("Response:", r.text[:500])
    except requests.RequestException as e:
        print("❌ Request failed:", e)

@app.before_request
def trigger_once():
    global _ran
    if not _ran:
        run_on_startup()
        _ran = True

@app.route("/")
def home():
    return "OK"

@app.route("/health")
def health():
    return jsonify(status="ok"), 200

if __name__ == "__main__":
    # start the dev server locally
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
