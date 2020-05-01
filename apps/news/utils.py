from .models import News


def side_news(request):
    last_news = News.objects.order_by('-pub_date')[:1]
    return {'last_news': last_news}
