from django.urls import path
from .views import permission, askPermit, home, loginn, logoutt, register

urlpatterns = [
    path("", home, name="home"),
    path("permissions/", permission, name="permissions-page"),
    path("askpermit/", askPermit, name="ask-permit"),
    path("login/", loginn, name="login"),
    path("register/", register, name="register"),
    path("logout/", logoutt, name="logout")\

]