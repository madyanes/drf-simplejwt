from django.urls import path

from .views import RegisteringView

urlpatterns = [
    path('api/register/', RegisteringView.as_view(), name='sign_up')
]
