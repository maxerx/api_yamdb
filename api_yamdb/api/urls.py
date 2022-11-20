from rest_framework import routers
from django.urls import path
from .views import APISignup, APIGetToken

app_name = 'api'

urlpatterns = [
    path('v1/auth/signup/', APISignup.as_view(), name='signup'),
    path('v1/auth/token/', APIGetToken.as_view(), name='get_token')
]
