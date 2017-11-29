from rest_framework import serializers
from stockApp.models import Stock , StockValue

class StockSerializer(serializers.ModelSerializer):
	class Meta:
		model = Stock
		fields = '__all__'

class StockValueSerializer(serializers.ModelSerializer):
	class Meta:
		model = StockValue
		fields = '__all__'