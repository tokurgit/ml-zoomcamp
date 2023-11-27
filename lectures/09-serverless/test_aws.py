import requests

url = "https://gi7kj25p48.execute-api.eu-west-1.amazonaws.com/test/predict"
data = {"url": "http://bit.ly/mlbookcamp-pants"}

result = requests.post(url, json=data).json()
print(result)