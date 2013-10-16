from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from events.models import Event

@dajaxice_register()
def sayhello(request, event_id):
	event_id = event_id.replace("event_", "")
	event = Event.objects.get(id=event_id)
	return simplejson.dumps({
		'name': event.name, 
		'description': event.description,
		'date': str(event.date),
		'teaser_desc': event.teaser_desc,
		'teaser_img' : event.teaser_img,
		'event_img1' : event.event_img1,
		'event_img2' : event.event_img2,
		'event_img3' : event.event_img3,
	})