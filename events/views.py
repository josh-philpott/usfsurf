# Create your views here.
import datetime
from django.http import HttpResponse
from django.template import RequestContext, loader

from events.models import Event

def index(request):
	upcoming_events_list = Event.objects.filter(date__gte=datetime.date.today()).order_by('date')[:10]
	previous_events_list = Event.objects.filter(date__lt=datetime.date.today()).order_by('date')[:10]
	template = loader.get_template('events/eventsindex.html')
	context = RequestContext(request,{'upcoming_events_list': upcoming_events_list, 'previous_events_list': previous_events_list})
	return HttpResponse(template.render(context))
