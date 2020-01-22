from django.urls import path
from . import views #. means current directory
#v2
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]