from django.urls import path

from .views import *

urlpatterns = [
    path('', test_page, name='home'),
    path('about/', about, name='about'),
    path('test/', test_page, name='test'),
]