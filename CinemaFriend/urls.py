"""CinemaFriend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from CinemaFriend import views

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')),

    path('accounts/profile/<str:user_login>/', views.profile, name='profile'),

    path('accounts/register/', include('registration.urls')),

    path('', views.index, name='index'),
    path('rating/', views.rating, name='rating'),

    path('news/', include('news.urls')),
    path('movies/', include('movies.urls')),
    path('serials/', include('serials.urls')),
    path('contact/', include('contact.urls')),
]
