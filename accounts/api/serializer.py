from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from rest_framework.validators import UniqueValidator

from django.contrib.auth.models import User
from client.models import Profile, Client

from rest_framework.serializers import (
    EmailField,
    CharField,
    ModelSerializer,
    PrimaryKeyRelatedField
)

User = get_user_model()

class UserSerializer(ModelSerializer):

    profile = PrimaryKeyRelatedField(queryset=Profile.objects.all())
    client = PrimaryKeyRelatedField(queryset=Client.objects.all())

    class Meta:
        model = User
        fields = ('id', 'email', 'profile', 'client')
        read_only_fields = ('id',)

class UserCreateSerializer(ModelSerializer):
    """
        Create User, username and email Unique and password minimal 8 caracteres
    """
    email = EmailField(label=_('E-mail'), required=True,validators=[UniqueValidator(queryset=User.objects.all())])
    password = CharField(label=_('Password'), min_length=8)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['email'],
             validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'email', 'password')

class UserListSerializer(ModelSerializer):
    """
        List resgistered Users
    """
    class Meta:
        model = User
        fields = ('id', 'email')


class UserUpdateSerializer(ModelSerializer):
    """
        Update registered User
    """
    class Meta:
        model = User
        fields = (
            'password'
        )