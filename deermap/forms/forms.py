from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import FormActions, Div
from crispy_forms.layout import Layout, Field, HTML, Submit, Reset

from deermap.models import Sighting

class SightingForm(forms.ModelForm):
	helper = FormHelper()
	helper.form_tag = False

	helper.layout = Layout(
		HTML("<br>"),
			#'Sighting Details',
			Field('geom', type="hidden", id="point"),
			Field('animal_type'),
			Field('num_animal'),
			Field('sighting_date', id="sighting_date", template='deermap/datepicker.html', autocomplete='off'),
			Field('additional'),
		Div(
			HTML("""
				<input type='checkbox' class='terms'>
					<strong> I have read and understand the terms.</strong>
				
				<script>
					$(".terms").change(function() {
						if(this.checked) {
							$(".submitBtnSighting").removeClass("disabled");
						} else {
							$(".submitBtnSighting").addClass("disabled");
						}
					});
				</script>
			"""),
		),
		Div(
			FormActions(
				Reset('cancel', 'Cancel', onclick="$('#sightingForm').modal('hide');$('.modal-backdrop').hide();"),
				Submit('save', 'Submit', css_class="disabled submitBtnSighting"),
			),
			css_class='modal-footer'
		),
	)
	
	class Meta:
		model = Sighting
		fields = ['geom','sighting_date','animal_type','num_animal','additional']

