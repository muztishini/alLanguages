from django.urls import path
# reset_password
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from my_user.views import \
    UserCreateView, UserRetrieveUpdateView, UpdatePasswordView, UpdateNativeView, UpdateLearnView

urlpatterns = [
    # user
    path('create/', UserCreateView.as_view(), name='create'),
    path('', UserRetrieveUpdateView.as_view(), name='retrieve-update'),
    # token
    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    # password
    path('update-password/', UpdatePasswordView.as_view(), name='update-password'),
    # path('reset-password/', reset_password),
    # path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    # update languages
    path('update-native', UpdateNativeView.as_view(), name='update-native'),
    path('update-learn', UpdateLearnView.as_view(), name='update-learn'),
]
