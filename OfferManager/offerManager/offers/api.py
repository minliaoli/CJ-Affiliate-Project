from offers.models import Offers
from rest_framework import viewsets, permissions
from .serializers import OffersSerializer

#Offer Viewset
class OffersViewset(viewsets.ModelViewSet):
	queryset = Offers.objects.all()
	permission_classer = [
		permissions.AllowAny
	]
	serializer_class = OffersSerializer