# URLs - API REFERENCE

URLs maps using in application.

## Base Auth for Tokens

* api/auth/
    * / -> include('djoser.urls')
    * / -> include('djoser.urls.jwt')
    * token/ -> obtain_jwt_token
    * refresh-token/ -> refresh_jwt_token
    * verify-token/ -> verify_jwt_token

## Base Auth URLs (end pont)

* api/auth/  (base path for auth)
    * list/ -> UserList, name='client-list'
    * create/ -> UserCreate, name='client-create'
    * detail/(?P<pk>[0-9]+)/ -> UserDetail, name='client-detail'

## Base User URLs (end points for Client and Profile)

* api/user/  (base path for users)
    * client/list/ -> ClientList, name='client-list'
    * client/create/ -> ClientCreate, name='client-create'
    * client/detail/(?P<pk>[0-9]+)/ -> ClientDetail, name='client-detail'

* api/user/ (base path for profile)
    * profile/list/ -> ProfileList, name='profile-list'
    * profile/create/ -> ProfileCreate, name='profile-create'
    * profile/detail/(?P<pk>[0-9]+)/ -> ProfileDetail, name='profile-detail'
    
    