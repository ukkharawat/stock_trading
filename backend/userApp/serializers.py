from rest_framework import serializers
from userApp.models import UserDetail, Portfolio

class UserDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    username = serializers.CharField(max_length = 30)
    cash = serializers.FloatField()
    stepCount = serializers.IntegerField()

    def create(self, validate_data):
        return UserDetail.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.cash = validate_data.get('cash', instance.cash)
        instance.stepCount = validate_data.get('stepCount', instance.stepCount)

        instance.save()

        return instance

class PortfolioSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    username = serializers.CharField(max_length = 30)
    date = serializers.DateField()
    symbol = serializers.CharField()
    volume = serializers.IntegerField()
    averagePrice = serializers.FloatField()

    def create(self, validate_data):
        return Portfolio.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.date = validate_data.get('date', instance.date)
        instance.volume = validate_data.get('volume', instance.volume)
        instance.averagePrice = validate_data.get('averagePrice', instance.averagePrice)

        instance.save()

        return instance