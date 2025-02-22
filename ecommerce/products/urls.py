# products/urls.py
from django.urls import path
from .views import CategoryProductListView

urlpatterns = [
    path('', CategoryProductListView.as_view(), name='category-product-list'),
]
