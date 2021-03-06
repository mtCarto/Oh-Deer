from django.shortcuts import render

#load model
from deermap.models import Sighting
#load forms
from deermap.forms import SightingForm

def index(request, lat=None, lng=None, zoom=None):
	context = indexContext(request)
	
	#center and zoom if available
	if not None in [lat,lng, zoom]:
		context['lat']=float(lat)
		context['lng']=float(lng)
		context['zoom']=int(zoom)
	
	return render(request, 'deermap/index.html', context)

#define default context data for index
def indexContext(request, sightingForm=SightingForm()):
	sightings = Sighting.objects.all()

	return {
		#model data used for map
		'deer': sightings.filter(animal_type__contains="deer"),

		#Form data used for map
		"sightingForm": sightingForm
	}

