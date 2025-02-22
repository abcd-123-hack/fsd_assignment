# products/views.py
from django.views.generic import ListView
from .models import Category

class CategoryProductListView(ListView):
    model = Category
    template_name = 'products/category_product_list.html'  # Specify your template name
    context_object_name = 'categories'
