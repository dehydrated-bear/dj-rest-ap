from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

#from django import Http404
from django.shortcuts import  get_object_or_404

from .models import Product
from .serializers import ProductSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    def perform_create(self,serializer):
        # serializer.save(user=self.request.user)
        
        print(serializer.validated_data)
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content') or None

        if content is None:
            content=title
        serializer.save(content=content)

        #could also send a signal

product_list_create_view=ProductListCreateView.as_view()

# class ProductListAPIView(generics.ListAPIView):
    
#     """not gonna use this??/
#     AS WE CAN USE PRODUCTLISTCREATE VIEW  instead"""

#     queryset=Product.objects.all()

#     serializer_class=ProductSerializer

# product_list_view=ProductListAPIView.as_view()

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset=Product.objects.all()

    serializer_class=ProductSerializer
    lookup_field='pk'

    def perform_update(self,serializer):

        instance=serializer.save()
        if not instance.content:
            instance.content=instance.title

product_update_view=ProductUpdateAPIView.as_view()



class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset=Product.objects.all()

    serializer_class=ProductSerializer

product_detail_view=ProductDetailAPIView.as_view()



class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset=Product.objects.all()

    serializer_class=ProductSerializer

    # lookup_field='pk'

product_detail_view=ProductDetailAPIView.as_view()

@api_view(['GET',"POST"])
def product_alt_view(request,pk=None,*args,**kwargs):
    method=request.method

    if  method=="GET":
        #get request data, or maybe list view
        if pk  is not None:

            obj=get_object_or_404(Product,pk=pk)
            data=ProductSerializer(obj,many=False).data
            
            # queryset=Product.objects.filter(pk=pk)

            # if not queryset.exist():
            #     raise Http404

            return Response(data)
            #detailviewq
        else:
            queryset=Product.objects.all()
            data=ProductSerializer(queryset,many=True).data
            return Response(data)
    

    if method=="POST":
        #create an item
        serializer=ProductSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):

            title=serializer.validated_data.get('title')
            content=serializer.validated_data.get('content') or None

            if content is None:
                content=title
            serializer.save(content=content)
            
            # instance=serializer.save()
            # print(instance)
            print(serializer.data)
            # data= serializer.data
        

        return Response(serializer.data)
