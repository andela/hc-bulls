from django.conf.urls import include, url

from hc.blog import views

urlpatterns = [
    url(r'^blogs/$', views.all_blogs,name="hc-blogs")
]

