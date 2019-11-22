from offers.models import Offers, Products
from rest_framework import viewsets, permissions
from .serializers import OffersSerializer, ProdcuctsSerializer
from .pyrebase_settings import db


#Offer Viewset
class OffersViewset(viewsets.ModelViewSet):
	queryset = Offers.objects.all()
	permission_classer = [
		permissions.AllowAny
	]
	serializer_class = OffersSerializer

class ProductsViewset(viewsets.ModelViewSet):
	queryset = Products.objects.all()
	permission_classer = [
		permissions.AllowAny
	]
	serializer_class = ProdcuctsSerializer
