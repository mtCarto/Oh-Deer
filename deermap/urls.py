from django.conf.urls import patterns, url
#from django.views.generic import TemplateView
#from djgeojson.views import GeoJSONLayerView
#from deermap.models import Sighting
from deermap import views

urlpatterns = patterns('',
	#old but working --- url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
	# getlayerpoints returns geojson, to be displayed on map
	#old but working --- url(r'^data.geojson$', GeoJSONLayerView.as_view(model=Sighting), name='data'),
	#new index view
	url(r'^$', views.index, name='index'),
	url(r'^(?P<lat>-?\d{1,3}\.?\d*)_(?P<lng>-?\d{1,3}\.?\d*)/(?P<zoom>\d+)/?$', views.index, name='index'),
	
	#create new sighting
	url(r'^sighting_submit/$', views.postSighting, name='postSighting'),

	#admin url
	#about url
)
