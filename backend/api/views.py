from django.http import JsonResponse,HttpResponse
import json
from django.forms.models import model_to_dict
from product.models import Product
from product.serializers import ProductSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST']) 
def api_home(request,*args,**kwargs):
    """DRF api view"""

    instance=Product.objects.all().order_by("?").first()
    # model_data=Product.objects.all().order_by("?").first()

    serializer=ProductSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        
        # instance=serializer.save()
        # print(instance)
        print(serializer.data)
        # data= serializer.data
        

        return Response(serializer.data)
    # return Response({"error":"not good data"})

    

    # data={}

    # if instance:
    #     # data["id"]=model_data.id
    #     # data["title"]=model_data.title
    #     # data["content"]=model_data.content
    #     # data["price"]=model_data.price
         
    #     # data=model_to_dict(model_data , fields=['id','title','price','sale_price'])

    #     instance=ProductSerializer(instance).data

    # return Response(instance)
    
    
    # return JsonResponse(data)

        # print(data)
        # print(type(data))

        # # data=dict(data)

        # data['price']=str(data['price'])
        

        # random_name=json.dumps(data)

        # print(random_name[2:9],type(random_name))


    # return HttpResponse(random_name , headers={"content-type":"application/json"})





