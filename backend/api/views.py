from django.http import JsonResponse,HttpResponse
import json
from django.forms.models import model_to_dict
from product.models import Product


def api_home(request,*args,**kwargs):

    model_data=Product.objects.all().order_by("?").first()

    data={}

    if model_data:
        # data["id"]=model_data.id
        # data["title"]=model_data.title
        # data["content"]=model_data.content
        # data["price"]=model_data.price
         
        data=model_to_dict(model_data , fields=['id','title','price'])

    return JsonResponse(data)

        # print(data)
        # print(type(data))

        # # data=dict(data)

        # data['price']=str(data['price'])
        

        # random_name=json.dumps(data)

        # print(random_name[2:9],type(random_name))


    # return HttpResponse(random_name , headers={"content-type":"application/json"})





