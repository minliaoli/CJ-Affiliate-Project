from rest_framework import serializers
from offers.models import Offers

# Offer Serializer
class OffersSerializer(serializers.ModelSerializer):
	class Meta:
		model = Offers
		fields = '__all__'
