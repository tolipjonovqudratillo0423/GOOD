from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth import get_user_model
# Create your views here.
class MainProfileView(DetailView):
    template_name = 'accounts/profile'
    model = get_user_model()
    context_object_name = 'user'
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['user'] = get_user_model().objects.all()
