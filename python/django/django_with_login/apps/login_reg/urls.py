from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^success$', views.success),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^', views.index)
]
