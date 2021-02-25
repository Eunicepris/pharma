from rest_framework import serializers

from .models import Medoc

class MedocSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Medoc
        fields = ('product_name', 'manufacturing_date', 'expiration_date', 'tracking_code', 'producer', 'notice')