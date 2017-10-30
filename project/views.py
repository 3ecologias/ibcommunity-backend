from rest_framework import generics, permissions, mixins

from .models import Project, ProjectCategory
from .serializers import ProjectSerializer, ProjectCategorySerializer

from accounts.permissions import IsAdmin, IsManagerOrAdmin, IsManagerClientOrAdmin


class ProjectList(mixins.ListModelMixin,
                  generics.GenericAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    http_method_names = ['get']
    permission_classes = [permissions.IsAuthenticated,
                          IsManagerClientOrAdmin]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ProjectCreate(mixins.CreateModelMixin,
                    generics.GenericAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    http_method_names = ['post']
    permission_classes = [permissions.IsAuthenticated,
                          IsAdmin]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProjectDetail(mixins.RetrieveModelMixin,
                    generics.GenericAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    http_method_names = ['get', 'delete']
    permission_classes = [permissions.IsAuthenticated,
                          IsManagerClientOrAdmin]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ProjectUpdate(mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    http_method_names = ['put', 'get']
    permission_classes = [permissions.IsAuthenticated,
                          IsManagerOrAdmin]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ProjectCategoryList(mixins.ListModelMixin,
                          generics.GenericAPIView):

    queryset = ProjectCategory.objects.all()
    serializer_class = ProjectCategorySerializer
    http_method_names = ['get']
    permission_classes = [permissions.IsAuthenticated,
                          IsManagerClientOrAdmin]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ProjectCategoryCreate(mixins.CreateModelMixin,
                            generics.GenericAPIView):
    queryset = ProjectCategory.objects.all()
    serializer_class = ProjectCategorySerializer
    http_method_names = ['post']
    permission_classes = [permissions.IsAuthenticated,
                          IsAdmin]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProjectCategoryUpdate(mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            generics.GenericAPIView):
    queryset = ProjectCategory.objects.all()
    serializer_class = ProjectCategorySerializer
    http_method_names = ['get','put','delete']
    permission_classes = [permissions.IsAuthenticated,
                          IsManagerOrAdmin]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ProjectCategoryDetail(mixins.RetrieveModelMixin,
                            generics.GenericAPIView):
    http_method_names = ['get']
    queryset = ProjectCategory.objects.all()
    serializer_class = ProjectCategorySerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsManagerClientOrAdmin]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
