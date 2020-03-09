from django.urls import path

from . import views

app_name = 'registration'
urlpatterns = [
    path('', views.register, name='register'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),

    path('user_police/', views.user_police, name='user_police'),
    path('conf_police/', views.conf_police, name='conf_police'),
]
