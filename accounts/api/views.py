from django.contrib.auth import get_user_model

from .serializer import UserCreateSerializer, UserListSerializer, UserSerializer, UserUpdateSerializer

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    GenericAPIView,
)

from rest_framework.mixins import (
    CreateModelMixin
)

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
)


User = get_user_model() #Return User Model
class UserCreateAPIView(CreateModelMixin, GenericAPIView):

    http_method_names = ['post', ]
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserListAPIView(ListAPIView):
    """
        API for Lister Users
    """
    http_method_names = ['get', ]
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