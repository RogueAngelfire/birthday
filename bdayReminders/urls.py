from django.urls import path
from .import views


urlpatterns = [
  path('bday/', views.index, name='index'),
]