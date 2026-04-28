from django.urls import path
from .views import MyTokenObtainPairView
from .views import register_user

urlpatterns = [
    path("token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("register/", register_user),
]
