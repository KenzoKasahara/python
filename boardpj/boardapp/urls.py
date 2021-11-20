from django.urls import path
from boardapp import views

urlpatterns = [
    path('index/', views.index, name='index'),
]
