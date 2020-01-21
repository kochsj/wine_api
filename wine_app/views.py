from rest_framework import generics
from .models import Bottle
from .serializers import BottleSerializer

# Create your views here.
class BottleList(generics.ListCreateAPIView):
    queryset = Bottle.objects.all()
    serializer_class = BottleSerializer

# class BottleListDetail(generics.ListCreateAPIView):
#     queryset = Bottle.objects.filter('pk')
