from django.conf.urls import include, url

from hc.blog import views

urlpatterns = [
    url(r'^blogs/$', views.all_blogs, name="hc-blogs"),
    url(r'^new_blog/$', views.new_blogs, name="hc-new-blog")
]

