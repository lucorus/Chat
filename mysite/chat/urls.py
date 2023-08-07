from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_page, name="main_page"),
    path("<str:room_name>/", views.room, name="room"),
    path('profile', views.profile, name='profile'),
    path('profile/<slug:slug>', views.profile, name='profile'),
    path('register', views.user_register, name='register'),
    path('logout', views.user_logout, name='logout'),
    path('login', views.user_login, name='login'),
]
