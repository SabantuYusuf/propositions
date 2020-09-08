from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), #home is a kwarg
    path('about/', views.about, name='about'), #about is a kwarg
]