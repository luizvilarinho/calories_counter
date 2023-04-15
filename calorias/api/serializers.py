from rest_framework import serializers
from api.models import Calories

class CaloriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calories
        fields = ['alimento', 'cal', 'p', 'c', 'g', 'f']

class AlimentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calories
        fields = '__all__'
