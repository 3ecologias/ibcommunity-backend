from django.conf.urls import url, include
from rest_framework_jwt import views as jwt_views

urlpatterns = [
    url(r'^account/', include('djoser.urls')),
    url(r'^auth/login/', jwt_views.obtain_jwt_token, name='auth'),
]
