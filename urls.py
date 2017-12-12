from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^product/(?P<id>\d+)/$', views.product_like, name='product_like'),
    ]