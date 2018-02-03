from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

#from accounts.views import UserList, UserDetail, UserCreate
from accounts.api.views import UserCreateAPIView, UserListAPIView, UserDetailAPIView

urlpatterns = [
    # Users
    # path api/users/
    url(r'^list/$', UserListAPIView.as_view(), name='client-list'),
    url(r'^create/$', UserCreateAPIView.as_view(), name='client-create'),
    url(r'^detail/(?P<pk>[0-9]+)/$', UserDetailAPIView.as_view(), name='client-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)