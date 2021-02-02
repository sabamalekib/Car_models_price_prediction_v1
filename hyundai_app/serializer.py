from rest_framework import serializers
from . models import Prediction1

class predictionSerializers(serializers.ModelSerializer):
    class Meta:
        model=Prediction1
        fields=('marka','model', 'year', 'engine', 'gearbox', 'transmission', 'ban_type', 
        'fuel_type', 'color', 'used_by_km')