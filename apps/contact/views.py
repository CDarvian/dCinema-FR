from django.shortcuts import render

from .models import Ticket


# Create your views here.

def index(request):
    return render(request, 'contact/main.html')


def sended(request):
    ticket = Ticket(ticket_name=request.POST['author'], ticket_email=request.POST['email'],
                    ticket_text=request.POST['message'])
    ticket.save()

    return render(request, 'contact/sended.html')
