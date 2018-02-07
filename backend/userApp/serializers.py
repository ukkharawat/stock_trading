from rest_framework import serializers
from userApp.models import UserDetail, Portfolio

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = '__all__'

    def create(self, validate_data):
        return UserDetail.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.cash = validate_data.get('cash', instance.cash)
        instance.stepCount = validate_data.get('stepCount', instance.stepCount)
        instance.save() 

        return instance

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'

    def create(self, validate_data):
        return Portfolio.objects.create(**validate_data)

    def update(self, instance, validate_data):
        if validate_data.get('volume', instance.volume) == 0:
            instance.delete()

        else:
            instance.volume = validate_data.get('volume', instance.volume)
            instance.averagePrice = validate_data.get('averagePrice', instance.averagePrice)

            instance.save()

        return instance