from rest_framework import generics
from rest_framework import mixins

from .serializers import AddressSerializer
from .models import Address


class AddressList(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  generics.GenericAPIView):

    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AddressDetail(mixins.DestroyModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin,
                    generics.GenericAPIView):

    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)