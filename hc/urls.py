from django.conf.urls import include, url
from django.contrib import admin

from hc.accounts import views
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('hc.accounts.urls')),
    url(r'^', include('hc.api.urls')),
    url(r'^', include('hc.front.urls')),
    url(r'^', include('hc.payments.urls'))
]

handler404 = views.Error404View.as_error_view()
handler500 = views.Error500View.as_error_view()