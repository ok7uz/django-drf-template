from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from apps.account.views import ProfileView, LoginView, RegisterView

app_name = 'account'

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),

    path('login/', LoginView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('register/', RegisterView.as_view(), name='register'),
]
