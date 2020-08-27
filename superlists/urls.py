from django.urls import path
from . import views

urlpatterns = [
        path('superlists', views.home_page, name='home'),
        ]


