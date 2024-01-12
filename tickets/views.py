from django.shortcuts import render, loader
from django.http import HttpResponse
from .models import TicketInfo

# Create your views here.
def tickets(request):
    mytickets = TicketInfo.objects.all().values()
    template = loader.get_template('alltickets.html')
    context = {
        'mytickets': mytickets,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
  mytickets = TicketInfo.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mytickets': mytickets,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())