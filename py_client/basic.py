import requests


# endpoint = "http://httpbin.org/status/200/"
# endpoint = "http://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

get_responce = requests.post(endpoint, json={"title":"abc123","content":"Hello World "})
# get_responce = requests.get(endpoint, json={"product_id": 123},)
# json={"query":"Hello World"}

# print(get_responce.headers)
# print(get_responce.text)
# print(get_responce.status_code)


print(get_responce.json())
# print(get_responce.status_code)