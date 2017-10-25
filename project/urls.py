from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ProjectList, ProjectDetail, ProjectCategoryList, ProjectCategoryDetail


urlpatterns = [
    url(r'^project/$', ProjectList.as_view(), name='project-list'),
    url(r'^project/(?P<pk>[0-9]+)/$', ProjectDetail.as_view(), name='project-detail'),
    url(r'^project/category/$', ProjectCategoryList.as_view(), name='category-list'),
    url(r'^project/category/(?P<pk>[0-9]+)/$', ProjectCategoryDetail.as_view(), name='category-detail'),
]


urlpatterns = format_suffix_patterns(urlpatterns)

