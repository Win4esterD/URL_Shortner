from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reg', views.register_request, name='registration'),
    path('login', views.login_request, name='login'),
    path("logout", views.logout_request, name= "logout"),
    path('create', views.create, name='create'),
    path('<str:pk>', views.go, name='go'),
]