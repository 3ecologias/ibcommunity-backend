from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ProjectList, ProjectDetail, ProjectUpdate, ProjectCreate, \
                   ProjectCategoryList, ProjectCategoryCreate, ProjectCategoryDetail, \
                   ProjectCategoryUpdate


urlpatterns = [
    # Projects
    url(r'^projects/$', ProjectList.as_view(), name='project-list'),
    url(r'^project/create/$', ProjectCreate.as_view(), name='project-create'),
    url(r'^project/update/(?P<pk>[0-9]+)/$', ProjectUpdate.as_view(), name='project-update'),
    url(r'^project/detail/(?P<pk>[0-9]+)/$', ProjectDetail.as_view(), name='project-detail'),

    # Project Categories
    url(r'^project/categories/$', ProjectCategoryList.as_view(), name='category-list'),
    url(r'^project/category/create/$', ProjectCategoryCreate.as_view(), name='category-create'),
    url(r'^project/category/detail/(?P<pk>[0-9]+)/$', ProjectCategoryDetail.as_view(), name='category-detail'),
    url(r'^project/category/update/(?P<pk>[0-9]+)/$', ProjectCategoryUpdate.as_view(), name='category-update'),
]


urlpatterns = format_suffix_patterns(urlpatterns)

