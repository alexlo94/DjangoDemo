from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^employeelist/', views.employeelist, name = 'employeelist'),
    url(r'^positionlist/', views.positionlist, name = 'positionlist'),
]