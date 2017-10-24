from rest_framework import serializers
from .models import Profile, Client


class ProfileSerializer(serializers.ModelSerializer):
    model = Profile
    fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    model = Client
    fields = "__all__"
