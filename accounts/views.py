from rest_framework import generics
from rest_framework import mixins

from .models import Profile, Client
from .serializers import UserSerializer, ProfileSerializer, ProfileDetailSerializer,\
    ClientSerializer, ClientDetailSerializer


class UserList(mixins.ListModelMixin,
               generics.GenericAPIView):

    http_method_names = ['get', ]
    queryset = Profile.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UserCreate(mixins.CreateModelMixin,
                 generics.GenericAPIView):
    http_method_names = ['post', ]
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserDetail(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):
    http_method_names = ['get', 'put', 'delete']
    queryset = Profile.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ProfileList(mixins.ListModelMixin,

                  generics.GenericAPIView):

    http_method_names = ['get', ]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ProfileCreate(mixins.CreateModelMixin,
                    generics.GenericAPIView):

    http_method_names = ['post', ]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProfileDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    http_method_names = ['get', 'put', 'delete']
    queryset = Profile.objects.all()
    serializer_class = ProfileDetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ClientList(mixins.ListModelMixin,
                 generics.GenericAPIView):

    http_method_names = ['get',]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ClientCreate(mixins.CreateModelMixin,
                   generics.GenericAPIView):

    http_method_names = ['post',]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ClientDetail(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   generics.GenericAPIView):
    http_method_names = ['get', 'put', 'delete']
    queryset = Client.objects.all()
    serializer_class = ClientDetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
