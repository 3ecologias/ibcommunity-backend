from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import ProductList, ProductDetail

urlpatterns = [
    url(r'^product/$', ProductList.as_view(), name='product-list'),
    url(r'^product/(?P<pk>[0-9]+)/$', ProductDetail.as_view(), name='product-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)