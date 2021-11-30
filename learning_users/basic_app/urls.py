from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path , re_path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    re_path (r'^register/$', views.register, name = 'joy_register' ),
    re_path (r'^user_login/$', views.joe_user_login, name = 'joy_user_login' ),
]
