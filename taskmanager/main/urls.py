from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('med', views.med, name='med'),
    path('create', views.create, name='create'),
]