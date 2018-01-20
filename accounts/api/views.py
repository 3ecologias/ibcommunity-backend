from django.contrib.auth import get_user_model

from .serializer import UserCreateSerializer, UserListSerializer, UserSerializer, UserUpdateSerializer

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
)

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
)


User = get_user_model() #Return User Model

class UserCreateAPIView(CreateAPIView):
    """
        API for Create User
    """
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserListAPIView(ListAPIView):
    """
        API for Lister Users
    """
    serializer_class = UserListSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]

class UserDetailAPIView(RetrieveAPIView):
    """
        API for User detail
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]

class UserUpdateAPIVew(UpdateAPIView):
    serializer_class = UserUpdateSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)