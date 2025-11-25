from django.db import models
from django.utils.text import slugify
# Create your models here.

class CategoryModel(models.Model):
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(unique=True,blank=True)
    image = models.FileField(upload_to='Category image/',blank=True,null=True)
    desc = models.TextField()
    color = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        
        super().save(*args,**kwargs)    



class ProductCategoryModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    category = models.ForeignKey(CategoryModel,on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        
        super().save(*args,**kwargs)    

    
class CountryModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,blank=True)
    desc = models.TextField()
    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        
        super().save(*args,**kwargs)
class ProductModel(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,blank=True)
    desc = models.TextField()
    main_image = models.FileField(upload_to='images_main/')
    product_category = models.ForeignKey(CategoryModel,on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.BigIntegerField(default=0)
    country = models.ForeignKey(CountryModel,on_delete=models.CASCADE)
    year = models.SmallIntegerField(default=2025)
    delivery_time = models.CharField(max_length=100)
    review = models.TextField()
    rate = models.SmallIntegerField(default=2)
    company = models.CharField(max_length=150)
    brand = models.CharField(max_length=50)
    size = models.CharField(max_length=500)
    discount = models.SmallIntegerField(default=0)
    color = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    is_recommended = models.BooleanField(default=False)
    condition = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args,**kwargs)    



class ProductImageModel(models.Model):
    image = models.FileField(upload_to="detailed_image_of_product/")
    product = models.ForeignKey(ProductModel)



