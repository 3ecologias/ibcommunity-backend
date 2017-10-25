from rest_framework import serializers

from .models import Address


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ('id', 'street', 'complement', 'post_code', 'city', 'state', 'country',)
        read_only_fields = ('id',)
