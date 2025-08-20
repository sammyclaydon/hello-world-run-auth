import os
import requests
from flask import Flask

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

if __name__ == "__main__":
    # runs once per container start
    run_on_startup()

    # start HTTP server
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
