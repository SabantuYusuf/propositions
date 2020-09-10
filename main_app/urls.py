from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'), #home is a kwarg
    path('about/', views.about, name='about'),

    path('start/', views.start, name='start'),
    path('propositions/', views.start, name='start'),
    path('propositions/<int:proposition_id>', views.show, name='show'),

    path('propositions/index', views.index, name='index'),
]

static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)