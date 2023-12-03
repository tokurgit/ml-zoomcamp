import requests

# url = "http://localhost:9696/predict"
# url = "http://localhost:8080/predict"
url = "http://ae501790ab8b1430f99c32cc3c1a02d6-1576033030.eu-west-1.elb.amazonaws.com/predict"
data = {"url": "http://bit.ly/mlbookcamp-pants"}

result = requests.post(url, json=data).json()
print(result)