from django.urls import include, path
# from rest_framework.routers import DefaultRouter

# from v1.views import UserViewSet

# app_name = 'api'

# router = DefaultRouter()
# router.register('users', UserViewSet, basename='users')


# urlpatterns = [
#     path('', include(router.urls)),
#     path('', include('djoser.urls')),
#     path('auth/', include('djoser.urls.authtoken')),
# ]

urlpatterns = [
    path('v1/', include('api.v1.urls')),
]
