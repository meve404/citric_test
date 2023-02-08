from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('get-demands/', views.get_demands),
]