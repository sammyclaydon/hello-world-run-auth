import requests

XANO_URL = "https://xj91-rcis-izm2.n2.xano.io/api:7KqKEvF6/gcr_testing"

payload = {"text": "hello world"}

try:
    r = requests.post(XANO_URL, json=payload, timeout=10)
    print("✅ Success:", r.status_code)
    print("Response:", r.text)
except requests.RequestException as e:
    print("❌ Request failed:", e)
