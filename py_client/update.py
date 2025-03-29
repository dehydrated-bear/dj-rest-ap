import requests 

endpoint="http://localhost:8000/api/products/1/update"

data={
    "title":"hello world oldie",
    "price":129
}

get_response=requests.put(endpoint,json=data)
print(get_response.json())