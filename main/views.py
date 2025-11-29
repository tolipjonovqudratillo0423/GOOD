from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from .models import ProductModel,CategoryModel,CountryModel,ProductCategoryModel,ProductImageModel
class MainPageListView(ListView):
    template_name = 'index.html'
    model = ProductModel
    context_object_name = 'products'
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        
        data['popular_category'] = CategoryModel.objects.filter(is_active=True).order_by('-view')[:3]
        data['category_all_main'] = CategoryModel.objects.filter(is_active = True)[:7]
        data['category_sub_main'] = CategoryModel.objects.filter(is_active = True)
        data['deals'] = ProductModel.objects.filter(is_active = True).order_by('-discount')[:5]
        
        return data
    