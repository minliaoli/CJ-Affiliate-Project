from rest_framework import serializers
from offers.models import Offers, Products


# Offer Serializer
class OffersSerializer(serializers.ModelSerializer):
	class Meta:
		model = Offers
		fields = '__all__'

class ProdcuctsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Products
		fields = '__all__'
