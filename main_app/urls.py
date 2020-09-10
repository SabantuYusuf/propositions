from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), #home is a kwarg
    path('propositions/', views.start, name='start'),
    
    path('about/', views.about, name='about'),
    

    path('propositions/index', views.index, name='index'),
    path('propositions/<int:proposition_id>', views.show, name='show'),
]