from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('add/',views.add),
    path('sub/',views.sub),
    path('mul/',views.mul),
    path('div/',views.div),
]