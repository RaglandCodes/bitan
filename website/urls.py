from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('auth/signin/', views.sign_in, name='signin'),
    path('paraPartial/', views.paraPartial, name='paraPartial')
]