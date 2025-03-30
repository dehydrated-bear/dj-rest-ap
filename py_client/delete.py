import requests 

primk=input("enter the pk value:\n")



try:
    primk=int(primk)
    
except:
    primk=None
    print(f"{primk} is not a real value!")


if primk:
    endpoint=f"http://localhost:8000/api/products/{primk}/delete"

    get_response=requests.delete(endpoint)
    print(get_response.status_code,get_response.status_code==204)