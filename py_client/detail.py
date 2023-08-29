import requests

endpoint = "http://localhost:8000/api/products/7/"

get_responce = requests.get(endpoint)



print(get_responce.json())
