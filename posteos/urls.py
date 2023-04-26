from django.urls import path
from posteos import views

urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('about', views.about, name='about'),
]