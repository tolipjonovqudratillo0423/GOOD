from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import BaseUserManager,AbstractUser,PermissionsMixin
# Create your models here.

from django.db import models


# =======================
# BRAND CHOICES
# =======================
class BrandChoices(models.TextChoices):
    APPLE = "apple", "Apple"
    SAMSUNG = "samsung", "Samsung"
    XIAOMI = "xiaomi", "Xiaomi"
    LENOVO = "lenovo", "Lenovo"
    HUAWEI = "huawei", "Huawei"
    ASUS = "asus", "ASUS"
    NIKE = "nike", "Nike"
    ADIDAS = "adidas", "Adidas"
    PUMA = "puma", "Puma"
    ZARA = "zara", "Zara"
    HM = "hm", "H&M"
    SONY = "sony", "Sony"
    LG = "lg", "LG"
    GUCCI = "gucci", "Gucci"
    PRADA = "prada", "Prada"
    TESLA = "tesla", "Tesla"


# =======================
# COLOR CHOICES
# =======================
class ColorChoices(models.TextChoices):
    BLACK = "black", "Black"
    WHITE = "white", "White"
    RED = "red", "Red"
    BLUE = "blue", "Blue"
    GREEN = "green", "Green"
    YELLOW = "yellow", "Yellow"
    ORANGE = "orange", "Orange"
    PURPLE = "purple", "Purple"
    BROWN = "brown", "Brown"
    GRAY = "gray", "Gray"
    GOLD = "gold", "Gold"
    SILVER = "silver", "Silver"


# =======================
# CONDITION CHOICES
# =======================
class ConditionChoices(models.TextChoices):
    NEW = "new", "Brand New"
    LIKE_NEW = "like_new", "Like New"
    REFURBISHED = "refurbished", "Refurbished"
    USED = "used", "Used"
    DAMAGED = "damaged", "Damaged"


# =======================
# DELIVERY TIME CHOICES
# =======================
class DeliveryTimeChoices(models.TextChoices):
    THREE_DAYS = "3_days", "1–3 days"
    FIVE_DAYS = "5_days", "3–5 days"
    WEEK = "1_week", "5–7 days"
    TWO_WEEKS = "2_weeks", "1–2 weeks"
    MONTH = "1_month", "2–4 weeks"


# =======================
# SIZE CHOICES
# =======================
class SizeChoices(models.TextChoices):
    XS = "xs", "XS"
    S = "s", "S"
    M = "m", "M"
    L = "l", "L"
    XL = "xl", "XL"
    XXL = "xxl", "XXL"
    XXXL = "xxxl", "3XL"

    SIZE_36 = "36", "36"
    SIZE_37 = "37", "37"
    SIZE_38 = "38", "38"
    SIZE_39 = "39", "39"
    SIZE_40 = "40", "40"
    SIZE_41 = "41", "41"
    SIZE_42 = "42", "42"
    SIZE_43 = "43", "43"
    SIZE_44 = "44", "44"


class   CategoryModel(models.Model):
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(unique=True,blank=True)
    image = models.FileField(upload_to='Category image/',blank=True,null=True)
    desc = models.TextField()
    view = models.PositiveBigIntegerField()
    color = models.CharField(max_length=50,choices=ColorChoices,default=ColorChoices.BLACK)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        
        super().save(*args,**kwargs)    



class ProductCategoryModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,blank=True)
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
    delivery_time = models.CharField(max_length=100,choices=DeliveryTimeChoices.choices, default=DeliveryTimeChoices.THREE_DAYS)
    review = models.TextField()
    rate = models.SmallIntegerField(default=2)
    company = models.CharField(max_length=150)
    brand = models.CharField(max_length=50,choices=BrandChoices.choices,default=BrandChoices.GUCCI)
    size = models.CharField(max_length=500,choices=SizeChoices.choices,default=SizeChoices.XS)
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
    product = models.ForeignKey(ProductModel,on_delete=models.CASCADE)  



# class UserManagerModel(BaseUserManager):
#     def create_user(self,username,password=None,email=None,phone=None,**extra_fields):

#         user = self.model(username=username,phone=phone,email=email,**extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#     def create_superuser(self,username,password=None,email=None,phone=None,**extra_fields):
#         extra_fields.setdefault('is_staff',True)
#         extra_fields.setdefault('is_superuser',True)
#         extra_fields.setdefault('is_active',True)
#         return self.create_user(self,username=username,password=password,email=email,phone=phone,**extra_fields)

# class UserModel(AbstractUser):
    
#     phone = models.CharField(max_length=50)

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email','phone']
