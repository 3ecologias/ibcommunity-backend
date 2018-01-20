from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from accounts.views import UserList, UserDetail, UserCreate

urlpatterns = [
    # Users
    url(r'^list/$', UserList.as_view(), name='client-list'),
    url(r'^create/$', UserCreate.as_view(), name='client-create'),
    url(r'^detail/(?P<pk>[0-9]+)/$', UserDetail.as_view(), name='client-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)