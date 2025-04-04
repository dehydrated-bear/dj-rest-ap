from django.urls import path 

from . import views

urlpatterns=[
    path('<int:pk>/',views.product_detail_view,name="product-detail"),
    path('<int:pk>/update',views.product_update_view),
    path('<int:pk>/delete',views.product_delete_view),
    path('',views.product_list_create_view,name="product-list"),
]