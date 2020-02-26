from django.contrib.auth import views
from django.urls import path
from .views import RegisterFormView, LoginFormView,LogoutView

urlpatterns = [
    path('register/', RegisterFormView.as_view()),
    path('login/', LoginFormView.as_view()),
    path('logout/', LogoutView.as_view()),
]