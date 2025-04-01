import requests 



endpoint="http://localhost:8000/api/products/"

headers={'Authorization': 'Bearer 797f101799eb98d79854a62aafd9d9746856b379'}
data={
    'title':"it is done",
    'price':33.99
}
get_response=requests.post(endpoint , json=data,headers=headers)
print(get_response.json())
