from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^hello/', views.hello, name='hello'),
    url(r'^article/(\d+)/', views.article, name='article'),
]
