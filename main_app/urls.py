from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'), #home is a kwarg
    path('about/', views.about, name='about'),
    path('start/', views.start, name='start'),
    
    path('propositions/', views.index, name='index'),
    path('propositions/<int:proposition_id>', views.show, name='show'),
]

static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)