import requests

url = "http://localhost:8080/2015-03-31/functions/function/invocations"
src = "https://habrastorage.org/webt/rt/d9/dh/rtd9dhsmhwrdezeldzoqgijdg8a.jpeg"
data = {"url": src}

result = requests.post(url, json=data).json()
print(result)