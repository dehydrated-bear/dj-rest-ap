from rest_framework import serializers 

from .models import Product

class ProductSerializer(serializers.ModelSerializer):

    #enriching the serializer field with custom names
    get_discount=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Product

        fields = [
            'pk',
            'url',
            'title',
            'content',
            'price',
            'sale_price',
            'get_discount'
        ]

    def get_url(self,obj):
        request=self.context.get('request')

    def get_get_discount(self,obj):

        #obj --> instance
        if not hasattr(obj,'id'):
            return None
        if not isinstance(obj,Product):
            return None
        return obj.discount()
       