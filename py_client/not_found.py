
import requests

endpoint = "http://localhost:8000/api/products/21314/"
get_responce = requests.get(endpoint)



print(get_responce.json())
