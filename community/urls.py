from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from .views import CommunityList, CommunityDetail

urlpatterns = [
    url(r'^community/$', CommunityList.as_view(), name='community-list'),
    url(r'^community/(?P<pk>[0-9]+)/$', CommunityDetail.as_view(), name='community-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)