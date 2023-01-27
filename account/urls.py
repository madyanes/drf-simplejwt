from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from .views import MyTokenObtainPairView, RegisterView

urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='sign_up'),
    path('api/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
