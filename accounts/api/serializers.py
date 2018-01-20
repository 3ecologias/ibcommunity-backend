from rest_framework import serializers
from django.contrib.auth.models import User
from client.models import Profile, Client

class UserSerializer(serializers.ModelSerializer):

    profile = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all())
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'profile', 'client')
        read_only_fields = ('id',)
