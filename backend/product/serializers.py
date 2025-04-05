from rest_framework import serializers 
from rest_framework.reverse import reverse

from .models import Product
from .validators import validate_title,unique_product_title

class ProductSerializer(serializers.ModelSerializer):

    #enriching the serializer field with custom names
    get_discount=serializers.SerializerMethodField(read_only=True)
    edit_url=serializers.SerializerMethodField(read_only=True)
    url=serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk'
    )

    title=serializers.CharField(validators=[validate_title,unique_product_title])
    # email=serializers.EmailField(write_only=True)
    class Meta:
        model=Product
        
        fields = [
            'pk',
            'url',
            # 'email',
            'edit_url',
            'title',
            'content',
            'price',
            'sale_price',
            'get_discount'
        ]

#with inline validation you can use self and call request and then with it more stuff is possible 
    # def validate_title(self,value):
    #     request=self.request.get('request')
    #     user=request.user
    #     qs=Product.objects.filter(user=user,title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name ")
    #     return value 


    # def create(self,validated_data):
    #     # return Product.objects.create(**validated_data)
    #     # email=validated_data.pop('email')
    #     obj= super().create(validated_data)
    #     # print(email,obj)
        
    #     return obj
    
    # def update(self,instance,validated_data):
    #     instance.title=validated_data.get('title')
    #     return instance 
    
    def get_edit_url(self,obj):
        request=self.context.get('request')
        # return f"/api/product/{obj.pk}/"
        if request is None:
            return None

        return reverse("product-detail",kwargs={"pk":obj.pk},request=request)

    def get_get_discount(self,obj):

        #obj --> instance
        if not hasattr(obj,'id'):
            return None
        if not isinstance(obj,Product):
            return None
        return obj.discount()
       