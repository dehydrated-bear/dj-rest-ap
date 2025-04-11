from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

# import algoliasearch_django as algoliasearch

from .models import Product


# @register(Product)
# class ProductIndex(AlgoliaIndex):
#     fields=[
#         'title',
#         'content',
#         'price',
#         'user__username',
#         'public'
#     ]

@register(Product)
class ProductIndex(AlgoliaIndex):
    should_index="is_public"
    fields = [
        'title',
        'content',
        'price',
        'public'
    ]
    tags='get_tags_list'

    def get_attributes(self, instance):
        return {
            'title': instance.title,
            'content': instance.content,
            'price': float(instance.price),
            'public': instance.public,
            'username': instance.user.username if instance.user else None  
        }

    settings = {
        'searchableAttributes': ['title', 'content', 'username']
    }