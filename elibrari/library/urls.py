from django.urls import path
from library import views


urlpatterns = [
    path('', views.index),
    path('registration/', views.register, name='registration'),
    path('reader/', views.reader, name='reader'),
]