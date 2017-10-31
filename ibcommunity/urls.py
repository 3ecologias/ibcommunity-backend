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
    url(r'^admin/', admin.site.urls),
    url(r'^', include('accounts.urls', namespace='accounts')),
    url(r'^', include('project.urls', namespace='project')),
    url(r'^', include('company.urls', namespace='company')),
    url(r'^', include('address.urls', namespace='address')),
    url(r'^', include('product.urls', namespace='product')),
    url(r'^', include('community.urls', namespace='community')),
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.jwt')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)