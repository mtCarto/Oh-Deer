from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render

from django.contrib.gis.geos import GEOSGeometry
import json
import math
from django.contrib import messages

#decorate!
from django.views.decorators.http import require_POST
#load model
from deermap.models import Sighting
#load forms
from deermap.forms import SightingForm
#may not need?
from deermap.views import indexContext

@require_POST
def postSighting(request):
	sightingForm = SightingForm(request.POST)
	sightingForm.data = sightingForm.data.copy()

	#convert coords 
	try:
		sightingForm.data['geom'] = normalizeGeometry(sightingForm.data['geom'])
	except(ValueError):
		messages.error(request, '<strong>Error</strong><br>No point was selected for request.')
		return HttpResponseRedirect(reverse('deermap:index'))

	if sightingForm.is_valid():
		sighting = sightingForm.save()
		alertUsers(request, sighting)

		messages.success(request, '<strong>Success!</strong><br>Your sighting was successfully added.')
		#may need a bunch of \ in kwargs below...
		return HttpResponseRedirect(reverse('deermap:index', 
						kwargs=({
										"lat":str(sighting.latlngList()[0]),
										"lng":str(sightings.latlngList()[1]),
										"zoom":str(18)
						})
		))
	else: #show errors in form
		sightingForm.data['geom'] = sightingForm.data['geom'].json
		return render(request, 'deermap/index.html', indexContext(request, sightingForm=sightingForm))

def normalizeGeometry(geom):
	#convert string GEOS to python dict
	geom = json.loads(geom)
	
	#normalize to [-180,180] range
	for i, c in enumerate(geom['coordinates']):
		geom['coordinates'][i] = (c+180 - ( math.floor( (c+180)/360) )*360) - 180

	#encode and return GEOS object
	return GEOSGeometry(json.dumps(geom))	
