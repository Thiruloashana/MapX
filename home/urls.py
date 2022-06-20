from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepagee,name='home-homepagee'),
]
