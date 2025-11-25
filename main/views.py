from django.shortcuts import render
from django.views.generic import DetailView,ListView
# Create your views here.
from .models import ProductModel,CategoryModel,CountryModel,ProductCategoryModel,ProductImageModel
class MainPageListView(ListView):
    template_name = 'index.html'
    model = ProductModel,CategoryModel,CountryModel,ProductCategoryModel,ProductImageModel
    context_object_name = 'products'
    