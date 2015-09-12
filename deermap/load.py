import os
from django.contrib.gis.utils import LayerMapping
from models import Sighting

sighting_mapping = {
	'objectid' : 'OBJECTID',
	'num_animal' : 'num_animal',
	'animal_type' : 'animal_typ',
	'sighting_date' : 'sighting_d',
	'additional' : 'additional',
  'geom' : 'MULTIPOINT',
}

deer_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'static/deermap/data/shp/sample_deer.shp'))

def run(verbose=True):
	lm = LayerMapping(Sighting, deer_shp, sighting_mapping, transform=False)
	lm.save(strict=True, verbose=verbose)
