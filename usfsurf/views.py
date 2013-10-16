# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader

from events.models import Event

def home(request):
    template = loader.get_template('events/index.html')
    context = RequestContext(request,{'upcoming_events_list': upcoming_events_list,})
    return HttpResponse(template.render(context))

