from django.urls import path
from . import views

urlpatterns = [
    path('wantvk/', views.post_list, name='post_list'),

]