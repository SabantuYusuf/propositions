from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'), #home is a kwarg
    path('start/', views.start, name='start'),
    path('propositions/', views.start, name='start'),
    
    path('about/', views.about, name='about'),
    

    path('propositions/index', views.index, name='index'),
    
    path('about/', views.about, name='about'),
    # path('propositions/', views.index, name='index'),
    path('propositions/<int:proposition_id>', views.show, name='show'),
]

static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)