from .models import Movie


def side_movies(request):
    latest_movies_list = Movie.objects.order_by('-pub_date')[:4]

    return {'latest_movies_list': latest_movies_list}
