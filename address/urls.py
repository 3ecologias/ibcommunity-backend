from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import AddressList, AddressDetail

urlpatterns = [
    url(r'^address/$', AddressList.as_view(), name='address-list'),
    url(r'^address/(?P<pk>[1-9]+)/$', AddressDetail.as_view(), name='address-detail' )
]

urlpatterns = format_suffix_patterns(urlpatterns)