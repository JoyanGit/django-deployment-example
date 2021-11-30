from django.conf.urls import url
from basic_app import views
from django.urls import path, re_path

# Template tagging :
app_name = 'basic_app'

urlpatterns = [
    re_path(r'^relative/$', views.relative, name = 'Joyan_Relative' ),
    re_path(r'^other/$', views.other, name = 'Joyan_Other' ),
]
