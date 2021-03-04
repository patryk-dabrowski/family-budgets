from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from user_profile.views import RegisterAPIView

urlpatterns = [
    path('token-auth/', obtain_auth_token, name='token_auth'),
    path('register/', RegisterAPIView.as_view(), name='register')
]
