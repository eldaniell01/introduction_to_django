import requests

headers = {'Authorization': 'Bearer 60591708231d2dc71e2805f8f9e2729518be00aa'}
endpoint = "http://127.0.0.1:8000/api/products/create/"


data = {
   
}

get_response = requests.post(endpoint, json=data, headers=headers)


print(get_response.status_code)
print(get_response.text)
print("Headers:", get_response.headers)

