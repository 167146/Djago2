import requests
import json

BASE_URL = 'http://127.0.0.1:5000'

# Add a new product
product_data = {
    "name": "Sample Product",
    "description": "This is a test product",
    "price": 19.99
}
response = requests.post(f'{BASE_URL}/products', json=product_data)
print("POST Response:", response.status_code, response.json())

# Retrieve all products
response = requests.get(f'{BASE_URL}/products')
print("GET Response:", response.status_code, json.dumps(response.json(), indent=2))
