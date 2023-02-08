from . import views
from django.urls import path

urlpatterns = [
    path('', views.elevator, name='elevator'),
    path('elevator-moving/<str:lastDemand>', views.moving_elevator, name='elevator-moving'),
    path('resting-elevator/<str:lastDemand>', views.resting_elevator, name='resting-elevator'),
    path('delete/<str:id>', views.del_elevator, name='delete'),
    path('update/<str:id>', views.update_elevator, name='update'),
    path('demans-json/', views.demands_json, name='demans-json'),
]