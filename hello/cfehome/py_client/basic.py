import requests

#endpoint = "hhtps://httpbin.org/status/200/"
endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.post(endpoint, json={'content':'hola mundo'})

print(get_response.json())