from rest_framework import generics, mixins, permissions
from accounts.permissions import IsClientOrAdmin, IsAdmin, IsManagerOrAdmin

from .serializers import ProductSerializer
from .models import Product


class ProductList(mixins.ListModelMixin,
                  generics.GenericAPIView):
    http_method_names = ['get']
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsClientOrAdmin]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ProductCreate(mixins.CreateModelMixin,
                    generics.GenericAPIView):
    http_method_names = ['post']
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsAdmin]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProductDetail(mixins.RetrieveModelMixin,
                    generics.GenericAPIView):
    http_method_names = ['get']
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsClientOrAdmin]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ProductUpdate(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    http_method_names = ['get', 'put', 'delete']
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsManagerOrAdmin]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
