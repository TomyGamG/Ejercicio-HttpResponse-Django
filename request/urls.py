from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('request/', views.request_page, name='request_page'),
    path('request/app-atributes/', views.app_atributes, name='app-atributes'),
    path('request/middleware/', views.middleware, name='middleware'),
    path('request/querydict/', views.querydict, name='querydict'),
    path('request/is-secure/', views.is_secure, name='is-secure'),
    path('home/', views.home, name='home'),
    path('response/', views.response, name='response'),
    path('response/subclasses/', views.subclasses, name='subclasses'),
    path('response/json/', views.json, name='json'),
    path('response/streaming/', views.streaming, name='streaming'),
    path('response/file/', views.file, name='file'),
    path('response/base/', views.base, name='base'),
]