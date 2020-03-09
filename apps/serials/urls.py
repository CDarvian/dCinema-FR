from django.urls import path

from . import views

app_name = 'serials'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:serial_id>/', views.detail, name='detail'),
]
