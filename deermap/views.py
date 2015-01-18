from django.shortcuts import render
from django.http import HttpResponse
from deer.forms import sightingForm
from models import Animal
from django.views.generic.edit import FormView

class sightingView(FormView):

	def new_sighting(request):
		if request.method == 'POST':
			form = sightingForm(request.POST)

			if form.is_valid():
				animal = Animal()
				animal.animal_type = form.cleaned_data.get('animal_type')
				animal.num_animal = form.cleaned_data.get('num_animal')
				animal.sighting_date = form.cleaned_data.get('sighting_date')
				animal.additional_info = form.cleaned_data.get('additional_info')
				animal.save()

		#return render_to_response('/sighting_submit/', context_instance=RequestContext(request))

# Create your views here.
