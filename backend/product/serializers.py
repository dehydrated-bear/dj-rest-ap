from rest_framework import serializers 
from rest_framework.reverse import reverse


from api.serializers import UserPublicSerializers
from .models import Product
from .validators import unique_product_title


class ProductInlineSerializer(serializers.Serializer):
    url=serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
        read_only=True
    )
    title=serializers.CharField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):

    #enriching the serializer field with custom names
    owner=UserPublicSerializers(source="user",read_only=True)
   
    edit_url=serializers.SerializerMethodField(read_only=True)
    url=serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk'
    )

    title=serializers.CharField(validators=[unique_product_title])
    
    class Meta:
        model=Product
        
        fields = [
            'owner',
            'pk',
            'url',
            
            'edit_url',
            'title',
            'content',
            'price',
            'sale_price',
            'public',
            
        ]

    def get_my_user_data(self,obj):
            return {
                "username":obj.user.username
            }

#with inline validation you can use self and call request and then with it more stuff is possible 
    
    
    def get_edit_url(self,obj):
        request=self.context.get('request')
        # return f"/api/product/{obj.pk}/"
        if request is None:
            return None

        return reverse("product-detail",kwargs={"pk":obj.pk},request=request)

    
       