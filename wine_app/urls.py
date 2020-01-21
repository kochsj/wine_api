from django.urls import path
from .views import BottleList

urlpatterns = [
    path('bottle/', BottleList.as_view(), name='bottle_list'),
]