from django.urls import path    
from .views import *
urlpatterns = [
    path('',MainPageListView.as_view(),name='home'),
]