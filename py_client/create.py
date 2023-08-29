import requests

endpoint = "http://localhost:8000/api/products/"
data = {
    "title":"This mixin adding",
    "price": 38.99
}
get_responce = requests.post(endpoint,json=data)



print(get_responce.json())
