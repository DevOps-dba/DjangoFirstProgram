from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^hello/', views.hello, name='hello'),
    url(r'^article/(\d+)/', views.article, name='article'),
    url(r'^mysql_test/', views.mysql_test, name='mysql_test'),
    url(r'^index/', views.index, name='index'),
]
