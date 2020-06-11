from rest_framework import serializers
from mainapp.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('email', 'mobN', 'agent', 'contract')
