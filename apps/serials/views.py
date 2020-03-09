from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render

from .models import Serial


# Create your views here.

def index(request):
    serial_list = Serial.objects.all()

    return render(request, 'serials/main.html', {'serial_list': serial_list})


def detail(request, serial_id):
    try:
        s = Serial.objects.get(id=serial_id)
    except ObjectDoesNotExist:
        raise Http404('Serial not found...')

    if request.method == 'POST':
        reviewer_name = request.POST['reviewer']
        review_text = request.POST['review']

        new_comment = s.comment_set.create(name_author=reviewer_name, comment_text=review_text)

    last_comments_list = s.comment_set.order_by('-id')[:5]

    return render(request, 'serials/detail.html', {'s': s, 'last_comments': last_comments_list})
