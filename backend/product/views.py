from rest_framework import generics , mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response

#from django import Http404
from django.shortcuts import  get_object_or_404

# from api.authentication import TokenAuthentication
# from ..api.permission import IsStaffEditorPermissions
from .models import Product
from .serializers import ProductSerializer

from api.mixins import StaffEditorPermissionMixin,UserQuerySetMixin


class ProductListCreateView(
                    UserQuerySetMixin,
                    StaffEditorPermissionMixin,
                    generics.ListCreateAPIView):
    # allow_staff_view=True
    
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    # permission_classes=[permissions.IsAdminUser,IsStaffEditorPermission]
    # authentication_classes=[authentication.SessionAuthentication,
    #                         TokenAuthentication]
 
    def perform_create(self,serializer):
        # serializer.save(user=self.request.user)

        # email=serializer.validated_data.pop("email")
        
        print(serializer.validated_data)
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content') or None

        if content is None:
            content=title
        serializer.save(user=self.request.user,content=content)

    # def get_queryset(self,*args,**kwargs):
    #     qs=super().get_queryset(*args,**kwargs)
    #     request=self.request
    #     user=request.user
    #     if not user.is_authenticated:
    #         return Product.objects.none()
    #     # print(request.user)
    #     return qs.filter(user=request.user)

        #could also send a signal

product_list_create_view=ProductListCreateView.as_view()

# class ProductListAPIView(generics.ListAPIView):
    
#     """not gonna use this??/
#     AS WE CAN USE PRODUCTLISTCREATE VIEW  instead"""

#     queryset=Product.objects.all()

#     serializer_class=ProductSerializer

# product_list_view=ProductListAPIView.as_view()

class ProductUpdateAPIView(UserQuerySetMixin,StaffEditorPermissionMixin,generics.UpdateAPIView):
    queryset=Product.objects.all()

    # permission_classes=[permissions.IsAdminUser,IsStaffEditorPermission]


    serializer_class=ProductSerializer
    lookup_field='pk'
    # permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self,serializer):

        instance=serializer.save()
        if not instance.content:
            instance.content=instance.title

product_update_view=ProductUpdateAPIView.as_view()



class ProductDeleteAPIView(UserQuerySetMixin,StaffEditorPermissionMixin,generics.DestroyAPIView):
    queryset=Product.objects.all()
    # permission_classes=[permissions.IsAdminUser,IsStaffEditorPermission]


    serializer_class=ProductSerializer

    def perform_destroy(self, instance):
        
        
        return super().perform_destroy(instance)

product_delete_view=ProductDeleteAPIView.as_view()



class ProductDetailAPIView(UserQuerySetMixin,StaffEditorPermissionMixin,generics.RetrieveAPIView):
    allow_staff_view=True

    # permission_classes=[permissions.IsAdminUser,IsStaffEditorPermission]

    queryset=Product.objects.all()

    serializer_class=ProductSerializer

    # lookup_field='pk'

product_detail_view=ProductDetailAPIView.as_view()


class ProductMixinView(mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):

    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    # lookup_field="pk"
    
    def get(self,request,*args,**kwargs):
        print(args,kwargs)
        pk=kwargs.get("pk")

        if pk is not None:
            return self.retrieve(request,*args,**kwargs)
        
        return self.list(request,*args,**kwargs)
    
    def post (self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
    def perform_create(self,serializer):
        # serializer.save(user=self.request.user)
        
        print(serializer.validated_data)
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content') or None

        if content is None:
            content="this a single view doing some stuff i guess"
        serializer.save(content=content)
    
    

product_mixin_view=ProductMixinView.as_view()


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
