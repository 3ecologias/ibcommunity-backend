from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from .views import ProfileList, ProfileDetail, ProfileCreate,\
                   ClientList, ClientDetail, ClientCreate,\
                   UserList, UserDetail, UserCreate

urlpatterns = [
    # Profile
    url(r'^profiles/$', ProfileList.as_view(), name='profile-list'),
    url(r'^profile/create/$', ProfileCreate.as_view(), name='profile-create'),
    url(r'^profile/(?P<pk>[0-9]+)/$', ProfileDetail.as_view(), name='profile-detail'),

    # Client
    url(r'^clients/$', ClientList.as_view(), name='client-list'),
    url(r'^client/create/$', ClientCreate.as_view(), name='client-create'),
    url(r'^client/(?P<pk>[0-9]+)/$', ClientDetail.as_view(), name='client-detail'),

    # Users
    url(r'^users/$', UserList.as_view(), name='client-list'),
    url(r'^user/create/$', UserCreate.as_view(), name='client-create'),
    url(r'^user/(?P<pk>[0-9]+)/$', UserDetail.as_view(), name='client-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)