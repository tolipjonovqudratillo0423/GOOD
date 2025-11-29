from django.contrib import admin

from .models import *

@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['title','slug','color','is_active']
    search_fields = ['title','desc']
    list_filter = ['is_active','color']
    prepopulated_fields = {'slug':('title',)}
    list_editable = ['is_active',]
    
@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['name','slug','color','is_active']
    search_fields = ['name','desc']
    list_filter = ['is_active','color']
    prepopulated_fields = {'slug':('name',)}
    list_editable = ['is_active']

@admin.register(ProductCategoryModel)
class ProductCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['name','category','slug','is_active']
    search_fields = ['name','desc']
    list_filter = ['is_active',]
    prepopulated_fields = {'slug':('name',)}
    list_editable = ['is_active',]
    
@admin.register(CountryModel)
class CountryModelAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    search_fields = ['name',]
    prepopulated_fields = {'slug':('name',)}
    

