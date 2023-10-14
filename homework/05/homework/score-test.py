import requests

client = {
    "job": "retired",
    "duration": 445,
    "poutcome": "success",
}

host = "0.0.0.0"
port = "1234"
url = f"http://{host}:{port}/score"

res = requests.post(url, json=client)

print()
print()
print(res.json())
print()
print()
