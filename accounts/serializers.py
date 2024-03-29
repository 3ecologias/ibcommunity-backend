from _ast import Add

from rest_framework import serializers

from django.contrib.auth.models import User

from .models import Profile, Client

from project.models import Project
from address.serializers import AddressSerializer
from address.models import Address


class ProfileSerializer(serializers.ModelSerializer):

    address = AddressSerializer()

    class Meta:
        model = Profile
        fields = ('id', 'user', 'image', 'birth_date', 'is_support', 'is_manager', 'is_admin', 'address',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address = Address.objects.create(**address_data)

        profile = Profile(**validated_data)
        profile.address = address
        profile.save()

        return profile


class ProfileDetailSerializer(serializers.ModelSerializer):

    address = AddressSerializer()

    class Meta:
        model = Profile
        fields = ('id', 'image', 'birth_date', 'address',)
        read_only_fields = ('id',)

    def update(self, instance, validated_data):
        address = instance.address
        address_data = validated_data.get('address')
        address.street = address_data.get('street', address.street)
        address.complement = address_data.get('complement', address.complement)
        address.post_code = address_data.get('post_code', address.post_code)
        address.city = address_data.get('city', address.city)
        address.state = address_data.get('state', address.state)
        address.country = address_data.get('country', address.country)
        address.save()

        instance.image = validated_data.get('image', instance.image)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.address = address
        instance.save()

        return instance


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('id', 'user', 'company')
        read_only_fields = ('id',)

    def create(self, validated_data):

        client = Client.objects.create(**validated_data)

        return client


class ClientDetailSerializer(serializers.ModelSerializer):

    supported_projects = serializers.PrimaryKeyRelatedField(many=True, queryset=Project.objects.all())

    class Meta:
        model = Client
        fields = ('company', 'supported_projects')

    def update(self, instance, validated_data):
        instance.company = validated_data.get('company')
        instance.save()

        return instance


class UserSerializer(serializers.ModelSerializer):

    profile = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all())
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'profile', 'client')
        read_only_fields = ('id',)
