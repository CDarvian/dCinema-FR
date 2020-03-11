from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render

from .models import Movie


# Create your views here.

def index(request):
    movie_list = Movie.objects.all()

    return render(request, 'movies/main.html', {'movie_list': movie_list})


def detail(request, movie_id):
    try:
        m = Movie.objects.get(id=movie_id)
    except ObjectDoesNotExist:
        raise Http404('Movie not found...')

    if request.method == 'POST':
        reviewer_name = request.POST['reviewer']
        review_text = request.POST['review']
        reviewer_username = request.POST['username_author']

        new_comment = m.comment_set.create(name_author=reviewer_name, comment_text=review_text,
                                           username_author=reviewer_username)

    last_comments_list = m.comment_set.order_by('-id')[:5]

    return render(request, 'movies/detail.html', {'m': m, 'last_comments': last_comments_list})
