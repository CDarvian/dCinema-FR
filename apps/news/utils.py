from .models import News


def side_news(request):
    last_news = News.objects.latest('pub_date')

    return {'last_news': last_news}
