from rest_framework import generics, permissions, mixins, response
from django.utils.translation import ugettext_lazy as _

from .models import Project, ProjectCategory
from .serializers import ProjectSerializer, ProjectCategorySerializer
from .tasks import project_support_request

from accounts.permissions import IsAdmin, IsManagerOrAdmin, IsManagerClientOrAdmin
from client.models import Client
from community.models import Community


class ProjectList(mixins.ListModelMixin,
                  generics.GenericAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    http_method_names = ['get']
    permission_classes = [permissions.IsAuthenticated,
                          IsManagerClientOrAdmin]

    def get(self, request, *args, **kwargs):
        if request.GET.get('product_id', ''):
            product_id = int(request.GET.get('product_id', ''))
            communities = Community.objects.filter(products=product_id)
            queryset = Project.objects.filter(community__in=communities)
            serializer = self.get_serializer(queryset, many=True)

            return response.Response(serializer.data)

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
    http_method_names = ['get', 'post']
    permission_classes = [permissions.IsAuthenticated,
                          IsManagerClientOrAdmin]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if hasattr(request.user, 'client'):
            client_id = Client.objects.get(user=request.user).id
            project_id = kwargs.get('pk', '')
            project_support_request.delay(client_id, project_id)

            return response.Response(data={'message': _("Email enviado com sucesso")}, status=200)

        return response.Response(data={'message': _("É necessário ser cliente para apoiar um projeto")}, status=500)



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
