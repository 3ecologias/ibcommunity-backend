from rest_framework import generics, permissions, mixins

from .models import Project, ProjectCategory
from .serializers import ProjectSerializer, ProjectCategorySerializer
from .permissions import IsAdmin, IsClientOrAdmin


class ProjectList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    http_method_names = ['get']
    permission_classes = [IsClientOrAdmin,
                          permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ProjectCreate(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    http_method_names = ['post']
    permission_classes = [IsAdmin,
                          permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProjectDetail(mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    http_method_names = ['get', 'delete']
    permission_classes = [IsClientOrAdmin,
                          permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ProjectUpdate(mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin,
                    generics.GenericAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    http_method_names = ['put', 'get']
    permission_classes = [IsClientOrAdmin,
                          permissions.IsAuthenticated,
                          permissions.IsAdminUser]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs   )

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class ProjectCategoryList(mixins.ListModelMixin,
                          generics.GenericAPIView):

    queryset = ProjectCategory.objects.all()
    serializer_class = ProjectCategorySerializer
    http_method_names = ['get']
    permission_classes = [IsClientOrAdmin,
                          permissions.IsAuthenticated,
                          permissions.IsAdminUser]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ProjectCategoryCreate(mixins.CreateModelMixin,
                            generics.GenericAPIView):
    queryset = ProjectCategory.objects.all()
    serializer_class = ProjectCategorySerializer
    http_method_names = ['post']
    permission_classes = [IsAdmin,
                          permissions.IsAuthenticated,
                          permissions.IsAdminUser]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProjectCategoryUpdate(mixins.UpdateModelMixin,
                            generics.GenericAPIView):
    queryset = ProjectCategory.objects.all()
    serializer_class = ProjectCategorySerializer
    http_method_names = ['put']
    permission_classes = [IsAdmin,
                          permissions.IsAuthenticated,
                          permissions.IsAdminUser]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class ProjectCategoryDetail(mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            generics.GenericAPIView):

    queryset = ProjectCategory.objects.all()
    serializer_class = ProjectCategorySerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)