import requests


endpoint = "http://127.0.0.1:8000/api/products/create/"

data = {}

get_response = requests.post(endpoint, json=data)


print(get_response.status_code)
print(get_response.text)
print("Headers:", get_response.headers)
try:
    print("JSON:", get_response.json())
except Exception:
    print("⚠️ No se pudo parsear JSON (respuesta vacía o error en servidor)")
