from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render

from .models import News


# Create your views here.

def detail(request, news_id):
    try:
        n = News.objects.get(id=news_id)
    except ObjectDoesNotExist:
        raise Http404('News not found...')

    if request.method == 'POST':
        reviewer_name = request.POST['reviewer']
        review_text = request.POST['review']
        reviewer_username = request.POST['username_author']

        new_comment = n.comment_set.create(name_author=reviewer_name, comment_text=review_text,
                                           username_author=reviewer_username)

    last_comments_list = n.comment_set.order_by('-id')[:5]

    return render(request, 'news/detail.html', {'n': n, 'last_comments': last_comments_list})
