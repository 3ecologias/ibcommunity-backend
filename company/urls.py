from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import CompanyList, CompanyDetail

urlpatterns = [
    url(r'^company/$', CompanyList.as_view(), name='company-list'),
    url(r'^company/(?P<pk>[0-9]+)/$', CompanyDetail.as_view(), name='company-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)
