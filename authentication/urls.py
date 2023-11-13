from django.urls import path
from .views import sign_up, CustomLoginView

app_name = 'authentication'

urlpatterns = [
   path("sign-up/", sign_up, name="sign_up"),
   path("login/", CustomLoginView.as_view(), name="login")
]