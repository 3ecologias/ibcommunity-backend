"""
ibcommunity URL Configuration
"""
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token


urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^', admin.site.urls),
    url(r'^api/user/', include('accounts.api.urls', namespace='accounts')), #API for Users - URLs
    url(r'^', include('project.urls', namespace='project')),
    url(r'^', include('company.urls', namespace='company')),
    url(r'^', include('address.urls', namespace='address')),
    url(r'^', include('product.urls', namespace='product')),
    url(r'^', include('community.urls', namespace='community')),
    url(r'^', include('providers.urls', namespace='providers')),

    url(r'^api/auth/', include('ibcommunity.api.urls')), # API Auth - URLs
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)