from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render
from movies.models import Movie
from news.models import News
from serials.models import Serial


def index(request):
    latest_serials_list = Serial.objects.order_by('-pub_date')[:4]
    latest_news_list = News.objects.order_by('-pub_date')[:5]

    return render(request, 'index/main.html',
                  {'latest_serials_list': latest_serials_list, 'latest_news_list': latest_news_list})


def rating(request):
    movies_list = Movie.objects.all()

    return render(request, 'index/rating.html', {'movies_list': movies_list})


def profile(request, user_login):
    try:
        user = User.objects.get(username=user_login)
    except UnboundLocalError:
        Http404('User not found...')

    return render(request, 'profile.html', {'usr': user})
