from django.urls import path
from .views import calculate_morse

urlpatterns=[
    path("",calculate_morse,name='morse-calculate'),
]