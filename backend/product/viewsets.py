from rest_framework import viewsets ,mixins
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    '''
    get->list->queryset
    get->retrive->Product Instance Detail View
    post->create ->New instance
    put->Update
    patch->Partial Update
    delete->destroy
    '''
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    look_field="pk"#defaultt bruh




class ProductGenericViewSet(
        viewsets.GenericViewSet,
        mixins.RetrieveModelMixin,
        mixins.ListModelMixin):
    '''
    get->list->queryset
    get->retrive->Product Instance Detail View
    #being treated as doc string??

    '''
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_filed='pk'#def
    
# product_list_view=ProductGenericViewSet.as_view({'get':'list'})

# product_detail_view=ProductGenericViewSet.as_view({'get':''
# 'retrive'})
 


